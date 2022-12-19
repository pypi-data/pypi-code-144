"""Generated from mgga_x_jk.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
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
  t29 = t2 ** 2
  t32 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t34 = 4 ** (0.1e1 / 0.3e1)
  t36 = params.beta * t29 / t32 * t34
  t37 = r0 ** 2
  t38 = r0 ** (0.1e1 / 0.3e1)
  t39 = t38 ** 2
  t40 = t39 * t37
  t42 = s0 / t40
  t43 = params.gamma * params.beta
  t44 = jnp.sqrt(s0)
  t47 = t44 / t38 / r0
  t48 = jnp.arcsinh(t47)
  t71 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + 0.2e1 / 0.9e1 * t36 * t42 / (t43 * t47 * t48 + 0.1e1) / (0.1e1 + 0.2e1 * (t42 - l0 / t39 / r0) / s0 * t40)))
  t73 = jnp.where(t10, t15, -t17)
  t74 = jnp.where(t14, t11, t73)
  t75 = 0.1e1 + t74
  t77 = t75 ** (0.1e1 / 0.3e1)
  t79 = jnp.where(t75 <= p.zeta_threshold, t23, t77 * t75)
  t81 = r1 ** 2
  t82 = r1 ** (0.1e1 / 0.3e1)
  t83 = t82 ** 2
  t84 = t83 * t81
  t86 = s2 / t84
  t87 = jnp.sqrt(s2)
  t90 = t87 / t82 / r1
  t91 = jnp.arcsinh(t90)
  t114 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t79 * t27 * (0.1e1 + 0.2e1 / 0.9e1 * t36 * t86 / (t43 * t90 * t91 + 0.1e1) / (0.1e1 + 0.2e1 * (t86 - l1 / t83 / r1) / s2 * t84)))
  res = t71 + t114
  return res

def unpol(r0, s0, l0, tau0, params, p):
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
  t21 = t3 ** 2
  t24 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t26 = 4 ** (0.1e1 / 0.3e1)
  t29 = 2 ** (0.1e1 / 0.3e1)
  t30 = t29 ** 2
  t31 = s0 * t30
  t32 = r0 ** 2
  t33 = t19 ** 2
  t34 = t33 * t32
  t35 = 0.1e1 / t34
  t37 = jnp.sqrt(s0)
  t40 = 0.1e1 / t19 / r0
  t44 = jnp.arcsinh(t37 * t29 * t40)
  t70 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 + 0.2e1 / 0.9e1 * params.beta * t21 / t24 * t26 * t31 * t35 / (params.gamma * params.beta * t37 * t29 * t40 * t44 + 0.1e1) / (0.1e1 + (t31 * t35 - l0 * t30 / t33 / r0) / s0 * t29 * t34)))
  res = 0.2e1 * t70
  return res