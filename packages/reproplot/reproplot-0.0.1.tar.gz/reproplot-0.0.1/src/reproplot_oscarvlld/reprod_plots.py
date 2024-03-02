###
 # @file   reprod_plots.py
 # @author Oscar Villemaud <oscar.villemaud@epfl.ch>
 #
 # @section LICENSE
 #
 # Copyright © 2024-2026 École Polytechnique Fédérale de Lausanne (EPFL).
 # All rights reserved.
 #
 # @section DESCRIPTION
 #
 # Data retrieval for plotting.
###

import os
import copy
from tqdm import tqdm

import numpy as np

from .utils import load_json, make_exp_name, make_grid, make_legend, make_plot_name, update_params, make_title
from .plotting import seeds_plot_together, seeds_plot_color3d, seeds_plot_surface3d


def _extract_line_data(lineconf, res_dir, nametag, exp_tags, ignore_missing):
    """ extracts data from json files and puts it in list of lists 
    Args:
        - lineconf (dict) : dictionnary containing directions to the data to plot on one line
            lineconf1 = {"confs": conf_list, "seeds":[1, 2], "metric": "metric"}
            or
            lineconf1 = {"conf": conf, "seeds":[1, 2], "metric": "metric"}
        - res_dir (str) : directory containing the data to plot
        - nametag (str) : prefix identifying the series of experiments
        - exp_tags (str list) : list of parameters used in experiment names
        - ignore_missing (bool) : True to plot despite missing data

    Returns:
        - (float list list) list of lists of values of the metric, one sublist is one seed 
    """
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    def _handle_missing(ignore_missing, path):
        if ignore_missing:
            print(f"{path} not found, plotting without it.")
        else:
            raise Exception("{} not found, use ignore_missing=True to plot anyway".format(path))
    if "confs" in lineconf:  # if the metric chosen gives one value (eg final loss)
        all_seeds = []
        for seed in lineconf["seeds"]:
            one_seed = []
            for params in lineconf["confs"]:
                exp_name = make_exp_name(params, nametag, exp_tags)
                exp_dir = f"{dir_path}/{res_dir}/{exp_name}/"
                path = exp_dir + f"seed_{seed}/"
                try:
                    value = load_json(path + "metrics.json")[lineconf["metric"]]
                    if type(value) is list:  # implicitely taking value at end of training
                        value = value[-1]
                    one_seed.append(value)
                except OSError:
                    _handle_missing(ignore_missing, path)
                    one_seed.append(np.nan)
            all_seeds.append(one_seed)
    elif "conf" in lineconf:  # if the metric chosen gives a list of values (eg training loss)
        all_seeds = []
        for seed in lineconf["seeds"]:
            params = lineconf["conf"]
            exp_name = make_exp_name(params, nametag, exp_tags)
            exp_dir = f"{dir_path}/{res_dir}/{exp_name}/"
            path = exp_dir + f"seed_{seed}/"
            try:
                one_seed = load_json(path + f"metrics.json")[lineconf["metric"]]
                all_seeds.append(one_seed)
            except OSError:
                _handle_missing(ignore_missing, path)            
    return all_seeds


def _plot_from_conf(
        plot_conf, res_dir, plot_dir, nametag, exp_tags, 
        same_line, metric, ignore_missing, plot_kwargs=None, 
        custom_xlab=None, custom_ylab=None):
    """ creates and saves a plot from a config 
    Args:
        - plot_conf (dict) : configuration of the plot, including instructions on the data to use
                        exp : plot_conf = { "filename" : "plot", "title": "title_foo", 
                                "lines": { "legend1" : lineconf1, "legend2" : lineconf2}}
        - res_dir (str) : directory containing the data to plot
        - plot_dir (str) : directory where to save the plot
        - nametag (str) : prefix identifying the series of experiments
        - exp_tags (str list) : list of parameters used in experiment names
        - same_line (list dict or empty dict) : {"param_name": list of values} values on x axis,
                                       empty dict will use training steps as x axis
        - metric (str) : name of the metric to plot
        - ignore_missing (bool) : True to plot despite missing data
        - plot_kwargs (dict) : dictionnary of parameters to forward to seeds_plot_together()
        - custom_xlab (func) : function that gives x label from x parameter name
        - custom_ylab (func) : function that gives y label from y parameter name
    """
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    os.makedirs(f"{dir_path}/{plot_dir}/", exist_ok=True)
    path = f"{dir_path}/{plot_dir}/{plot_conf['filename']}"
    if plot_conf["type"] == "lines2d":  # 2D line plot
        all_lines = []
        all_legends = []
        for legend, lineconf in tqdm(plot_conf["lines"].items(), desc=f"Plotting {plot_conf['filename']}"):
            all_lines.append(_extract_line_data(lineconf, res_dir, nametag, exp_tags, ignore_missing))
            all_legends.append(legend) 
        if len(same_line) == 0: # implicit values for x axis
            xlab, xvals = "steps", None
        else:  # explicit values for x axis
            xlab, xvals = list(same_line.items())[0]
        seeds_plot_together(
            all_lines, all_legends, title=plot_conf["title"], savepath=path, 
            ylab=custom_ylab(metric), xlab=custom_xlab(xlab), x_vals=xvals, **plot_kwargs
            )
    elif plot_conf["type"] in ["colors3d", "surface3d"]:  # 3D plots
        all_rows = []
        xlab, xvals = list(same_line.items())[0]
        ylab, yvals = list(same_line.items())[1]
        for lineconf in tqdm(plot_conf["rows"], desc=f"Plotting {plot_conf['filename']}"):
            all_rows.append(_extract_line_data(lineconf, res_dir, nametag, exp_tags, ignore_missing))
        all_seeds = np.transpose(np.array(all_rows), (1, 0, 2))
        plot_funcs = {"colors3d": seeds_plot_color3d, "surface3d": seeds_plot_surface3d}
        plot_funcs[plot_conf["type"]](
                all_seeds, x_vals=xvals, y_vals=yvals, label=metric,
                title=plot_conf["title"], xlab=custom_xlab(xlab), ylab=custom_ylab(ylab), 
                savepath=path, std=False, **plot_kwargs)

#  plot_conf = { "filename" : "plot", "title": "title_foo", "type":"3d",
#                               "rows": [lineconf1, lineconf2]}
def plot_experiments(
        res_dir=None, plot_dir=None, metrics=None,
        seeds=None, nametag="", params_common=None, 
        diff_plots=None, same_plot=None, same_line=None, set_depending_params=None,
        exp_tags=None, ignore_missing=None, style3Dplot=None,
        custom_title=None, custom_legend=None,
        custom_xlab=None, custom_ylab=None,
    ):
    """ Plot a series of experiments
    Args:
        - res_dir (str) : directory containing the data to plot
        - plot_dir (str) : directory where to save the plot
        - metrics ((str | str tuple) list) : list of metrics to plot (batch to put on same plot)
        - seeds (int list) : seeds of runs to plot
        - nametag (str) : prefix identifying the series of experiments
        - exp_tags (str list) : list of parameters used in experiment names
        - same_line (list dict or empty dict) : {"param_name": list of values} values on x axis,
                                       empty dict will use training steps as x axis
        - params_common (dict) : dictionnary of {"param_name": value} 
                                that are de default parameters of experiment_func
        - diff_plots (list dict) : dictionnary of {"param_name": list of values} each value combination on a different plot
        - same_plot (list dict) : dictionnary of {"param_name": list of values} each value combination on a different line of the same plot
        - same_line (list dict) : dictionnary of {"param_name": list of values}, values on the x axis of the plot (only one parameter)
        - set_depending_params (func) : function editing in-place a dictionnary of parameters
        - exp_tags (str list) : list of parameters to put in experiment names
        - ignore_missing (bool) : True to plot despite missing data
        - style3Dplot (str) : 'surface3d' or 'colors3d'
        - custom_title (func or str) : (optionnal) function that gives a title from parameters
        - custom_legend (func) : (optionnal) function that gives a legend from parameters
        - custom_xlab (func or str) : function that gives x label from x parameter name
        - custom_ylab (func or str) : function that gives y label from y parameter name
    """
    # handling constant functions
    if type(custom_title) is str:
        _title = custom_title
        custom_title = lambda x, y : _title
    if type(custom_xlab) is str:
        _xlab = custom_xlab
        custom_xlab = lambda x : _xlab 
    if type(custom_ylab) is str:
        _ylab = custom_ylab
        custom_ylab = lambda x : _ylab 
    # infering plot type
    if len(same_line) < 2:
        plot_type = "lines2d"
    else:
        plot_type = style3Dplot
    # searching for config options
    if os.path.exists("plot_config.json"):
        plot_params = load_json("plot_config.json")[plot_type]
    else:
        print("plot_config.json not found, plotting without config")
        plot_params = {"_overwrite":{}}
    plot_tags = list(diff_plots.keys())
    legend_tags = list(same_plot.keys())
    # creating plot configs and plotting
    for metrics_plot in metrics:
        if type(metrics_plot) is str:  # if only one metric on the plot
            metrics_plot = [metrics_plot]
        for params1 in make_grid(diff_plots):
            if custom_title is None:
                title = make_title(params1, plot_tags)
            else:
                title = custom_title(params1, metrics_plot)
            plot_conf = {
                "title": title, 
                "filename": make_plot_name(params1, nametag, metrics_plot[0], plot_tags)}
            if plot_type == "lines2d":  # if 2D line plot
                plot_conf["lines"] = {}
                for params2 in make_grid(same_plot):
                    if len(metrics_plot) > 1:
                        prefix = metric + ", "
                    else:
                        prefix = ""   
                    for metric in metrics_plot:  
                        def _pick_legend(params):
                            if custom_legend is None:
                                return prefix + make_legend(params, legend_tags)
                            return custom_legend(params, metric)
                        if same_line == {}:
                            params = update_params(params_common, params1, params2)
                            set_depending_params(params)
                            plot_conf["lines"][_pick_legend(params)] = {
                                "seeds": seeds, "metric": copy.deepcopy(metric), "conf": params
                                }
                        else:
                            params_list = []
                            for params3 in make_grid(same_line):
                                params = update_params(params_common, params1, params2, params3)
                                set_depending_params(params)
                                params_list.append(params)
                            plot_conf["lines"][_pick_legend(params)] = {
                                "seeds": seeds, "metric": copy.deepcopy(metric), "confs": params_list, 
                                }
            elif plot_type in ["colors3d", "surface3d"]:  # if 3d plot
                for metric in metrics_plot:
                    plot_conf["rows"] = []
                    x_param, x_values = list(same_line.items())[0]
                    y_param, y_values = list(same_line.items())[1]
                    for y_value in y_values:
                        params_list = []
                        for x_value in x_values:
                            params = update_params(params_common, params1, {x_param: x_value, y_param: y_value})
                            set_depending_params(params)
                            params_list.append(params)
                        lineconf = {"seeds": seeds, "metric": copy.deepcopy(metric), "confs": params_list, 
                                    }
                        plot_conf["rows"].append(lineconf)
            plot_conf["type"] = plot_type
            if plot_params is not None:
                plot_kwargs = update_params(plot_params.get(metric, {}), plot_params["_overwrite"])
            _plot_from_conf(
                plot_conf, res_dir, plot_dir, 
                nametag, exp_tags, 
                same_line, metric, ignore_missing, plot_kwargs, 
                custom_xlab, custom_ylab
                )
# lineconf = {"confs": conf_list, "seeds":[1, 2], "metric": "metric"}
