import numpy as np
from scipy.stats import mode
from .api_resample import resample_2D_mean, resample_3D_mean
from joblib import Parallel, delayed
def aggregate(x, exc_shape, ignore_nodata=None):
    """
    x: 2D array
    exc_shape: tuple of (rows, cols)
    return: 2D array
    """
    cur_rows, cur_cols = x.shape
    exc_rows, exc_cols = exc_shape
    rw = cur_rows / exc_rows
    cw = cur_cols / exc_cols
    
    x = np.pad(x, ((0, int(rw+1)), (0, int(cw+1))), 'constant', constant_values=np.nan)
    x[np.isinf(x)] = np.nan
    
    if ignore_nodata is not None:
        x[x==ignore_nodata] = np.nan
    
    x_min = np.nanmin(x)-1
    x = x - x_min # x >= 1

    x[np.isnan(x)] = 0 # 0 is the missing value
    x = x.astype(np.float64)
    y = np.full(exc_shape, np.nan).astype(np.float64)
    y = resample_2D_mean(x, y, rw, cw, exc_rows, exc_cols, 0) # 0 is the missing value
    y = np.asarray(y) + x_min
    
    return y


def aggregate3D(x, exc_shape, ignore_nodata=None):
    """
    x: 2D array
    exc_shape: tuple of (rows, cols)
    return: 2D array
    """
    cur_times, cur_rows, cur_cols = x.shape
    exc_times, exc_rows, exc_cols = exc_shape
    rw = cur_rows / exc_rows
    cw = cur_cols / exc_cols
    
    x = np.pad(x, (0, (0, int(rw+1)), (0, int(cw+1))), 'constant', constant_values=np.nan)
    x[np.isinf(x)] = np.nan
    
    if ignore_nodata is not None:
        x[x==ignore_nodata] = np.nan
    
    x_min = np.nanmin(x)-1
    x = x - x_min # x >= 1

    x[np.isnan(x)] = 0 # 0 is the missing value
    x = x.astype(np.float64)
    y = np.full(exc_shape, np.nan).astype(np.float64)
    y = resample_3D_mean(x, y, rw, cw, exc_times, exc_rows, exc_cols, 0) # 0 is the missing value
    y = np.asarray(y) + x_min
    
    return y

def aggregate3D_v2(data, exc_shape, n_jobs=-1):
    res = Parallel(n_jobs)(delayed(aggregate)(data_i, exc_shape) for data_i in data)
    res = np.array(res)
    return res


def nanmode(data, axis=-1):
    mask = np.sum(np.isnan(data), axis=axis)==0
    data_np = data[mask].astype(np.int32)
    data_sy = data[~mask] # (1, 36)

    # 求第三个维度上的众数
    if data_np.size > 0:
        res_np = np.apply_along_axis(lambda x: np.argmax(np.bincount(x)), axis=axis, arr=data_np)
    else:
        res_np = None
        
    if data_sy.size > 0:
        res_sy = mode(data_sy, axis=axis, nan_policy='omit').mode
    else:
        res_sy = None

    result = np.full(mask.shape, np.nan)
    result[mask] = res_np
    result[~mask] = res_sy
    
    return result


def slide_win_npy(data, step=10, winsize=10):
    l_ws = winsize//2 # 中心点左和上侧边长
    r_ws = winsize - l_ws # 中心点右和下侧边长
    height, width, bands = data.shape
    
    x_range = np.arange(l_ws, height+l_ws, step).astype(int)
    y_range = np.arange(l_ws, width+l_ws, step).astype(int)
    data = np.concatenate((data, data[:, :winsize, :]), axis=1) # (2400, 14410, 13)
    data = np.pad(data, ((0, winsize), (0, 0), (0, 0)), mode='constant', constant_values=np.nan) # (2410, 14410, 13)
    
    res_list = []
    for i in x_range:
        i_start = i - l_ws
        i_end = i + r_ws
        for j in y_range:
            j_start = j - l_ws
            j_end = j + r_ws
            res_list.append(data[i_start:i_end, j_start:j_end])

    res = np.array(res_list).reshape(len(x_range), len(y_range), winsize, winsize, bands)
    return res