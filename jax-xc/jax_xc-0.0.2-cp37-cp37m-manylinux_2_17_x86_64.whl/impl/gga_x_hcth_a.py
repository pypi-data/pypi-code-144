"""Generated from gga_x_hcth_a.mpl."""

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
  t29 = t2 ** 2
  t31 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t34 = 4 ** (0.1e1 / 0.3e1)
  t35 = t29 / t31 * t34
  t36 = r0 ** 2
  t37 = r0 ** (0.1e1 / 0.3e1)
  t38 = t37 ** 2
  t42 = jnp.sqrt(s0)
  t45 = t42 / t37 / r0
  t46 = jnp.arcsinh(t45)
  t49 = 0.1e1 + 0.252e-1 * t45 * t46
  t52 = t49 ** 2
  t63 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.109878e1 + 0.93333333333333333332e-3 * t35 * s0 / t38 / t36 * (-0.251173e1 / t49 + 0.37198333333333333333e1 / t52)))
  t65 = jnp.where(t10, t15, -t17)
  t66 = jnp.where(t14, t11, t65)
  t67 = 0.1e1 + t66
  t69 = t67 ** (0.1e1 / 0.3e1)
  t71 = jnp.where(t67 <= p.zeta_threshold, t23, t69 * t67)
  t73 = r1 ** 2
  t74 = r1 ** (0.1e1 / 0.3e1)
  t75 = t74 ** 2
  t79 = jnp.sqrt(s2)
  t82 = t79 / t74 / r1
  t83 = jnp.arcsinh(t82)
  t86 = 0.1e1 + 0.252e-1 * t82 * t83
  t89 = t86 ** 2
  t100 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t71 * t27 * (0.109878e1 + 0.93333333333333333332e-3 * t35 * s2 / t75 / t73 * (-0.251173e1 / t86 + 0.37198333333333333333e1 / t89)))
  res = t63 + t100
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
  t21 = t3 ** 2
  t23 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t26 = 4 ** (0.1e1 / 0.3e1)
  t28 = 2 ** (0.1e1 / 0.3e1)
  t29 = t28 ** 2
  t31 = r0 ** 2
  t32 = t19 ** 2
  t35 = jnp.sqrt(s0)
  t36 = t35 * t28
  t38 = 0.1e1 / t19 / r0
  t40 = jnp.arcsinh(t36 * t38)
  t44 = 0.1e1 + 0.252e-1 * t36 * t38 * t40
  t47 = t44 ** 2
  t59 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.109878e1 + 0.93333333333333333332e-3 * t21 / t23 * t26 * s0 * t29 / t32 / t31 * (-0.251173e1 / t44 + 0.37198333333333333333e1 / t47)))
  res = 0.2e1 * t59
  return res