"""Generated from gga_k_apbeint.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = 3 ** (0.1e1 / 0.3e1)
  t3 = t2 ** 2
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t6 = t3 * t4 * jnp.pi
  t7 = r0 + r1
  t8 = 0.1e1 / t7
  t11 = 0.2e1 * r0 * t8 <= p.zeta_threshold
  t12 = p.zeta_threshold - 0.1e1
  t15 = 0.2e1 * r1 * t8 <= p.zeta_threshold
  t16 = -t12
  t18 = (r0 - r1) * t8
  t19 = jnp.where(t15, t16, t18)
  t20 = jnp.where(t11, t12, t19)
  t21 = 0.1e1 + t20
  t23 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t25 = t24 * p.zeta_threshold
  t26 = t21 ** (0.1e1 / 0.3e1)
  t27 = t26 ** 2
  t29 = jnp.where(t21 <= p.zeta_threshold, t25, t27 * t21)
  t30 = t7 ** (0.1e1 / 0.3e1)
  t31 = t30 ** 2
  t35 = 6 ** (0.1e1 / 0.3e1)
  t36 = (params.muPBE - params.muGE) * params.alpha * t35
  t37 = jnp.pi ** 2
  t38 = t37 ** (0.1e1 / 0.3e1)
  t39 = t38 ** 2
  t40 = 0.1e1 / t39
  t41 = t40 * s0
  t42 = r0 ** 2
  t43 = r0 ** (0.1e1 / 0.3e1)
  t44 = t43 ** 2
  t46 = 0.1e1 / t44 / t42
  t47 = params.alpha * t35
  t48 = t41 * t46
  t70 = jnp.where(r0 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t29 * t31 * (0.1e1 + params.kappa * (0.1e1 - params.kappa / (params.kappa + (params.muGE + t36 * t41 * t46 / (0.1e1 + t47 * t48 / 0.24e2) / 0.24e2) * t35 * t48 / 0.24e2))))
  t72 = jnp.where(t11, t16, -t18)
  t73 = jnp.where(t15, t12, t72)
  t74 = 0.1e1 + t73
  t76 = t74 ** (0.1e1 / 0.3e1)
  t77 = t76 ** 2
  t79 = jnp.where(t74 <= p.zeta_threshold, t25, t77 * t74)
  t81 = t40 * s2
  t82 = r1 ** 2
  t83 = r1 ** (0.1e1 / 0.3e1)
  t84 = t83 ** 2
  t86 = 0.1e1 / t84 / t82
  t87 = t81 * t86
  t109 = jnp.where(r1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t79 * t31 * (0.1e1 + params.kappa * (0.1e1 - params.kappa / (params.kappa + (params.muGE + t36 * t81 * t86 / (0.1e1 + t47 * t87 / 0.24e2) / 0.24e2) * t35 * t87 / 0.24e2))))
  res = t70 + t109
  return res

def unpol(r0, s0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = t3 ** 2
  t5 = jnp.pi ** (0.1e1 / 0.3e1)
  t8 = 0.1e1 <= p.zeta_threshold
  t9 = p.zeta_threshold - 0.1e1
  t11 = jnp.where(t8, -t9, 0)
  t12 = jnp.where(t8, t9, t11)
  t13 = 0.1e1 + t12
  t15 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t16 = t15 ** 2
  t18 = t13 ** (0.1e1 / 0.3e1)
  t19 = t18 ** 2
  t21 = jnp.where(t13 <= p.zeta_threshold, t16 * p.zeta_threshold, t19 * t13)
  t22 = r0 ** (0.1e1 / 0.3e1)
  t23 = t22 ** 2
  t27 = 6 ** (0.1e1 / 0.3e1)
  t28 = jnp.pi ** 2
  t29 = t28 ** (0.1e1 / 0.3e1)
  t30 = t29 ** 2
  t31 = 0.1e1 / t30
  t34 = 2 ** (0.1e1 / 0.3e1)
  t35 = t34 ** 2
  t36 = s0 * t35
  t37 = r0 ** 2
  t39 = 0.1e1 / t23 / t37
  t42 = t36 * t39
  t65 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t4 * t5 * jnp.pi * t21 * t23 * (0.1e1 + params.kappa * (0.1e1 - params.kappa / (params.kappa + (params.muGE + (params.muPBE - params.muGE) * params.alpha * t27 * t31 * t36 * t39 / (0.1e1 + params.alpha * t27 * t31 * t42 / 0.24e2) / 0.24e2) * t27 * t31 * t42 / 0.24e2))))
  res = 0.2e1 * t65
  return res