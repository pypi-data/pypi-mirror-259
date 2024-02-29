# -*- coding: utf-8 -*-
"""
Tests the class Engine in bayesvalidrox
Tests are available for the following functions:
    hellinger_distance   - x
    logpdf               - x
    subdomain            - x
Engine:
    start_engine         - x
    train_normal
    train_sequential
    eval_metamodel
    train_seq_design
    util_VarBasedDesign
    util_BayesianActiveDesign
    util_BayesianDesign
    run_util_func
    dual_annealing
    tradoff_weights      - x
    choose_next_sample
        plotter
    util_AlphOptDesign
    _normpdf            - x    Also move outside the class?
    _corr_factor_BME           Not used again in this class
    _posteriorPlot      - x
    _BME_Calculator     - x
    _validError         - x
    _error_Mean_Std     - x 

"""
import math
import numpy as np
import pandas as pd

import sys
sys.path.append("src/")
#import pytest

from bayesvalidrox.surrogate_models.inputs import Input
from bayesvalidrox.surrogate_models.exp_designs import ExpDesigns
from bayesvalidrox.surrogate_models.surrogate_models import MetaModel
from bayesvalidrox.pylink.pylink import PyLinkForwardModel as PL
from bayesvalidrox.surrogate_models.engine import Engine
from bayesvalidrox.surrogate_models.engine import hellinger_distance, logpdf, subdomain


#%% Test Engine constructor


def test_engine() -> None:
    """
    Build Engine without inputs
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mod = PL()
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    Engine(mm, mod, expdes)

#%% Test Engine.start_engine

def test_start_engine() -> None:
    """
    Build Engine without inputs
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mod = PL()
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    engine = Engine(mm, mod, expdes)
    engine.start_engine()


#%% Test Engine.train_normal
# TODO: build mock model to do this? - test again in full-length examples

#%% Test Engine._error_Mean_Std

def test__error_Mean_Std() -> None:
    """
    Compare moments of surrogate and reference
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    mm.fit([[0.0],[1.0]], {'Z':[[0.5],[0.5]]})
    expdes = ExpDesigns(inp)
    mod = PL()
    mod.mc_reference['mean'] = [0.5]
    mod.mc_reference['std'] = [0.0]
    mod.Output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    mean, std = engine._error_Mean_Std()
    assert mean < 0.01 and std <0.01
    
#%% Test Engine._validError

def test__validError() -> None:
    """
    Calculate validation error
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    mm.fit([[0.0],[1.0]], {'Z':[[0.5],[0.5]]})
    expdes = ExpDesigns(inp)
    mod = PL()
    expdes.valid_samples = [[0.5]]
    expdes.valid_model_runs = {'Z':[[0.5]]}
    mod.Output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    mean, std = engine._validError()
    assert mean['Z'][0] < 0.01 #and std['Z'][0] <0.01
    
#%% Test Engine._BME_Calculator

def test__BME_Calculator() -> None:
    """
    Calculate BME
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    mm.fit([[0.0],[0.5],[1.0]], {'Z':[[0.5],[0.4],[0.5]]})
    expdes = ExpDesigns(inp)
    expdes.generate_ED(2,transform=True,max_pce_deg=1)
    mod = PL()
    mod.Output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    obs_data = {'Z':np.array([0.45])}
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    engine._BME_Calculator(obs_data, sigma2Dict)
    # Note: if error appears here it might also be due to inoptimal choice of training samples

def test__BME_Calculator_rmse() -> None:
    """
    Calculate BME with given RMSE
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    mm.fit([[0.0],[0.5],[1.0]], {'Z':[[0.5],[0.4],[0.5]]})
    expdes = ExpDesigns(inp)
    expdes.generate_ED(2,transform=True,max_pce_deg=1)
    mod = PL()
    mod.Output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    obs_data = {'Z':np.array([0.45])}
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    engine._BME_Calculator(obs_data, sigma2Dict, rmse = {'Z':0.1})
    # Note: if error appears here it might also be due to inoptimal choice of training samples

def test__BME_Calculator_lik() -> None:
    """
    Calculate BME with given validation likelihood and post-snapshot
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    mm.fit([[0.0],[0.5],[1.0]], {'Z':[[0.5],[0.4],[0.5]]})
    expdes = ExpDesigns(inp)
    expdes.generate_ED(2,transform=True,max_pce_deg=1)
    mod = PL()
    mod.Output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    obs_data = {'Z':np.array([0.45])}
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    expdes.post_snapshot = True
    
    engine.valid_likelihoods = [0.1]
    engine._BME_Calculator(obs_data, sigma2Dict)
    

def test__BME_Calculator_2d() -> None:
    """
    Calculate BME with given validation likelihood and post-snapshot, 2d input
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    inp.add_marginals()
    inp.Marginals[1].dist_type = 'normal'
    inp.Marginals[1].parameters = [0,1]
    mm = MetaModel(inp)
    mm.fit([[0.0,0.0],[0.5,0.1],[1.0,0.9]], {'Z':[[0.5],[0.4],[0.5]]})
    expdes = ExpDesigns(inp)
    expdes.generate_ED(2,transform=True,max_pce_deg=1)
    mod = PL()
    mod.n_obs = 1
    mod.Output.names = ['Z']
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    obs_data = {'Z':np.array([0.45])}
    m_observations = obs_data
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    expdes.post_snapshot = True
    
    engine.valid_likelihoods = [0.1]
    engine._BME_Calculator(obs_data, sigma2Dict)
    
#%% Test hellinger_distance

def test_hellinger_distance_isnan() -> None:
    """
    Calculate Hellinger distance-nan
    """
    P = [0]
    Q = [1]
    math.isnan(hellinger_distance(P,Q))
    
def test_hellinger_distance_0() -> None:
    """
    Calculate Hellinger distance-0
    """
    P = [0,1,2]
    Q = [1,0,2]
    assert hellinger_distance(P,Q) == 0.0
    
def test_hellinger_distance_1() -> None:
    """
    Calculate Hellinger distance-1
    """
    P = [0,1,2]
    Q = [0,0,0]
    assert hellinger_distance(P,Q) == 1.0
    
#%% Test Engine._normpdf
   
def test__normpdf() -> None:
    """
    Likelihoods based on gaussian dist
    """
    
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    mod = PL()
    mod.Output.names = ['Z']
    
    y_hat_pce =  {'Z':np.array([[0.12]])}
    std_pce = {'Z':np.array([[0.05]])}
    obs_data = {'Z':np.array([0.1])}
    sigma2Dict = {'Z':np.array([0.05])}
    total_sigma2s = pd.DataFrame(sigma2Dict, columns = ['Z'])
    
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    engine._normpdf(y_hat_pce, std_pce, obs_data, total_sigma2s)
      
def test__normpdf_rmse() -> None:
    """
    Likelihoods based on gaussian dist with rmse
    """
    
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    mod = PL()
    mod.Output.names = ['Z']
    
    y_hat_pce =  {'Z':np.array([[0.12]])}
    std_pce = {'Z':np.array([[0.05]])}
    obs_data = {'Z':np.array([0.1])}
    sigma2Dict = {'Z':np.array([0.05])}
    total_sigma2s = pd.DataFrame(sigma2Dict, columns = ['Z'])
    
    engine = Engine(mm, mod, expdes)
    engine.start_engine()
    engine._normpdf(y_hat_pce, std_pce, obs_data, total_sigma2s, rmse = {'Z':0.1})
    
    
#%% Test Engine._posteriorPlot

def test__posteriorPlot() -> None:
    """
    Plot posterior
    """    
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    expdes.generate_ED(2,transform=True,max_pce_deg=1)
    mod = PL()
    posterior = np.array([[0],[0.1],[0.2]])
    engine = Engine(mm, mod, expdes)
    engine._posteriorPlot(posterior, ['i'], 'Z')
    
def test__posteriorPlot_2d() -> None:
    """
    Plot posterior for 2 params
    """    
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    inp.add_marginals()
    inp.Marginals[1].dist_type = 'normal'
    inp.Marginals[1].parameters = [0,1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    expdes.generate_ED(2,transform=True,max_pce_deg=1)
    mod = PL()
    posterior = np.array([[0,0],[0.1,1.0],[0.2,0.5]])
    engine = Engine(mm, mod, expdes)
    engine._posteriorPlot(posterior, ['i', 'j'], 'Z')
    
#%% Test logpdf

def test_logpdf() -> None:
    """
    Calculate log-pdf
    """
    logpdf(np.array([0.1]), np.array([0.2]), np.array([0.1]))
    
#%% Test Engine._corr_factor_BME
# TODO: not used again here?

#%% Test subdomain

def test_subdomain() -> None:
    """
    Create subdomains from bounds
    """
    subdomain([(0,1),(0,1)], 2)


#%% Test Engine.tradeoff_weights

def test_tradeoff_weights_None() -> None:
    """
    Tradeoff weights with no scheme
    """  
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    mod = PL()
    engine = Engine(mm, mod, expdes)
    weights = engine.tradeoff_weights(None, [[0],[1]], {'Z':[[0.4],[0.5]]})
    assert weights[0] == 0 and weights[1] == 1
    
def test_tradeoff_weights_equal() -> None:
    """
    Tradeoff weights with 'equal' scheme
    """  
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    mod = PL()
    engine = Engine(mm, mod, expdes)
    weights = engine.tradeoff_weights('equal', [[0],[1]], {'Z':[[0.4],[0.5]]})
    assert weights[0] == 0.5 and weights[1] == 0.5
    
def test_tradeoff_weights_epsdecr() -> None:
    """
    Tradeoff weights with 'epsilon-decreasing' scheme
    """  
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 3
    expdes.X = np.array([[0],[1]])
    mod = PL()
    engine = Engine(mm, mod, expdes)
    weights = engine.tradeoff_weights('epsilon-decreasing', expdes.X, {'Z':[[0.4],[0.5]]})
    assert weights[0] == 1.0 and weights[1] == 0.0
    
def test_tradeoff_weights_adaptive() -> None:
    """
    Tradeoff weights with 'adaptive' scheme
    """  
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    mm = MetaModel(inp)
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 3
    expdes.X = np.array([[0],[1]])
    mod = PL()
    engine = Engine(mm, mod, expdes)
    weights = engine.tradeoff_weights('adaptive', expdes.X, {'Z':[[0.4],[0.5]]})
    assert weights[0] == 0.5 and weights[1] == 0.5
    
def test_tradeoff_weights_adaptiveit1() -> None:
    """
    Tradeoff weights with 'adaptive' scheme for later iteration (not the first)
    """  
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine._y_hat_prev, _ = mm.eval_metamodel(samples=np.array([[0.1],[0.2],[0.6]]))
    engine.tradeoff_weights('adaptive', expdes.X, expdes.Y)
    
#%% Test Engine.choose_next_sample

def test_choose_next_sample() -> None:
    """
    Chooses new sample using all standard settings (exploration, random, space-filling,...)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='random'
    expdes.exploit_method='Space-filling'
    expdes.util_func='Space-filling'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample()
    assert x.shape[0]==1 and x.shape[1] == 1
    
def test_choose_next_sample_da_spaceparallel() -> None:
    """
    Chooses new sample using dual-annealing and space-filling, parallel=True
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='dual-annealing'
    expdes.exploit_method='Space-filling'
    expdes.util_func='Space-filling'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.parallel = True
    x, nan = engine.choose_next_sample()
    assert x.shape[0]==1 and x.shape[1] == 1
       
def test_choose_next_sample_da_spacenoparallel() -> None:
    """
    Chooses new sample using dual-annealing and space-filling, parallel = False
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='dual-annealing'
    expdes.exploit_method='Space-filling'
    expdes.util_func='Space-filling'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.parallel = False
    x, nan = engine.choose_next_sample()
    assert x.shape[0]==1 and x.shape[1] == 1
    
def test_choose_next_sample_loo_space() -> None:
    """
    Chooses new sample using all LOO-CV and space-filling
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='LOO-CV'
    expdes.exploit_method='Space-filling'
    expdes.util_func='Space-filling'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample()
    assert x.shape[0]==1 and x.shape[1] == 1
    
def test_choose_next_sample_vor_space() -> None:
    """
    Chooses new sample using voronoi, space-filling
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='voronoi'
    expdes.exploit_method='Space-filling'
    expdes.util_func='Space-filling'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample()
    assert x.shape[0]==1 and x.shape[1] == 1
    
def test_choose_next_sample_latin_space() -> None:
    """
    Chooses new sample using all latin-hypercube, space-filling
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='Space-filling'
    expdes.util_func='Space-filling'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample()
    assert x.shape[0]==1 and x.shape[1] == 1
     
def test_choose_next_sample_latin_alphD() -> None:
    """
    Chooses new sample using all latin-hypercube, alphabetic (D)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='alphabetic'
    expdes.util_func='D-Opt'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample(var = expdes.util_func)
    assert x.shape[0]==1 and x.shape[1] == 1
     
def test_choose_next_sample_latin_alphK() -> None:
    """
    Chooses new sample using all latin-hypercube, alphabetic (K)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='alphabetic'
    expdes.util_func='K-Opt'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample(var = expdes.util_func)
    assert x.shape[0]==1 and x.shape[1] == 1
    
def test_choose_next_sample_latin_alphA() -> None:
    """
    Chooses new sample using all latin-hypercube, alphabetic (A)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='alphabetic'
    expdes.util_func='A-Opt'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample(var = expdes.util_func)
    assert x.shape[0]==1 and x.shape[1] == 1
     
def test_choose_next_sample_latin_VarALM() -> None:
    """
    Chooses new sample using all latin-hypercube, VarDesign (ALM)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='VarOptDesign'
    expdes.util_func='ALM'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample(var = expdes.util_func)
    assert x.shape[0]==1 and x.shape[1] == 1
     
def test_choose_next_sample_latin_VarEIGF() -> None:
    """
    Chooses new sample using all latin-hypercube, VarDesign (EIGF)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='VarOptDesign'
    expdes.util_func='EIGF'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample(var = expdes.util_func)
    assert x.shape[0]==1 and x.shape[1] == 1

def test_choose_next_sample_latin_VarLOO() -> None:
    """
    Chooses new sample using all latin-hypercube, VarDesign (LOOCV)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='VarOptDesign'
    expdes.util_func='LOOCV'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    x, nan = engine.choose_next_sample(var = expdes.util_func)
    assert x.shape[0]==1 and x.shape[1] == 1
    
def test_choose_next_sample_latin_BODMI() -> None:
    """
    Chooses new sample using all latin-hypercube, BayesOptDesign (MI)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='BayesOptDesign'
    expdes.util_func='MI'
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.observations = {'Z':np.array([0.45])}
    #engine.choose_next_sample(sigma2=None, n_candidates=5, var='DKL')
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    x, nan = engine.choose_next_sample(sigma2=sigma2Dict, var = expdes.util_func)
      
def test_choose_next_sample_latin_BODALC() -> None:
    """
    Chooses new sample using all latin-hypercube, BayesOptDesign (ALC)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='BayesOptDesign'
    expdes.util_func='ALC'
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.observations = {'Z':np.array([0.45])}
    #engine.choose_next_sample(sigma2=None, n_candidates=5, var='DKL')
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    x, nan = engine.choose_next_sample(sigma2=sigma2Dict, var = expdes.util_func)
   
def test_choose_next_sample_latin_BODDKL() -> None:
    """
    Chooses new sample using all latin-hypercube, BayesOptDesign (DKL)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='BayesOptDesign'
    expdes.util_func='DKL'
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.observations = {'Z':np.array([0.45])}
    #engine.choose_next_sample(sigma2=None, n_candidates=5, var='DKL')
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    x, nan = engine.choose_next_sample(sigma2=sigma2Dict, var = expdes.util_func)

   
def test_choose_next_sample_latin_BODDPP() -> None:
    """
    Chooses new sample using all latin-hypercube, BayesOptDesign (DPP)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='BayesOptDesign'
    expdes.util_func='DPP'
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.observations = {'Z':np.array([0.45])}
    #engine.choose_next_sample(sigma2=None, n_candidates=5, var='DKL')
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    x, nan = engine.choose_next_sample(sigma2=sigma2Dict, var = expdes.util_func)

   
def test_choose_next_sample_latin_BODAPP() -> None:
    """
    Chooses new sample using all latin-hypercube, BayesOptDesign (APP)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='BayesOptDesign'
    expdes.util_func='APP'
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.observations = {'Z':np.array([0.45])}
    #engine.choose_next_sample(sigma2=None, n_candidates=5, var='DKL')
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    x, nan = engine.choose_next_sample(sigma2=sigma2Dict, var = expdes.util_func)

   
def test_choose_next_sample_latin_BODMI() -> None:
    """
    Chooses new sample using all latin-hypercube, BayesOptDesign (MI)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='BayesOptDesign'
    expdes.util_func='MI'
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.observations = {'Z':np.array([0.45])}
    #engine.choose_next_sample(sigma2=None, n_candidates=5, var='DKL')
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    x, nan = engine.choose_next_sample(sigma2=sigma2Dict, var = expdes.util_func)

   
def test_choose_next_sample_latin_BADBME() -> None:
    """
    Chooses new sample using all latin-hypercube, BayesActDesign (BME)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='BayesActDesign'
    expdes.util_func='BME'
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.observations = {'Z':np.array([0.45])}
    #engine.choose_next_sample(sigma2=None, n_candidates=5, var='DKL')
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    engine.n_obs = 1
    x, nan = engine.choose_next_sample(sigma2=sigma2Dict, var = expdes.util_func)

def test_choose_next_sample_latin_BADDKL() -> None:
    """
    Chooses new sample using all latin-hypercube, BayesActDesign (DKL)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='BayesActDesign'
    expdes.util_func='DKL'
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.observations = {'Z':np.array([0.45])}
    #engine.choose_next_sample(sigma2=None, n_candidates=5, var='DKL')
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    engine.n_obs = 1
    x, nan = engine.choose_next_sample(sigma2=sigma2Dict, var = expdes.util_func)


def test_choose_next_sample_latin_BADinfEntropy() -> None:
    """
    Chooses new sample using all latin-hypercube, BayesActDesign (infEntropy)
    """
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.tradeoff_scheme = 'equal'
    expdes.explore_method='latin-hypercube'
    expdes.exploit_method='BayesActDesign'
    expdes.util_func='infEntropy'
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.observations = {'Z':np.array([0.45])}
    #engine.choose_next_sample(sigma2=None, n_candidates=5, var='DKL')
    sigma2Dict = {'Z':np.array([0.05])}
    sigma2Dict = pd.DataFrame(sigma2Dict, columns = ['Z'])
    engine.n_obs = 1
    x, nan = engine.choose_next_sample(sigma2=sigma2Dict, var = expdes.util_func)

    
if __name__ == '__main__':
    inp = Input()
    inp.add_marginals()
    inp.Marginals[0].dist_type = 'normal'
    inp.Marginals[0].parameters = [0,1]
    expdes = ExpDesigns(inp)
    expdes.n_init_samples = 2
    expdes.n_max_samples = 4
    expdes.X = np.array([[0],[1],[0.5]])
    expdes.Y = {'Z':[[0.4],[0.5],[0.45]]}
    expdes.explore_method='dual-annealing'
    expdes.exploit_method='Space-filling'
    expdes.util_func='Space-filling'
    
    mm = MetaModel(inp)
    mm.fit(expdes.X, expdes.Y)
    expdes.generate_ED(expdes.n_init_samples, transform=True, max_pce_deg=np.max(mm.pce_deg))
    mod = PL()
    engine = Engine(mm, mod, expdes)
    engine.out_names = ['Z']
    engine.parallel = True
    x, nan = engine.choose_next_sample()
    assert x.shape[0]==1 and x.shape[1] == 1
    
    None