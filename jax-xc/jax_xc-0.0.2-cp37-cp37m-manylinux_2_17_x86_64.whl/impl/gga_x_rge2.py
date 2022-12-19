"""Generated from gga_x_rge2.mpl."""

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
  t30 = jnp.pi ** 2
  t31 = t30 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t34 = t29 / t32
  t35 = r0 ** 2
  t36 = r0 ** (0.1e1 / 0.3e1)
  t37 = t36 ** 2
  t43 = t29 ** 2
  t46 = t43 / t31 / t30
  t47 = s0 ** 2
  t48 = t35 ** 2
  t62 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1804e1 - 0.646416e0 / (0.804e0 + 0.5e1 / 0.972e3 * t34 * s0 / t37 / t35 + 0.32911784453572541027e-4 * t46 * t47 / t36 / t48 / r0)))
  t64 = jnp.where(t10, t15, -t17)
  t65 = jnp.where(t14, t11, t64)
  t66 = 0.1e1 + t65
  t68 = t66 ** (0.1e1 / 0.3e1)
  t70 = jnp.where(t66 <= p.zeta_threshold, t23, t68 * t66)
  t72 = r1 ** 2
  t73 = r1 ** (0.1e1 / 0.3e1)
  t74 = t73 ** 2
  t80 = s2 ** 2
  t81 = t72 ** 2
  t95 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t70 * t27 * (0.1804e1 - 0.646416e0 / (0.804e0 + 0.5e1 / 0.972e3 * t34 * s2 / t74 / t72 + 0.32911784453572541027e-4 * t46 * t80 / t73 / t81 / r1)))
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
  t22 = jnp.pi ** 2
  t23 = t22 ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t27 = 2 ** (0.1e1 / 0.3e1)
  t28 = t27 ** 2
  t30 = r0 ** 2
  t31 = t19 ** 2
  t37 = t21 ** 2
  t41 = s0 ** 2
  t43 = t30 ** 2
  t57 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1804e1 - 0.646416e0 / (0.804e0 + 0.5e1 / 0.972e3 * t21 / t24 * s0 * t28 / t31 / t30 + 0.65823568907145082055e-4 * t37 / t23 / t22 * t41 * t27 / t19 / t43 / r0)))
  res = 0.2e1 * t57
  return res