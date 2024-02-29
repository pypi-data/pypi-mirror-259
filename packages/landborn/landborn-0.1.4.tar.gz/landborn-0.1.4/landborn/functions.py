import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import pandas as pd
import matplotlib.patches as patches
from matplotlib.path import Path

def barplot(df, xvar, yvar, orientation='vertical', color='lightblue', axis=None, save_path=None):
    if axis is None:
        fig, axis = plt.subplots()

    if orientation == 'vertical':
        if isinstance(xvar, str):
            categories = df[xvar].unique()
            x = np.arange(len(categories))
            heights = df.groupby(xvar)[yvar].mean()
            errors = df.groupby(xvar)[yvar].sem()
        else:
            x = xvar
            heights = x.mean()
            errors = x.sem()
        bars = []
        for i, (category, height) in enumerate(zip(categories, heights)):
            error_line = mlines.Line2D([x[i], x[i]], [height-(errors[category]/2), height+(errors[category]/2)], color='black')
            error_line_top = mlines.Line2D([x[i] - 0.1, x[i] + 0.1], [height+(errors[category]/2), height+(errors[category]/2)], color='black')
            error_line_bottom = mlines.Line2D([x[i] - 0.1, x[i] + 0.1], [height-(errors[category]/2), height-(errors[category]/2)], color='black')
            rect = patches.Rectangle((x[i] - 0.4, 0), 0.8, height,facecolor=color, edgecolor='black')
            bars.append(rect)
            axis.add_patch(rect)
            axis.add_line(error_line)
            axis.add_line(error_line_top)
            axis.add_line(error_line_bottom)

        axis.set_xticks(x)
        axis.set_xticklabels(categories)
        axis.set_xlabel(xvar)
        axis.set_ylabel(yvar)
        axis.autoscale()
        axis.set_ylim(bottom=0)

    elif orientation == 'horizontal':
        # Horizontal bar plot
        categories = df[yvar].unique()
        y = np.arange(len(categories))
        heights = df.groupby(yvar)[xvar].mean()
        errors = df.groupby(yvar)[xvar].sem()

        bars = []
        for i, (category, height) in enumerate(zip(categories, heights)):
            rect = patches.Rectangle((0, y[i] - 0.4), height, 0.8,facecolor=color, edgecolor='black')
            bars.append(rect)
            axis.add_patch(rect)

        axis.set_yticks(y)
        axis.set_yticklabels(categories)
        axis.set_ylabel(yvar)
        axis.set_xlabel(xvar)
        axis.autoscale()
        axis.set_xlim(0)
    if save_path:
        plt.savefig(save_path)

    return axis


def lineplot(df, x=[], y=[], color='k', size=1, style='-', marker=None, ax=None, save_path=None):
    if ax is None:
        fig, ax = plt.subplots()

    if isinstance(x, str) and df is not None:
        xdata = df[x]
    else:
        xdata = x
    if isinstance(y, str):
        ydata = df[y]
    else:
        ydata = y

    line = mlines.Line2D(xdata, ydata, color=color, linestyle=style, marker=marker, markersize=size)
    ax.add_line(line)
    ax.autoscale()
    
    if save_path:
        plt.savefig(save_path)

    return ax


def scatterplot(df, xvar, yvar, color='k',colormap='viridis', size=1, marker='.', ax=None, save_path=None):
    if ax is None:
        fig, ax = plt.subplots()
    if isinstance(xvar, str):
        xdata = df[xvar]
    else:
        xdata = xvar
        
    if isinstance(yvar, str):
        ydata = df[yvar]
    else:
        ydata = yvar
    
    patches_li = []
    for i, (x, y) in enumerate(zip(xdata, ydata)):
        #creating small square for "point"
        verts = [
        (x, y),  #left, bottom
        (x, y + .5),  #left, top
        (x + .5, y + .5),  #right, top
        (x + .5, y),  #right, bottom
        (x, y),  #back to start
        ]

        codes = [
            Path.MOVETO,
            Path.LINETO,
            Path.LINETO,
            Path.LINETO,
            Path.CLOSEPOLY,
        ]
        path = Path(verts, codes)
        patch = patches.PathPatch(path, lw=1, color=color)
        patches_li.append(patch)
    
    for patch in patches_li:
        ax.add_patch(patch)
    ax.set_xlim(min(xdata), max(xdata))
    ax.set_ylim(min(ydata), max(ydata))
    ax.autoscale()
    ax.legend()
    
    if save_path:
        plt.savefig(save_path)
        
    # plt.show()
    return ax


def jointplot(x, y, ax=None, color='black', title='Joint Plot', save_path=None):
    fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True) #create two plots

    #top line plot
    axs[0].set_title(title)
    axs[0].tick_params(axis='x',which='both', bottom=False,top=False,labelbottom=False)
    axs[0].spines['bottom'].set_visible(False)
    axs[0].spines['right'].set_visible(False)
    axs[0].spines['top'].set_visible(False)
    lineplot(None,x,y, color=color, ax=axs[0])

    #bottom scatterplot
    axs[1].spines['top'].set_visible(False)
    axs[1].spines['right'].set_visible(False)
    axs[1].set_xlabel('X axis')
    scatterplot(None, x,y, color=color, ax=axs[1])
    
    if save_path:
        plt.savefig(save_path)


