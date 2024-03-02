###
 # @file   utils.py
 # @author Oscar Villemaud <oscar.villemaud@epfl.ch>
 #
 # @section LICENSE
 #
 # Copyright © 2024-2026 École Polytechnique Fédérale de Lausanne (EPFL).
 # All rights reserved.
 #
 # @section DESCRIPTION
 #
 # Utilitary functions.
###

import os
import json
import pickle
import random
from itertools import product

import numpy as np
import torch


def dump_json(object, path, indent=0):
    """ save object in json file 
    Args:
        - object : python object to save
        - path (str) : path where to save the object
        - indent (int) : indent level to use (for readability)
    """
    with open(path, "w") as outfile:
        json.dump(object, outfile, indent=indent)


def load_json(path):
    """ load object from json file 
    Args:
        - path (str) : path where to save the object
    """
    with open(path, 'r') as openfile: 
        return json.load(openfile)
    

def dump_pickle(object, path):
    """ save object in pickle file 
    Args:
        - object : python object to save
        - path (str) : path where to save the object
    """
    with open(path, "wb") as outfile:
        pickle.dump(object, outfile)


def load_pickle(path):
    """ load object from pickle file 
    Args:
        - path (str) : path where to save the object
    """
    with open(path, 'rb') as openfile: 
        return pickle.load(openfile)


def seedall(seed):
    """ seed random, numpy and pytorch with the same seed 
    Args:
        - seed (int) : seed to use
    """
    np.random.seed(seed)
    torch.manual_seed(seed)
    random.seed(seed)


def make_grid(list_dic):
    """ build iterator over different combination of params (gridsearch) 
    Args:
        - list_dic (list dict): dictionnary of {"param_name": list of values}

    Yields:
        - (dict) 
    """
    for params in product(*list_dic.values()):
        yield {key : param for key, param in zip(list_dic.keys(), params)}


def count_combinations(list_dic):
    """ count number of parameter combinations 
    
    Args:
        - list_dic : dictionnary of {"metric": list of values}

    Returns:
        - (int) number of possible parameter combinations
    """
    nb = 1
    for _, params in list_dic.items():
        nb *= len(params)
    return nb


def update_params(params, *updates):
    """ add new parameters or replace existing ones 
    Args:
        - params   : dictionnary of parameters
        - *updates : dictionnaries of additionnal parameters
    Return:
         - (dict) updated dictionnary of parameters
    """
    paramsall = params.copy()
    for new_params in updates:
        paramsall.update(new_params)
    return paramsall


def make_exp_name(params, nametag, tags_list):
    """ create experiment name
    Args:
        - params : dictionnary of {"metric": value}
        - nametag (str) : prefix to identify experiment series
        - tag_list (str list) : list of metrics to put in experiment name

    Returns:
        - (str) experiment name  
    """
    exp_name = nametag
    for name in tags_list:
        exp_name += f"-{name}_{params[name]}"
    return exp_name


def make_plot_name(params, nametag, metric, tags_list):
    """" result should depend on diff_plot 
    Args:
        - params : dictionnary of {"metric": value}
        - nametag (str) : prefix to identify experiment series
        - metric (str) : metric plotted
        - tag_list (str list) : list of param names to put in experiment name

    Returns:
        - (str) plot name  
    """
    plot_name = f"{nametag}-{metric}"
    for name in tags_list:
        plot_name += f"-{name}_{params[name]}"
    return plot_name


def make_title(params, tags_list):
    """
    Args:
        - params : dictionnary of {"metric": value}
        - tag_list (str list) : list of param names to put in experiment name

    Returns:
        - (str) plot title
    """
    if len(tags_list) == 0:
        return "X"
    # title = f"{tags_list[0]}={params[tags_list[0]]}"
    title = ""
    for name in tags_list:
        if len(title):
            title += ", "
        title += f"{name}={params[name]}"
    return title


def make_legend(params, tags_list):
    """ create a legend for a line on a plot 
    from parameters and a list of parameter names 
    Args:
        - params : dictionnary of {"metric": value}
        - tag_list (str list) : list of param names to put in experiment name

    Returns:
        - (str) line legend 
    """
    if len(tags_list) == 0:
        return "X"
    legend = f"{tags_list[0]}={params[tags_list[0]]}"
    for name in tags_list[1:]:
        legend += f", {name}={params[name]}"
    return legend


def check_compatibility(
        diff_plots, same_plot, same_line, exp_tags
        ):
    """ check if the same name if generated twice 
    Args:
        - diff_plots (list dict) : dictionnary of {"param_name": list of values} each value combination on a different plot
        - same_plot (list dict) : dictionnary of {"param_name": list of values} each value combination on a different line of the same plot
        - same_line (list dict) : dictionnary of {"param_name": list of values}, values on the x axis of the plot (only one parameter)
        - exp_tags (str list) : list of parameters to put in experiment names
    """
    for param in list(diff_plots.keys()) + list(same_plot.keys()) + list(same_line.keys()):
        if param not in exp_tags:
            print(f"WARNING : Experiment names should depend on -{param} to avoid having the same name")


def scan_runs(
        res_dir, dir_path=None,
        seeds=None, nametag="", params_common=None, 
        diff_plots=None, same_plot=None, same_line=None,
        exp_tags=None, set_depending_params=lambda x: None):
    """ finds existing and missing runs
    - res_dir (str) : name of the directory where to store results as json
    - dir_path (str) : path to directory containing -res_dir
    - seeds (int list) : list of random seeds to use for reproducibility
    - nametag (str) : prefix that identifies the series of experiments
    - params_common (dict) : dictionnary of {"param_name": value} 
                            that are de default parameters of experiment_func
    - diff_plots (list dict) : dictionnary of {"param_name": list of values} each value combination on a different plot
    - same_plot (list dict) : dictionnary of {"param_name": list of values} each value combination on a different line of the same plot
    - same_line (list dict) : dictionnary of {"param_name": list of values}, values on the x axis of the plot (only one parameter)
    - exp_tags (str list) : list of parameters to put in experiment names
    - set_depending_params (func) : function editing in-place a dictionnary of parameters
    """
    confs_paths = []
    count_done, count_total = 0, 0
    for params1 in make_grid(diff_plots):
        for params2 in make_grid(same_plot):
            for params3 in make_grid(same_line):
                params = update_params(params_common, params1, params2, params3)
                set_depending_params(params)
                exp_name = make_exp_name(params, nametag, exp_tags)
                exp_dir = f"{dir_path}/{res_dir}/{exp_name}/"
                for seed in seeds:
                    path = exp_dir + f"seed_{seed}/"
                    if os.path.isdir(path):
                        count_done += 1
                    else:
                        confs_paths.append((params.copy(), path))
                    count_total += 1
    return count_done, count_total, confs_paths
