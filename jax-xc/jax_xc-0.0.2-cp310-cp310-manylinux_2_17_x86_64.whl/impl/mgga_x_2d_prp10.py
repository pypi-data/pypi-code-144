"""Generated from mgga_x_2d_prp10.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable

from ._helper import lambertw

def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
  t1 = r0 ** 2
  t2 = 0.1e1 / t1
  t5 = tau0 * t2
  t9 = s0 / t1 / r0 / 0.8e1
  t11 = 0.1e1 / jnp.pi
  t12 = (l0 * t2 / 0.4e1 - t5 + t9) * t11
  t14 = jnp.where(-0.9999999999e0 < t12, t12, -0.9999999999e0)
  t15 = jnp.exp(-1)
  t17 = lambertw(t14 * t15)
  t20 = jax.scipy.special.i0(t17 / 0.2e1 + 0.1e1 / 0.2e1)
  t22 = t5 - t9
  t24 = jnp.where(0.1e-9 < t22, t22, 0.1e-9)
  t25 = jnp.sqrt(t24)
  t29 = jnp.sqrt(r0)
  res = -(jnp.pi * t20 - 0.4e1 / 0.3e1 * t11 * t25) * t29
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t1 = r0 ** 2
  t2 = 0.1e1 / t1
  t6 = 0.2e1 * tau0 * t2
  t10 = s0 / t1 / r0 / 0.4e1
  t12 = 0.1e1 / jnp.pi
  t13 = (l0 * t2 / 0.2e1 - t6 + t10) * t12
  t15 = jnp.where(-0.9999999999e0 < t13, t13, -0.9999999999e0)
  t16 = jnp.exp(-1)
  t18 = lambertw(t15 * t16)
  t21 = jax.scipy.special.i0(t18 / 0.2e1 + 0.1e1 / 0.2e1)
  t23 = t6 - t10
  t25 = jnp.where(0.1e-9 < t23, t23, 0.1e-9)
  t26 = jnp.sqrt(t25)
  t30 = jnp.sqrt(0.2e1)
  t32 = jnp.sqrt(r0)
  res = -(jnp.pi * t21 - 0.4e1 / 0.3e1 * t12 * t26) * t30 * t32 / 0.2e1
  return res