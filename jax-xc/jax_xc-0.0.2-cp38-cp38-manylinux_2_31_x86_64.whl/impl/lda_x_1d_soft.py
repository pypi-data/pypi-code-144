"""Generated from lda_x_1d_soft.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t3 = r0 + r1
  t4 = 0.1e1 / t3
  t5 = (r0 - r1) * t4
  t7 = 0.1e1 + t5 <= p.zeta_threshold
  t8 = jnp.logical_or(r0 <= p.dens_threshold, t7)
  t9 = p.zeta_threshold - 0.1e1
  t11 = 0.1e1 - t5 <= p.zeta_threshold
  t12 = -t9
  t13 = jnp.where(t11, t12, t5)
  t14 = jnp.where(t7, t9, t13)
  t15 = 0.1e1 + t14
  t17 = params.beta * t3
  t18 = t15 * jnp.pi * t17
  t19 = int1(t18)
  t21 = int2(t18)
  t22 = 0.1e1 / jnp.pi
  t24 = 0.1e1 / params.beta
  t25 = t24 * t4
  t31 = jnp.where(t8, 0, -0.25e0 * (-t21 * t22 * t25 + t15 * t19) * t22 * t24)
  t33 = jnp.logical_or(r1 <= p.dens_threshold, t11)
  t34 = jnp.where(t7, t12, -t5)
  t35 = jnp.where(t11, t9, t34)
  t36 = 0.1e1 + t35
  t38 = t36 * jnp.pi * t17
  t39 = int1(t38)
  t41 = int2(t38)
  t48 = jnp.where(t33, 0, -0.25e0 * (-t41 * t22 * t25 + t36 * t39) * t22 * t24)
  res = t31 + t48
  return res

def unpol(r0, params, p):
  t3 = 0.1e1 <= p.zeta_threshold
  t4 = jnp.logical_or(r0 / 0.2e1 <= p.dens_threshold, t3)
  t5 = p.zeta_threshold - 0.1e1
  t7 = jnp.where(t3, -t5, 0)
  t8 = jnp.where(t3, t5, t7)
  t9 = 0.1e1 + t8
  t12 = t9 * jnp.pi * params.beta * r0
  t13 = int1(t12)
  t15 = int2(t12)
  t16 = 0.1e1 / jnp.pi
  t18 = 0.1e1 / params.beta
  t26 = jnp.where(t4, 0, -0.25e0 * (t9 * t13 - t15 * t16 * t18 / r0) * t16 * t18)
  res = 0.2e1 * t26
  return res