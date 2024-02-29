# BayesValidRox

<div align="center">
  <img src="https://git.iws.uni-stuttgart.de/inversemodeling/bayesian-validation/-/raw/master/docs/logo/bayesvalidrox-logo.png" alt="bayesvalidrox logo"/>
</div>

An open-source, object-oriented Python package for surrogate-assisted Bayesain Validation of computational models.
This framework provides an automated workflow for surrogate-based sensitivity analysis, Bayesian calibration, and validation of computational models with a modular structure.

## Authors
- [@farid](https://git.iws.uni-stuttgart.de/farid)

## Installation
The best practive is to create a virtual environment and install the package inside it.

To create and activate the virtual environment run the following command in the terminal:
```bash
  python3 -m venv bayes_env
  cd bayes_env
  source bin/activate
```
You can replace `bayes_env` with your preferred name. For more information on virtual environments see [this link](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Now, you can install the latest release of the package on PyPI inside the venv with:
```bash
  pip install bayesvalidrox
```
and installing the version on the master branch can be done by cloning this repo and installing:
```bash
  git clone https://git.iws.uni-stuttgart.de/inversemodeling/bayesvalidrox.git
  cd bayesvalidrox
  pip install .
```

## Features
* Surrogate modeling with Polynomial Chaos Expansion
* Global sensitivity analysis using Sobol Indices
* Bayesian calibration with MCMC using `emcee` package
* Bayesian validation with model weights for multi-model setting

## Requirements
* numpy==1.22.1
* pandas==1.2.4
* joblib==1.0.1
* matplotlib==3.4.2
* seaborn==0.11.1
* scikit-learn==0.24.2
* tqdm==4.61.1
* chaospy==4.3.3
* emcee==3.0.2
* corner==2.2.1
* h5py==3.2.1
* statsmodels==0.13.2

## TexLive for Plotting with matplotlib
Here you need super user rights
```bash
sudo apt-get install dvipng texlive-latex-extra texlive-fonts-recommended cm-super
```
