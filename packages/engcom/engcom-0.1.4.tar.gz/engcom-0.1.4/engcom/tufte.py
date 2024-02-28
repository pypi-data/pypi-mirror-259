"""Tufte styling for matplotlib plots"""
import numpy as np
import matplotlib.ticker
import matplotlib.pyplot as plt
import importlib
import sys

# mpl.use("pgf")
# plt.rcParams.update({
#     "pgf.texsystem": "lualatex",
#     "font.family": "serif",  # use serif/main font for text elements
#     "text.usetex": True,     # use inline math for ticks
#     "pgf.rcfonts": False,    # don't setup fonts from rc parameters
#     "pgf.preamble": "\n".join([
#          r"\RequirePackage[T1]{fontenc}%",
#          r"\usepackage{newpxmath} % math font is Palatino compatible",
#          r"\let\Bbbk\relax % so it doesn't clash with amssymb",
#          r"\usepackage[no-math]{fontspec}",
#          r"\setmainfont{Palatino}",
#          r"\setmonofont{Latin Modern Mono}[%",
#          r"Scale=1.05, % a touch smaller than MatchLowercase",
#          r"BoldFont=*,",
#          r"BoldFeatures={FakeBold=2}",
#          r"]",
#          r"\setsansfont{Helvetica}",
#     ])
# })

params = {
    "pgf.texsystem": "lualatex",
    "font.family": "serif",  # use serif/main font for text elements
    "font.serif": ["Palatino"],
    "mathtext.fontset": "cm",
    "pgf.rcfonts": True,    # don't setup fonts from rc parameters
    "axes.formatter.use_mathtext": True,
    "savefig.bbox": "tight",
    "font.size": 8,
    "axes.labelsize": 8,            
    "axes.titlesize": 8,     
    "figure.labelsize": 8,        
    "legend.fontsize": 8,   
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "text.usetex": False,     # use inline math for ticks
    "pgf.preamble": "\n".join([
         r"\RequirePackage[T1]{fontenc}%",
         r"\usepackage{newpxmath} % math font is Palatino compatible",
         r"\let\Bbbk\relax % so it doesn't clash with amssymb",
         r"\usepackage[no-math]{fontspec}",
         r"\setmainfont{Palatino}",
         r"\setmonofont{Latin Modern Mono}[%",
         r"Scale=1.05, % a touch smaller than MatchLowercase",
         r"BoldFont=*,",
         r"BoldFeatures={FakeBold=2}",
         r"]",
         r"\setsansfont{Helvetica}",
         r"\renewcommand{\mathdefault}[1][]{}",
    ])
}

def plot(x, y, 
    locator=None, 
    axis=0, 
    xlabel=None, 
    ylabel=None, 
    labels=None, 
    legend=None, 
    legendloc="outside right",
    save=False, 
    figsize=(5,5/1.618), 
    dotsize=10,
    color="black",
    points=True,
    cmap=plt.get_cmap('coolwarm'),
    xticks=None,
):
    if save:
        if "matplotlib" in sys.modules:
            print("reloading mpl")
            importlib.reload(matplotlib)
            mpl = matplotlib
        else:
            import matplotlib as mpl
        mpl.use('pgf') # Use the pgf backend (must be set before pyplot imported)
        if "matplotlib.pyplot" in sys.modules:
            print("reloading plt")
            importlib.reload(matplotlib.pyplot)
            plt = matplotlib.pyplot
        else:
            import matplotlib.pyplot as plt
        plt.rcParams.update(params)
        plt.rcParams["figure.figsize"] = figsize
    else:
        import matplotlib as mpl
        import matplotlib.pyplot as plt
    fig, ax = plt.subplots(layout="constrained")
    if len(y.shape) > 1:
        bxis = (axis+1)%2  # The axis we're not plotting along (i.e., the potentially multiple-trace axis)
        m = y.shape[bxis]  # Number of traces
    else:
        bxis = None
        m = 1
    if color == "map":
        colors = cmap(np.linspace(0, 1, m))
    else:
        colors = [color] * m  #  All the same color
    for i in range(m):
        if bxis is None:
            yi = y
        else:
            yi = y.take(indices=i,axis=bxis)
        if points:
            ax.plot(x, yi, linestyle="-", color=colors[i], linewidth=1, zorder=1)
            ax.scatter(x, yi, color="white", s=dotsize+30, zorder=2)
            ax.scatter(x, yi, color=colors[i], s=dotsize, zorder=3)
        else:
            ax.plot(x, yi, linestyle="-", color=colors[i], linewidth=1, zorder=1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_bounds(np.min(x), np.max(x))
    ax.spines["left"].set_bounds(np.min(y), np.max(y))
    if locator:
        ax.yaxis.set_major_locator(
            matplotlib.ticker.MultipleLocator(base=locator)
        )
    ax.tick_params(direction="in")
    if xticks is not None:
        ax.set_xticks(xticks)
    if xlabel:
        ax.set_xlabel(xlabel, loc="right")
    if ylabel:
        ax.text(x=0, y=1.0, s=ylabel, transform=ax.transAxes)
    if labels:
        for i in range(y.shape[(axis+1)%2]):
            yi = y.take(indices=i,axis=(axis+1)%2).flatten()
            ax.text(x=x[-1], y=yi[-1], s=f"\\ \\ \\ {labels[i]}", verticalalignment="center")
    if legend:
        fig.legend(legend, loc=legendloc)
    if save:
        plt.savefig(save,bbox_inches='tight')
    return fig, ax

def bar(x, y,
    axis=0, 
    xlabel=None, 
    ylabel=None, 
    labels=None, 
    save=False, 
    figsize=(5,5/1.618), 
    barsize=0.6,
    color="black",
):
    if save:
        if "matplotlib" in sys.modules:
            print("reloading mpl")
            importlib.reload(matplotlib)
            mpl = matplotlib
        else:
            import matplotlib as mpl
        mpl.use('pgf') # Use the pgf backend (must be set before pyplot imported)
        if "matplotlib.pyplot" in sys.modules:
            print("reloading plt")
            importlib.reload(matplotlib.pyplot)
            plt = matplotlib.pyplot
        else:
            import matplotlib.pyplot as plt
        plt.rcParams.update(params)
        plt.rcParams["figure.figsize"] = figsize
    else:
        import matplotlib as mpl
        import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    for i in range(y.shape[(axis+1)%2]):
        yi = y.take(indices=i,axis=(axis+1)%2)
        ax.bar(x, y, color=color, width=barsize)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    # ... TODO incomplete
    # if locator:
    #     ax.yaxis.set_major_locator(
    #         matplotlib.ticker.MultipleLocator(base=locator)
    #     )
    # ax.tick_params(direction="in")
    # if xlabel:
    #     ax.set_xlabel(xlabel, loc="right")
    # if ylabel:
    #     ax.text(x=0, y=1.0, s=ylabel, transform=ax.transAxes)
    # if legend:
    #     for i in range(y.shape[(axis+1)%2]):
    #         yi = y.take(indices=i,axis=(axis+1)%2).flatten()
    #         ax.text(x=x[-1], y=yi[-1], s=f"\\ \\ \\ {legend[i]}", verticalalignment="center")
    # if save:
    #     plt.savefig(save,bbox_inches='tight')
    # return fig, ax
