"""Generated from gga_x_s12.mpl."""

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
  t28 = t6 ** (0.1e1 / 0.3e1)
  t29 = t28 * params.bx
  t31 = r0 ** 2
  t32 = r0 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t35 = 0.1e1 / t33 / t31
  t37 = s0 ** 2
  t39 = t31 ** 2
  t58 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t29 * (params.A + params.B * (0.1e1 - 0.1e1 / (0.1e1 + params.C * s0 * t35 + params.D * t37 / t32 / t39 / r0)) * (0.1e1 - 0.1e1 / (params.E * s0 * t35 + 0.1e1))))
  t60 = jnp.where(t10, t15, -t17)
  t61 = jnp.where(t14, t11, t60)
  t62 = 0.1e1 + t61
  t64 = t62 ** (0.1e1 / 0.3e1)
  t66 = jnp.where(t62 <= p.zeta_threshold, t23, t64 * t62)
  t69 = r1 ** 2
  t70 = r1 ** (0.1e1 / 0.3e1)
  t71 = t70 ** 2
  t73 = 0.1e1 / t71 / t69
  t75 = s2 ** 2
  t77 = t69 ** 2
  t96 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t66 * t29 * (params.A + params.B * (0.1e1 - 0.1e1 / (0.1e1 + params.C * s2 * t73 + params.D * t75 / t70 / t77 / r1)) * (0.1e1 - 0.1e1 / (params.E * s2 * t73 + 0.1e1))))
  res = t58 + t96
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
  t20 = r0 ** (0.1e1 / 0.3e1)
  t23 = 2 ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t25 = r0 ** 2
  t26 = t20 ** 2
  t29 = t24 / t26 / t25
  t31 = s0 ** 2
  t33 = t25 ** 2
  t54 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t20 * params.bx * (params.A + params.B * (0.1e1 - 0.1e1 / (0.1e1 + params.C * s0 * t29 + 0.2e1 * params.D * t31 * t23 / t20 / t33 / r0)) * (0.1e1 - 0.1e1 / (params.E * s0 * t29 + 0.1e1))))
  res = 0.2e1 * t54
  return res