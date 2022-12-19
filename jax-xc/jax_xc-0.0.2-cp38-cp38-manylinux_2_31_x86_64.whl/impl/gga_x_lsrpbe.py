"""Generated from gga_x_lsrpbe.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = 3 ** (0.1e1 / 0.3e1)
  t3 = jnp.pi ** (0.1e1 / 0.3e1)
  t5 = t2 / t3
  t6 = r0 + r1
  t7 = 0.1e1 / t6
  t10 = 0.2e1 * r0 * t7 <= p.zeta_threshold
  t11 = p.zeta_threshold - 0.1e1
  t14 = 0.2e1 * r1 * t7 <= p.zeta_threshold
  t15 = -t11
  t17 = (r0 - r1) * t7
  t18 = jnp.where(t14, t15, t17)
  t19 = jnp.where(t10, t11, t18)
  t20 = 0.1e1 + t19
  t22 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t23 = t22 * p.zeta_threshold
  t24 = t20 ** (0.1e1 / 0.3e1)
  t26 = jnp.where(t20 <= p.zeta_threshold, t23, t24 * t20)
  t27 = t6 ** (0.1e1 / 0.3e1)
  t29 = 6 ** (0.1e1 / 0.3e1)
  t31 = jnp.pi ** 2
  t32 = t31 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t34 = 0.1e1 / t33
  t35 = params.mu * t29 * t34
  t36 = r0 ** 2
  t37 = r0 ** (0.1e1 / 0.3e1)
  t38 = t37 ** 2
  t40 = 0.1e1 / t38 / t36
  t42 = 0.1e1 / params.kappa
  t46 = jnp.exp(-t35 * s0 * t40 * t42 / 0.24e2)
  t49 = params.kappa + 0.1e1
  t50 = params.alpha * t29
  t55 = jnp.exp(-t50 * t34 * s0 * t40 / 0.24e2)
  t62 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + params.kappa * (0.1e1 - t46) - t49 * (0.1e1 - t55)))
  t64 = jnp.where(t10, t15, -t17)
  t65 = jnp.where(t14, t11, t64)
  t66 = 0.1e1 + t65
  t68 = t66 ** (0.1e1 / 0.3e1)
  t70 = jnp.where(t66 <= p.zeta_threshold, t23, t68 * t66)
  t72 = r1 ** 2
  t73 = r1 ** (0.1e1 / 0.3e1)
  t74 = t73 ** 2
  t76 = 0.1e1 / t74 / t72
  t81 = jnp.exp(-t35 * s2 * t76 * t42 / 0.24e2)
  t88 = jnp.exp(-t50 * t34 * s2 * t76 / 0.24e2)
  t95 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t70 * t27 * (0.1e1 + params.kappa * (0.1e1 - t81) - t49 * (0.1e1 - t88)))
  res = t62 + t95
  return res

def unpol(r0, s0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t7 = 0.1e1 <= p.zeta_threshold
  t8 = p.zeta_threshold - 0.1e1
  t10 = jnp.where(t7, -t8, 0)
  t11 = jnp.where(t7, t8, t10)
  t12 = 0.1e1 + t11
  t14 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t16 = t12 ** (0.1e1 / 0.3e1)
  t18 = jnp.where(t12 <= p.zeta_threshold, t14 * p.zeta_threshold, t16 * t12)
  t19 = r0 ** (0.1e1 / 0.3e1)
  t21 = 6 ** (0.1e1 / 0.3e1)
  t23 = jnp.pi ** 2
  t24 = t23 ** (0.1e1 / 0.3e1)
  t25 = t24 ** 2
  t26 = 0.1e1 / t25
  t28 = 2 ** (0.1e1 / 0.3e1)
  t29 = t28 ** 2
  t30 = s0 * t29
  t31 = r0 ** 2
  t32 = t19 ** 2
  t34 = 0.1e1 / t32 / t31
  t40 = jnp.exp(-params.mu * t21 * t26 * t30 * t34 / params.kappa / 0.24e2)
  t49 = jnp.exp(-params.alpha * t21 * t26 * t30 * t34 / 0.24e2)
  t56 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 + params.kappa * (0.1e1 - t40) - (params.kappa + 0.1e1) * (0.1e1 - t49)))
  res = 0.2e1 * t56
  return res