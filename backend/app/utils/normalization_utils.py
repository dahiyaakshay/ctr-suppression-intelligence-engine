import pandas as pd

def min_max_normalize(series: pd.Series):
    min_val = series.min()
    max_val = series.max()

    if max_val - min_val == 0:
        return 0

    return (series - min_val) / (max_val - min_val)
