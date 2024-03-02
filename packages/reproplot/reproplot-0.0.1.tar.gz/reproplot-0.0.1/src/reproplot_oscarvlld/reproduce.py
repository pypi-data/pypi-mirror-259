###
 # @file   reproduce.py
 # @author Oscar Villemaud <oscar.villemaud@epfl.ch>
 #
 # @section LICENSE
 #
 # Copyright © 2024-2026 École Polytechnique Fédérale de Lausanne (EPFL).
 # All rights reserved.
 #
 # @section DESCRIPTION
 #
 # reproplot main functions to run, plot and manage experiments.
###

import os
import random
from tqdm import tqdm

from .utils import load_json, make_exp_name, check_compatibility
from .reprod_exps import run_experiments
from .reprod_plots import plot_experiments


def rename_exps(
        directory, new_tag, new_exp_tags, old_tag=None):
    """ rename experiment names using parameters saved 
    Args:
        - directory : directory of experiments
        - new_tag (str) : new prefix for experiment names
        - new_exp_tags (str list) : new names of metrics to put in experiment names
        - old_tag (str) : specify to rename only experiments with that tag
    """
    print("Renaming experiments of directory :", directory)
    exp_names_paths = [(f.name, f.path) for f in os.scandir(directory) if f.is_dir()]
    counter = 0
    for exp_name, exp_path in exp_names_paths:
        prefix_cond = True
        if old_tag is not None:
            prefix = exp_name.split("-")[0]
            prefix_cond = prefix == old_tag
        if prefix_cond:
            params = load_json(exp_path + "/params.json")
            exp_name_new = make_exp_name(params, new_tag, tags_list=new_exp_tags)
            os.rename(exp_path, directory + "/" + exp_name_new)
            counter += 1
            print("renaming:", exp_name, "\n into: ", exp_name_new)
    print(f"Renamed {counter} experiments")


def index_exps(directory, nametag=None, param_requirements=None):
    """ gives a summary of available experiments 
    Args:
        - directory : directory of experiments
        - nametag (str) : specify to see only experiments with that tag
        - param_requirements (bool func) : function taking params as input 
                    and outputing True if this experiment should be included
    """
    exp_names_paths = [(f.name, f.path) for f in os.scandir(directory) if f.is_dir()]
    all_params = {}
    seeds = set()
    nb_runs, nb_exps = 0, 0
    for exp_name, exp_path in tqdm(exp_names_paths):
        loaded_params = load_json(exp_path + "/params.json")
        select = True
        if param_requirements is not None:
            select = param_requirements(loaded_params)
        if nametag is not None:
            prefix = exp_name.split("-")[0]
            select = select and (prefix == nametag)
        if select:
            nb_exps += 1
            for name, value in loaded_params.items():  
                if type(value) is list:
                    value = tuple(value)
                if name in all_params:
                    all_params[name].add(value)
                else:
                    all_params[name] = {value}
            for seed_name in [f.name for f in os.scandir(exp_path) if f.is_dir()]:
                if "failed" not in seed_name:
                    seed = int(seed_name[5:])
                    seeds.add(seed)
                    nb_runs += 1
    print(f"found {nb_runs} runs grouped in {nb_exps}/{len(exp_names_paths)} experiments with parameters :")
    def _custom_key(obj):
        if obj is None:
            return 0
        elif type(obj) is int or float:
            return obj
        else:
            return len(obj)
    for name, values in all_params.items():
        print(name, sorted(values, key=_custom_key))
    print("seeds", sorted(seeds))
  

def run_and_plot(
    seeds=None, res_dir="results_RPP", plot_dir="plots_RPP", 
    metrics=["metric"], experiment_func=None,
    nametag="", params_common={}, 
    diff_plots={}, same_plot={}, same_line={},
    exp_tags=None, set_depending_params=lambda x : None, 
    no_run=False, no_plot=False, 
    ignore_missing=False, style3Dplot="colors3d", verb=["pbar"],
    custom_title=None, custom_legend=None, custom_xlab=lambda x:x, custom_ylab=lambda x:x,
  ):  
  """ run and plot experiments by using all hyperparameters in a grid-search fashion 
    Args:
        - res_dir (str) : directory containing the data to plot
        - plot_dir (str) : directory where to save the plot
        - seeds (int list) : seeds of runs to plot
        - metrics ((str | str tuple) list) : list of metrics to plot (batch to put on same plot)
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
        - no_run (bool) : True to disable running new experiments
        - no_plot (bool) : True to disable plotting
        - ignore_missing (bool) : True to plot despite missing data
        - style3Dplot (str) : 'surface3d' or 'colors3d'
        - verb (str list) : string codes to indicate verbose
        - custom_title (func or str) : (optionnal) function that gives a title from parameters
        - custom_legend (func) : (optionnal) function that gives a legend from parameters
        - custom_xlab (func or str) : (optionnal) function that gives x label from x parameter name
        - custom_ylab (func or str) : (optionnal) function that gives y label from y parameter name
  """ 
  if exp_tags is None:
      exp_tags = sorted(list(set(diff_plots.keys()) | set(same_plot.keys()) | set(same_line.keys())))
  if seeds is None:
      seeds = [random.randint(1, 99999)]
      print(f"No seeds specified, using random seed {seeds[0]}")
  check_compatibility(diff_plots, same_plot, same_line, exp_tags)

  if not no_run:
    run_experiments(
        experiment_func=experiment_func, res_dir=res_dir, seeds=seeds, nametag=nametag,
        params_common=params_common, diff_plots=diff_plots, same_plot=same_plot, same_line=same_line,
        exp_tags=exp_tags, set_depending_params=set_depending_params, verb=verb,
    )

  if not no_plot:
    plot_experiments(  
        res_dir=res_dir, plot_dir=plot_dir, seeds=seeds,
        nametag=nametag, metrics=metrics, same_line=same_line,
        params_common=params_common, diff_plots=diff_plots, same_plot=same_plot,
        exp_tags=exp_tags, set_depending_params=set_depending_params,
        ignore_missing=ignore_missing, style3Dplot=style3Dplot,
        custom_title=custom_title, custom_legend=custom_legend,
        custom_xlab=custom_xlab, custom_ylab=custom_ylab,
    )
