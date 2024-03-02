import random 
import numpy as np
import torch
import pandas as pd

from scipy.signal import convolve
from scipy import ndimage
from matplotlib.lines import Line2D


def get_dna_seq(tokens, tokenizer):
	# Convert n-mers tokens into a DNA sequence
	seq = tokenizer.from_seq(tokens)
	seq = [s for s in seq if "<" not in s]
	
	seq = seq[0][0] + "".join([s[1] for s in seq]) + seq[-1][-1]
	
	return seq

def set_seed(seed: int):
	"""
	Helper function for reproducible behavior to set the seed in ``random``, ``numpy``, ``torch`` and/or ``tf`` (if
	installed).

	Args:
		seed (:obj:`int`): The seed to set.
	"""
	random.seed(seed)
	np.random.seed(seed)
	torch.manual_seed(seed)
	torch.cuda.manual_seed_all(seed)
	

def _moment(a, moment, axis, *, mean=None):
	if np.abs(moment - np.round(moment)) > 0:
		raise ValueError("All moment parameters must be integers")

	# moment of empty array is the same regardless of order
	if a.size == 0:
		return np.mean(a, axis=axis)

	dtype = a.dtype.type if a.dtype.kind in 'fc' else np.float64

	if moment == 0 or (moment == 1 and mean is None):
		# By definition the zeroth moment is always 1, and the first *central*
		# moment is 0.
		shape = list(a.shape)
		del shape[axis]

		if len(shape) == 0:
			return dtype(1.0 if moment == 0 else 0.0)
		else:
			return (np.ones(shape, dtype=dtype) if moment == 0
					else np.zeros(shape, dtype=dtype))
	else:
		# Exponentiation by squares: form exponent sequence
		n_list = [moment]
		current_n = moment
		while current_n > 2:
			if current_n % 2:
				current_n = (current_n - 1) / 2
			else:
				current_n /= 2
			n_list.append(current_n)

		# Starting point for exponentiation by squares
		mean = (a.mean(axis, keepdims=True) if mean is None
				else dtype(mean))
		a_zero_mean = a - mean

		eps = np.finfo(a_zero_mean.dtype).resolution * 10
		with np.errstate(divide='ignore', invalid='ignore'):
			rel_diff = np.max(np.abs(a_zero_mean), axis=axis) / np.abs(mean)
		with np.errstate(invalid='ignore'):
			precision_loss = np.any(rel_diff < eps)
		n = a.shape[axis] if axis is not None else a.size
		if precision_loss and n > 1:
			message = ("Precision loss occurred in moment calculation due to "
					   "catastrophic cancellation. This occurs when the data "
					   "are nearly identical. Results may be unreliable.")
			warnings.warn(message, RuntimeWarning, stacklevel=4)

		if n_list[-1] == 1:
			s = a_zero_mean.copy()
		else:
			s = a_zero_mean**2

		# Perform multiplications
		for n in n_list[-2::-1]:
			s = s**2
			if n % 2:
				s *= a_zero_mean
		return np.mean(s, axis)

def visualisation(target_dmr: pd.Series, reads: pd.DataFrame, fname: str, figsize = None, gt_label="ctype_label", **kwargs):

	if "length" not in target_dmr.keys():
	    target_dmr["length"] = target_dmr["end"] - target_dmr["start"] + 1
	reads["gt"] = reads[gt_label]
	methyl_patterns = np.ones((len(read.index), target_dmr["length"]))*3 # 3 == loci not covered by reads
	reads =reads.sort_values(by="gt")

	if "pred" in reads.keys():
		reads =reads.sort_values(by="pred")

	# Read-level patterns
	for ri, index in enumerate(read.index):
	    
	    methyl_patt = list(reads.loc[index, "methyl_seq"])    
	    read_pos = reads.loc[index, "ref_pos"]+1 # The first locus does not have a methyl pattern due to 3-mers
	    read_pos_end = read_pos + len(methyl_patt)

	    # Determine start idx both on the read in the plot
	    if read_pos < target_dmr["start"]:
	    	# If a read starts before the DMR start pos
	        read_start = target_dmr["start"] - read_pos
	        pattern_start = 0
	    else:
	        read_start = 0
	        pattern_start = read_pos - target_dmr["start"]
	    
	    # Determine end idx both on the read and in the plot
	    if read_pos_end > target_dmr["end"]:
	    	# If read ends after the DMR end
	        read_end = target_dmr["end"] - read_pos + 1
	        pattern_end = target_dmr["length"]
	    else:
	        read_end = len(methyl_patt)+1
	        pattern_end = read_pos_end - target_dmr["start"]
	    
	    # Get patterns from the read    
	    methyl_patt = np.array(methyl_patt)[read_start:int(read_end)]
	    # Put the read pattern in the plot 
	    methyl_patterns[ri, pattern_start:pattern_end] = methyl_patt

	# DataFrame is for seaborn clustermap 
	methyl_patterns = pd.DataFrame(methyl_patterns)
	methyl_patterns.columns = range(target_dmr.start, int(target_dmr.end+1))

	methyl_patterns["Ground-truth"] = reads.loc[idces, "gt"].tolist()
	if "pred" in reads.keys():
		methyl_patterns["Prediction"] = reads.loc[idces,"pred"].tolist()
	methyl_patterns.index = idces # move read indices to plot index 
	

	lut = dict(zip([0,1], "brg"))
	methyl_patterns = methyl_patterns.sort_values(by=["Ground-truth","Prediction"])# 
	row_colors = methyl_patterns["Ground-truth"].map(lut)
	pred_row_colors = methyl_patterns["Prediction"].map(lut)
	sns.set(font_scale=1, style="white")
	sns.clustermap(methyl_patterns.iloc[:,:-2],
	               #figsize= (70, 50),
	               figsize=(15,8), 
	               row_colors=pd.concat([pred_row_colors, row_colors], axis=1), 
	               #row_colors=pd.concat([pred_row_colors], axis=1), 
	               row_cluster=False, col_cluster=False, cbar_pos=None,
	               cmap=["yellow", "black", "grey", "white"])

	plt.axhline(y=cpos, color="gray", linestyle="--")
	plt.xticks([])
	plt.yticks([])

	# Label tumour and normal 
	legend_elements = [Line2D([0], [0], color='r', lw=4, label='Tumour'),
	                   Line2D([0], [0], color='b', lw=4, label='Normal')]
	plt.legend(handles=legend_elements,bbox_to_anchor=(.5, -.2), loc='lower center', ncol=2)
	plt.title("DMR ID %d %s:%d-%d"%(DMR_ID, target_dmr.chr,target_dmr.start,target_dmr.end))

	#plt.savefig("/home/yuni/icgc/DL_project/methylbert/imgs/dmr%d_read_classification.png"%DMR_ID, dpi=300, bbox_inches="tight")
	#plt.savefig("/home/yuni/icgc/DL_project/methylbert/imgs/dmr%d_read_classification.pdf"%DMR_ID, format="pdf", dpi=300, bbox_inches="tight")
