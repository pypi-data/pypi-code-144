import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
import matplotlib.pyplot as plt
import seaborn as sns
import pyro.distributions as dist
import run
import svi
import pybasilica

'''
pip uninstall pybasilica
python setup.py sdist
twine upload --repository testpypi dist/pybasilica-0.0.60.tar.gz | for test pypi
twine upload dist/*                                              | for main pypi
pip install -i https://test.pypi.org/simple/ pybasilica==0.0.60  | for test pypi
pip install pybasilica==0.1.3                                    | for main pypi
'''


M = pd.read_csv("/home/azad/Documents/thesis/pybasilica/pybasilica/data/real/data_sigphylo.csv")
cosmic_df = pd.read_csv("/home/azad/Documents/thesis/pybasilica/pybasilica/data/cosmic/cosmic_catalogue.csv", index_col=0)
B_input = pd.read_csv("/home/azad/Documents/thesis/pybasilica/pybasilica/data/real/beta_aging.csv", index_col=0)
groups = [0,0,1,2,1]
k_list = [0,1,2]
lr = 0.05
steps_per_iter = 500


no_converge = [0,1,10,11,16,22,36,60,80,90,110,218,280,400]
yes_converge = [0,1,1,11,16,12,13,5,8,10,11,8,9,14]

#print(no_converge[-10:])
#print(svi.convergence(x=yes_converge, alpha=0.05))

obj = pybasilica.fit(
    x=M, 
    k_list=k_list, 
    lr=0.05, 
    n_steps=100, 
    groups=None, 
    beta_fixed=B_input, 
    compile_model = False, 
    CUDA = False, 
    enforce_sparsity=False, 
    verbose=False
    )

print("alpha:\n", obj.alpha)
print("beta_fixed:\n", obj.beta_fixed)
print("beta_denovo:\n", obj.beta_denovo)
print("BIC:\n", obj.bic)

'''
obj = svi.PyBasilica(
    x=M,
    k_denovo=2,
    lr=0.05,
    n_steps=100,
    groups=None,
    beta_fixed=B_input,
    compile_model=False,
    CUDA=False,
    enforce_sparsity=False
)

obj = run.single_run(x=M, k_denovo=1, lr=0.05, n_steps=500, groups=None, beta_fixed=B_input, compile_model = False, CUDA = False, enforce_sparsity = False)

#print("likelihood:", obj.likelihood)
#print("regularization:", obj.regularization)

print("x:\n", obj.x)
print("lr:", obj.lr)
print("n_steps:", obj.n_steps)
print("n_samples:", obj.n_samples)
print("k_fixed:", obj.k_fixed)
print("k_denovo:", obj.k_denovo)
print("groups:", obj.groups)
'''
