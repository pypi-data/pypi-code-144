"""Generated from gga_x_lv_rpw86.mpl."""

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
  t41 = t34 * s0 / t37 / t35
  t44 = t30 ** 2
  t45 = 0.1e1 / t44
  t46 = s0 ** 2
  t48 = t45 * t46 * s0
  t49 = t35 ** 2
  t50 = t49 ** 2
  t51 = 0.1e1 / t50
  t52 = t48 * t51
  t53 = 0.9453125e-5 * t52
  t58 = t29 ** 2
  t61 = t58 / t31 / t30
  t70 = (0.1e1 + 0.77125000000000000002e-1 * t41 + 0.30086805555555555556e-1 * t61 * t46 / t36 / t49 / r0 + 0.70746527777777777778e-4 * t52) ** (0.1e1 / 0.15e2)
  t81 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * ((0.1e1 + 0.39310185185185185185e-2 * t41) / (0.1e1 + t53) + 0.9453125e-5 * t48 * t51 * t70 / (0.115e1 + t53)))
  t83 = jnp.where(t10, t15, -t17)
  t84 = jnp.where(t14, t11, t83)
  t85 = 0.1e1 + t84
  t87 = t85 ** (0.1e1 / 0.3e1)
  t89 = jnp.where(t85 <= p.zeta_threshold, t23, t87 * t85)
  t91 = r1 ** 2
  t92 = r1 ** (0.1e1 / 0.3e1)
  t93 = t92 ** 2
  t97 = t34 * s2 / t93 / t91
  t100 = s2 ** 2
  t102 = t45 * t100 * s2
  t103 = t91 ** 2
  t104 = t103 ** 2
  t105 = 0.1e1 / t104
  t106 = t102 * t105
  t107 = 0.9453125e-5 * t106
  t120 = (0.1e1 + 0.77125000000000000002e-1 * t97 + 0.30086805555555555556e-1 * t61 * t100 / t92 / t103 / r1 + 0.70746527777777777778e-4 * t106) ** (0.1e1 / 0.15e2)
  t131 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t89 * t27 * ((0.1e1 + 0.39310185185185185185e-2 * t97) / (0.1e1 + t107) + 0.9453125e-5 * t102 * t105 * t120 / (0.115e1 + t107)))
  res = t81 + t131
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
  t35 = t21 / t24 * s0 * t28 / t31 / t30
  t38 = t22 ** 2
  t40 = s0 ** 2
  t42 = 0.1e1 / t38 * t40 * s0
  t43 = t30 ** 2
  t44 = t43 ** 2
  t45 = 0.1e1 / t44
  t46 = t42 * t45
  t47 = 0.378125e-4 * t46
  t52 = t21 ** 2
  t65 = (0.1e1 + 0.77125000000000000002e-1 * t35 + 0.60173611111111111112e-1 * t52 / t23 / t22 * t40 * t27 / t19 / t43 / r0 + 0.28298611111111111111e-3 * t46) ** (0.1e1 / 0.15e2)
  t76 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * ((0.1e1 + 0.39310185185185185185e-2 * t35) / (0.1e1 + t47) + 0.378125e-4 * t42 * t45 * t65 / (0.115e1 + t47)))
  res = 0.2e1 * t76
  return res