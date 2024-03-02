###
 # @file   plotting.py
 # @author Oscar Villemaud <oscar.villemaud@epfl.ch>
 #
 # @section LICENSE
 #
 # Copyright © 2024-2026 École Polytechnique Fédérale de Lausanne (EPFL).
 # All rights reserved.
 #
 # @section DESCRIPTION
 #
 # Plotting functions based on pyplot.
###

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import colors


def _finalize_plot(title, xlab, ylab, fontsize, savepath, extension, show):   
    plt.title(title)  
    plt.xlabel(xlab, size=fontsize)
    plt.ylabel(ylab, size=fontsize)
    if savepath is not None:
        plt.savefig(f"{savepath}.{extension}")
    if show:
        plt.show()
    plt.close()


def plot(data, legend=None, title="", log=False):
    """ simple plotting function """
    def _plot_scaled(curve):
        if log:
            plt.semilogy(curve)
        else:
            plt.plot(curve)
    if not hasattr(data[0], '__iter__'):
        _plot_scaled(data)
    else:
        for curve in data:
            _plot_scaled(curve)
    if legend is not None:
        plt.legend(legend)
    plt.title(title)
    plt.show()
    plt.close()


def seeds_plot(
    list_list, legend=None, x_vals=None, color=None, style=None, 
    xlog=False, ylog=False, confidence=True, std=False, plot_all=False, x_vlines=False):
    """ plots one line and confidence interval from multiple seeds """
    if len(list_list) == 0:
        return
    def _log_switch_plot(values, x_vals):
        if ylog and xlog:
            plt.loglog(x_vals, values, label=legend, linestyle=style, color=color)
        elif ylog and not xlog:
            plt.semilogy(x_vals, values, label=legend, linestyle=style, color=color)
        elif xlog and not ylog:
            plt.semilogx(x_vals, values, label=legend, linestyle=style, color=color)    
        else:
            plt.plot(x_vals, values, label=legend, linestyle=style, color=color)
    nb_samples = len(list_list)
    if plot_all:    
        for values in list_list:
            if x_vals is None:
                x_vals = list(range(len(values)))
            _log_switch_plot(values, x_vals)
    else:
        if x_vals is None:
            x_vals = list(range(len(list_list[0])))
        arr = np.array(list_list)
        vals = np.nanmean(arr, axis=0)
        _log_switch_plot(vals, x_vals)
        if confidence:
            confs = 1.96 * np.nanstd(arr, axis=0) / nb_samples**0.5
            plt.plot(x_vals, vals - confs, linestyle=style, color=color, linewidth=0.3)
            plt.plot(x_vals, vals + confs, linestyle=style, color=color, linewidth=0.3)
        if std:
            stds = np.nanstd(arr, axis=0)
            plt.fill_between(list(x_vals), vals - stds, vals + stds, alpha=0.1, color=color)
    if x_vlines:
        for x in x_vals:
            plt.axvline(x, linewidth=0.3)


def seeds_plot_together(
    all_curves, legends=None, title="", xlog=False, ylog=False, confidence=True, std=False,
    vlines=[], x_vals=None, xlab=None, ylab=None, fontsize=11, xlims=None, ylims=None,
    savepath=None, figsize=(8, 5), show=False, plot_all=False, x_vlines=False, extension="png",
    ):
    """ 
    Plots several lines of several seeds (for each line average and confidence interval)
    Args:
        - all_curves (float list list list) : order 3 array/list of lists of lists
                        one sublist is one line, one subsublist is one seed
        - legends (str list) : labels to use for each line (in order)
        - title (str) : title of the plot
        - xlog (bool) : True for x axis log scale
        - ylog (bool) : True for y axis log scale
        - confidence (bool) : True to display 95% mean estimate confidence intervals
        - std (bool) : True to display standard deviation accross seeds
        - vlines (float list) : list of x coordinates where to add vertical lines
        - x_vals (list) : x axis values, default is 0 to n
        - xlab (str) : label of x axis
        - ylab (str) : label of y axis
        - fontsize (int) : font size
        - xlims (float pair) : plot limits for x axis, None for auto
        - ylims (float pair) : plot limits for y axis, None for auto
        - savepath (str) : path where to save the plot, not saved if None
        - figsize (int pair) : dimensions of the plot
        - show (bool) : True to show the plot
        - plot_all (bool) : True to display one line for each seed instead of average 
        - x_vlines (bool) : True to draw a vertical line at each data point
        - extension (str) : format for the saved image file
    """
    plt.figure(figsize=figsize)
    colors = ["orange", "green", "blue", "red", "purple", "black"] * 10
    styles = ["-", "--", "-.", ":", "-"] * 10
    if legends is None:
        legends = [[]] * len(all_curves)
    for curve, color, style, legend in zip(all_curves, colors, styles, legends):
        seeds_plot(
            curve, color=color, x_vals=x_vals, style=style, legend=legend, 
            xlog=xlog, ylog=ylog, confidence=confidence, std=std, plot_all=plot_all, x_vlines=x_vlines)
    for x in vlines:
        plt.axvline(x)
    plt.xlim(xlims)
    plt.ylim(ylims) 
    if legend is not None:
        plt.legend(prop={'size': fontsize})
    _finalize_plot(title, xlab, ylab, fontsize, savepath, extension, show)


def seeds_plot_color3d(
        all_seeds, x_vals, y_vals, title, xlab, ylab, 
        savepath, show=False, label="", fontsize=11, std=False,
        xlog=False, ylog=False, zlog=False, extension="png",
        **kwargs):
    """ 3d color plot """
    all_seeds = np.array(all_seeds)
    means = np.nanmean(all_seeds, axis=0)
    if zlog:
        plt.pcolor(x_vals, y_vals, means, norm=colors.LogNorm())
    else:
        plt.pcolor(x_vals, y_vals, means)    

    if xlog:
        plt.xscale('log')
    if ylog:
        plt.yscale('log')
    if std:
        stds = np.nanstd(all_seeds, axis=0)
        for y, row in enumerate(stds):
            for x, val in enumerate(row):
                plt.text(x_vals[x], y_vals[y] , 
                         f"+{round(val, 2)}", ha='center', 
                         va='center', color='black')
    plt.colorbar(label=label) 
    _finalize_plot(title, xlab, ylab, fontsize, savepath, extension, show)


def seeds_plot_surface3d(
        all_seeds, x_vals, y_vals, title, xlab, ylab, 
        savepath, show=False, label="", fontsize=11,
        xlog=False, ylog=False, zlog=False, angle=None, extension="png",
        **kwargs):
    """ 3d color plot """
    all_seeds = np.array(all_seeds)
    means = np.nanmean(all_seeds, axis=0)
    ax = plt.axes(projection='3d')
    if angle is not None:
        ax.view_init(*angle)
    x, y = x_vals, y_vals
    y_len, x_len = len(y), len(x)
    x = np.expand_dims(x, axis=1)
    x = np.repeat(x, [y_len], axis=1).transpose()
    y = np.expand_dims(y, axis=0)
    y = np.repeat(y, [x_len], axis=0).transpose()
    # if xlog:
    #     ax.set_xscale('log')
    # if ylog:
    #     ax.set_yscale('log')
    if zlog:
        ax.set_zscale('log')
    ax.plot_surface(x, y, means, cmap='viridis',\
                    edgecolor='green')
    ax.set_zlabel(label, size=fontsize)
    _finalize_plot(title, xlab, ylab, fontsize, savepath, extension, show)
