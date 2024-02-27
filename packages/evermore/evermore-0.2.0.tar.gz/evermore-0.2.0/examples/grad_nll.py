from __future__ import annotations

import equinox as eqx
from jax import config
from model import init_values, model, observation, optimizer

import evermore as evm

config.update("jax_enable_x64", True)

# create negative log likelihood
nll = evm.likelihood.NLL(model=model, observation=observation)

# fit
params, state = optimizer.fit(fun=nll, init_values=init_values)

# gradients of nll of fitted model
fast_grad_nll = eqx.filter_jit(eqx.filter_grad(nll))
grads = fast_grad_nll(params)
# gradients of nll of fitted model only wrt to `mu`
# basically: pass the parameters dict of which you want the gradients
params_ = {k: v for k, v in params.items() if k == "mu"}
grad_mu = fast_grad_nll(params_)

# hessian + cov_matrix of nll of fitted model
hessian = eqx.filter_jit(evm.likelihood.Hessian(model=model, observation=observation))()

# covariance matrix of fitted model
covmatrix = eqx.filter_jit(
    evm.likelihood.CovMatrix(model=model, observation=observation)
)()
