import numpy as np
arr = np.arange(15) #[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
def gen_strides(a, stride_len=5, window_len=5):
    n_strides = ((a.size-window_len)//stride_len) + 1
    # return np.array([a[s:(s+window_len)] for s in np.arange(0, a.size, stride_len)[:n_strides]])
    return np.array([a[s:(s+window_len)] for s in np.arange(0, n_strides*stride_len, stride_len)])
print(gen_strides(arr, stride_len=2, window_len=4))
#???