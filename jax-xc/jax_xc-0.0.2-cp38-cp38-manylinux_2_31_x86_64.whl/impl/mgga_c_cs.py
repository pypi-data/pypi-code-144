"""Generated from mgga_c_cs.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
  t1 = r0 - r1
  t2 = t1 ** 2
  t3 = r0 + r1
  t4 = t3 ** 2
  t8 = t3 ** (0.1e1 / 0.3e1)
  t9 = 0.1e1 / t8
  t15 = jnp.exp(-0.2533e0 * t9)
  t17 = t1 / t3
  t18 = 0.1e1 + t17
  t20 = p.zeta_threshold ** 2
  t21 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t22 = t21 ** 2
  t23 = t22 * t20
  t24 = t18 ** 2
  t25 = t18 ** (0.1e1 / 0.3e1)
  t26 = t25 ** 2
  t28 = jnp.where(t18 <= p.zeta_threshold, t23, t26 * t24)
  t29 = 2 ** (0.1e1 / 0.3e1)
  t31 = r0 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t34 = 0.1e1 / t32 / r0
  t36 = l0 * t34
  t40 = 0.1e1 - t17
  t42 = t40 ** 2
  t43 = t40 ** (0.1e1 / 0.3e1)
  t44 = t43 ** 2
  t46 = jnp.where(t40 <= p.zeta_threshold, t23, t44 * t42)
  t48 = r1 ** (0.1e1 / 0.3e1)
  t49 = t48 ** 2
  t51 = 0.1e1 / t49 / r1
  t53 = l1 * t51
  t59 = t8 ** 2
  t63 = t18 / 0.2e1
  t64 = t63 ** (0.1e1 / 0.3e1)
  t65 = t64 ** 2
  t68 = t40 / 0.2e1
  t69 = t68 ** (0.1e1 / 0.3e1)
  t70 = t69 ** 2
  res = -0.4918e-1 * (0.1e1 - t2 / t4) / (0.1e1 + 0.34899999999999999998e0 * t9) * (0.1e1 + 0.264e0 * t15 * (t28 * t29 * (tau0 * t34 - t36 / 0.8e1) / 0.8e1 + t46 * t29 * (tau1 * t51 - t53 / 0.8e1) / 0.8e1 - (s0 + 0.2e1 * s1 + s2) / t59 / t4 / 0.8e1 + t36 * t65 * t63 / 0.8e1 + t53 * t70 * t68 / 0.8e1))
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t1 = r0 ** (0.1e1 / 0.3e1)
  t2 = 0.1e1 / t1
  t7 = jnp.exp(-0.2533e0 * t2)
  t9 = p.zeta_threshold ** 2
  t10 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t11 = t10 ** 2
  t13 = jnp.where(0.1e1 <= p.zeta_threshold, t11 * t9, 1)
  t14 = 2 ** (0.1e1 / 0.3e1)
  t16 = t14 ** 2
  t18 = t1 ** 2
  t20 = 0.1e1 / t18 / r0
  t28 = r0 ** 2
  res = -0.4918e-1 / (0.1e1 + 0.34899999999999999998e0 * t2) * (0.1e1 + 0.264e0 * t7 * (t13 * t14 * (tau0 * t16 * t20 - l0 * t16 * t20 / 0.8e1) / 0.4e1 - s0 / t18 / t28 / 0.8e1 + l0 * t20 / 0.8e1))
  return res