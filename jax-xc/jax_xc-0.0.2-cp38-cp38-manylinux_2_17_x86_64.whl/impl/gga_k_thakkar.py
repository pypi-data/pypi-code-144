"""Generated from gga_k_thakkar.mpl."""

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
  t33 = r0 ** 2
  t34 = r0 ** (0.1e1 / 0.3e1)
  t35 = t34 ** 2
  t39 = jnp.sqrt(s0)
  t41 = 0.1e1 / t34 / r0
  t42 = t39 * t41
  t43 = jnp.arcsinh(t42)
  t50 = 4 ** (0.1e1 / 0.3e1)
  t62 = jnp.where(r0 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t29 * t31 * (0.1e1 + 0.55e-2 * s0 / t35 / t33 / (0.1e1 + 0.253e-1 * t42 * t43) - 0.72e-1 * t42 / (0.2e1 * t50 * t39 * t41 + 0.1e1)))
  t64 = jnp.where(t11, t16, -t18)
  t65 = jnp.where(t15, t12, t64)
  t66 = 0.1e1 + t65
  t68 = t66 ** (0.1e1 / 0.3e1)
  t69 = t68 ** 2
  t71 = jnp.where(t66 <= p.zeta_threshold, t25, t69 * t66)
  t73 = r1 ** 2
  t74 = r1 ** (0.1e1 / 0.3e1)
  t75 = t74 ** 2
  t79 = jnp.sqrt(s2)
  t81 = 0.1e1 / t74 / r1
  t82 = t79 * t81
  t83 = jnp.arcsinh(t82)
  t101 = jnp.where(r1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t71 * t31 * (0.1e1 + 0.55e-2 * s2 / t75 / t73 / (0.1e1 + 0.253e-1 * t82 * t83) - 0.72e-1 * t82 / (0.2e1 * t50 * t79 * t81 + 0.1e1)))
  res = t62 + t101
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
  t25 = 2 ** (0.1e1 / 0.3e1)
  t26 = t25 ** 2
  t28 = r0 ** 2
  t31 = jnp.sqrt(s0)
  t32 = t31 * t25
  t34 = 0.1e1 / t22 / r0
  t36 = jnp.arcsinh(t32 * t34)
  t45 = 4 ** (0.1e1 / 0.3e1)
  t59 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t4 * t5 * jnp.pi * t21 * t23 * (0.1e1 + 0.55e-2 * s0 * t26 / t23 / t28 / (0.1e1 + 0.253e-1 * t32 * t34 * t36) - 0.72e-1 * t32 * t34 / (0.2e1 * t45 * t31 * t25 * t34 + 0.1e1)))
  res = 0.2e1 * t59
  return res