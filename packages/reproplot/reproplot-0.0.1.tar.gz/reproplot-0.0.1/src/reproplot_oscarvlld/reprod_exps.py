###
 # @file   reprod_exps.py
 # @author Oscar Villemaud <oscar.villemaud@epfl.ch>
 #
 # @section LICENSE
 #
 # Copyright © 2024-2026 École Polytechnique Fédérale de Lausanne (EPFL).
 # All rights reserved.
 #
 # @section DESCRIPTION
 #
 # Experiment running.
###

import os
import time
from tqdm import tqdm
import traceback
import multiprocessing as mp

from .utils import seedall, dump_json, load_json, make_exp_name, make_grid, update_params, scan_runs


def _run_one_run(experiment_func, params, seed, exp_name, run_path, verb):
    """ return 0 if run completed, 1 if failed"""
    if "runs" in verb:
        print(f"running {exp_name} seed {seed}.")
    def _handle_error(exc):
        count = 1
        while os.path.isdir(f"{run_path[:-1]}_failed_{count}"):
            count += 1 
        new_path = f"{run_path[:-1]}_failed_{count}"
        os.rename(run_path, new_path)
        print(f"{exp_name} seed {seed} failed with error: {exc}, renaming to: failed_{count}")
        with open(new_path  + "/" + "traceback.txt", 'w') as f:
            f.write(traceback.format_exc())
    try:
        run_time = time.time()
        seedall(seed)
        metrics = experiment_func(**params)
        if type(metrics) is not dict:
            metrics = {"metric": metrics}
        run_time = time.time() - run_time
        metrics["run_time"] = run_time
        dump_json(metrics, run_path + f"metrics.json")
        if "runs" in verb:
            print(f"{exp_name} seed {seed} saved. ({round(run_time)} secs)")
    except Exception as exc:
        _handle_error(exc)
        return 1
    except KeyboardInterrupt:
        _handle_error("Keyboard Interrupt")
        raise KeyboardInterrupt
    return 0


def run_experiments(
        experiment_func=None, res_dir=None,
        seeds=None, nametag="", params_common=None, diff_plots=None, same_plot=None, same_line=None,
        exp_tags=None, set_depending_params=None, verb=None): 
    """ run an experiment series given a grid of parameters, saves results in json files
    Args:
        - experiment_func (func) : function running a (random) experiment 
                                and outputing a dictionnary of metrics
        - res_dir (str) : name of the directory where to store results as json
        - seeds (int list) : list of random seeds to use for reproducibility
        - nametag (str) : prefix that identifies the series of experiments
        - params_common (dict) : dictionnary of {"param_name": value} 
                                that are de default parameters of experiment_func
        - diff_plots (list dict) : dictionnary of {"param_name": list of values} each value combination on a different plot
        - same_plot (list dict) : dictionnary of {"param_name": list of values} each value combination on a different line of the same plot
        - same_line (list dict) : dictionnary of {"param_name": list of values}, values on the x axis of the plot (only one parameter)
        - exp_tags (str list) : list of parameters to put in experiment names
        - set_depending_params (func) : function editing in-place a dictionnary of parameters
        - verb (str list) : string codes to indicate verbose
    """
    multiprocess = 0
    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    nb_runs_found, nb_runs_total, confs_paths =  scan_runs(
        res_dir=res_dir, dir_path=dir_path,
        seeds=seeds, nametag=nametag, params_common=params_common, 
        diff_plots=diff_plots, same_plot=same_plot, same_line=same_line,
        exp_tags=exp_tags, set_depending_params=set_depending_params)
    nb_runs_needed = nb_runs_total - nb_runs_found
    print(f"Recovered {nb_runs_found}/{nb_runs_total} runs. Running the remaining {nb_runs_needed}.")
    # nb_exps = count_combinations(diff_plots) * count_combinations(same_plot) * count_combinations(same_line) * len(seeds)
    nb_runs_ran = 0
    init_time = time.time()
    # TODO use confs_paths ?
    if multiprocess:
        mp_pool = mp.Pool(processes=multiprocess)
    else:
        nb_failed = 0
    with tqdm(total=nb_runs_needed, leave=True, disable=("pbar" not in verb)) as pbar:
        for params1 in make_grid(diff_plots):
            for params2 in make_grid(same_plot):
                for params3 in make_grid(same_line):
                    params = update_params(params_common, params1, params2, params3)
                    set_depending_params(params)
                    exp_name = make_exp_name(params, nametag, exp_tags)
                    exp_dir = f"{dir_path}/{res_dir}/{exp_name}/"
                    can_run = True
                    try:  # check if parameters are matching
                        loaded_params = load_json(exp_dir + "params.json")
                        if loaded_params != params:
                            print("WARNING : old and new parameters don't match despite same experiment name !")
                            print("found :", loaded_params)
                            print("but has :", params)
                            can_run = False
                    except OSError:
                        os.makedirs(exp_dir)
                        dump_json(params, exp_dir + "params.json", indent=2)
                    if can_run:
                        for seed in seeds:                  
                            run_path = exp_dir + f"seed_{seed}/"
                            if os.path.isdir(run_path):
                                if "runs" in verb:
                                    print(exp_name, "seed", seed, "already exists.")  
                            else:
                                os.makedirs(run_path)
                                if multiprocess:
                                        mp_pool.apply_async(
                                            func=_run_one_run, 
                                            args=(experiment_func, params, seed, exp_name, run_path, verb))
                                else:
                                    failed = _run_one_run(experiment_func, params, seed, exp_name, run_path, verb)
                                    nb_failed += failed
                                    pbar.update()
                                nb_runs_ran += 1
                    else:
                        print("Skipping experiment")
    if multiprocess:
        mp_pool.close()
        mp_pool.join()
    time_taken = time.time() - init_time
    if multiprocess:
        print("Unable to count fails in multiprocess mode")
        print(f"{nb_runs_ran} runs ran and {nb_runs_found} recovered in {round(time_taken)} seconds")
    else:
        print(f"{nb_runs_ran - nb_failed} runs ran, {nb_runs_found} recovered and {nb_failed} failed in {round(time_taken)} seconds")
      