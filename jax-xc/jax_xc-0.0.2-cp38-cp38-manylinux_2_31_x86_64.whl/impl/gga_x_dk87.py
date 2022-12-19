"""Generated from gga_x_dk87.mpl."""

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
  t29 = 0.1e1 / jnp.pi
  t30 = 6 ** (0.1e1 / 0.3e1)
  t31 = t30 ** 2
  t33 = jnp.pi ** 2
  t34 = t33 ** (0.1e1 / 0.3e1)
  t36 = t2 ** 2
  t38 = t29 ** (0.1e1 / 0.3e1)
  t41 = t29 * t31 / t34 * t36 / t38
  t42 = 4 ** (0.1e1 / 0.3e1)
  t44 = r0 ** 2
  t45 = r0 ** (0.1e1 / 0.3e1)
  t46 = t45 ** 2
  t48 = 0.1e1 / t46 / t44
  t49 = jnp.sqrt(s0)
  t53 = (t49 / t45 / r0) ** params.alpha
  t69 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + 0.7e1 / 0.11664e5 * t41 * t42 * s0 * t48 * (params.a1 * t53 + 0.1e1) / (params.b1 * s0 * t48 + 0.1e1)))
  t71 = jnp.where(t10, t15, -t17)
  t72 = jnp.where(t14, t11, t71)
  t73 = 0.1e1 + t72
  t75 = t73 ** (0.1e1 / 0.3e1)
  t77 = jnp.where(t73 <= p.zeta_threshold, t23, t75 * t73)
  t80 = r1 ** 2
  t81 = r1 ** (0.1e1 / 0.3e1)
  t82 = t81 ** 2
  t84 = 0.1e1 / t82 / t80
  t85 = jnp.sqrt(s2)
  t89 = (t85 / t81 / r1) ** params.alpha
  t105 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t77 * t27 * (0.1e1 + 0.7e1 / 0.11664e5 * t41 * t42 * s2 * t84 * (params.a1 * t89 + 0.1e1) / (params.b1 * s2 * t84 + 0.1e1)))
  res = t69 + t105
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
  t21 = 0.1e1 / jnp.pi
  t22 = 6 ** (0.1e1 / 0.3e1)
  t23 = t22 ** 2
  t25 = jnp.pi ** 2
  t26 = t25 ** (0.1e1 / 0.3e1)
  t28 = t3 ** 2
  t30 = t21 ** (0.1e1 / 0.3e1)
  t34 = 4 ** (0.1e1 / 0.3e1)
  t36 = 2 ** (0.1e1 / 0.3e1)
  t37 = t36 ** 2
  t39 = r0 ** 2
  t40 = t19 ** 2
  t42 = 0.1e1 / t40 / t39
  t43 = jnp.sqrt(s0)
  t48 = (t43 * t36 / t19 / r0) ** params.alpha
  t65 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 + 0.7e1 / 0.11664e5 * t21 * t23 / t26 * t28 / t30 * t34 * s0 * t37 * t42 * (params.a1 * t48 + 0.1e1) / (params.b1 * s0 * t37 * t42 + 0.1e1)))
  res = 0.2e1 * t65
  return res