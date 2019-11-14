import numpy as np
import seaborn as sns


def permutation(arr, n1, n2):
    n = n1 + n2
    arr = np.random.permutation(arr)
    return arr[:n1], arr[n1:]


def plot_box(data, x, y, ax):
    sns.boxplot(x=x, y=y, data=data, width=0.3, ax=ax)


def plot_hist(data, axv_line, ax, is_cum=False):
    if is_cum:
        sns.distplot(data, bins=50, norm_hist=True, hist_kws={'cumulative': True}, kde=False, ax=ax)
        ax.set_yticks(np.linspace(0., 1., 11))
    else:
        sns.distplot(data, bins=50, ax=ax)
    ax.axvline(axv_line, color='k')
    ax.grid()