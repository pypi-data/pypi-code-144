"""Generated from gga_x_pbea.mpl."""

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
  t29 = r0 ** 2
  t30 = r0 ** (0.1e1 / 0.3e1)
  t31 = t30 ** 2
  t37 = (0.1e1 + 0.86399408095363255118e-2 * s0 / t31 / t29) ** (-0.52e0)
  t43 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1804e1 - 0.804e0 * t37))
  t45 = jnp.where(t10, t15, -t17)
  t46 = jnp.where(t14, t11, t45)
  t47 = 0.1e1 + t46
  t49 = t47 ** (0.1e1 / 0.3e1)
  t51 = jnp.where(t47 <= p.zeta_threshold, t23, t49 * t47)
  t53 = r1 ** 2
  t54 = r1 ** (0.1e1 / 0.3e1)
  t55 = t54 ** 2
  t61 = (0.1e1 + 0.86399408095363255118e-2 * s2 / t55 / t53) ** (-0.52e0)
  t67 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t51 * t27 * (0.1804e1 - 0.804e0 * t61))
  res = t43 + t67
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
  t21 = 2 ** (0.1e1 / 0.3e1)
  t22 = t21 ** 2
  t24 = r0 ** 2
  t25 = t19 ** 2
  t31 = (0.1e1 + 0.86399408095363255118e-2 * s0 * t22 / t25 / t24) ** (-0.52e0)
  t37 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1804e1 - 0.804e0 * t31))
  res = 0.2e1 * t37
  return res