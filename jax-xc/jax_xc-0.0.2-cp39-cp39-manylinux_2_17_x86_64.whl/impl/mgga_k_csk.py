"""Generated from mgga_k_csk.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
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
  t33 = 6 ** (0.1e1 / 0.3e1)
  t34 = jnp.pi ** 2
  t35 = t34 ** (0.1e1 / 0.3e1)
  t36 = t35 ** 2
  t38 = t33 / t36
  t39 = r0 ** 2
  t40 = r0 ** (0.1e1 / 0.3e1)
  t41 = t40 ** 2
  t45 = t38 * s0 / t41 / t39
  t53 = 0.5e1 / 0.54e2 * t38 * l0 / t41 / r0 - 0.5e1 / 0.81e2 * t45
  t55 = jnp.log(0.1e1 - 2.220446049250313e-16)
  t56 = 0.1e1 / params.csk_a
  t57 = (-t55) ** (-t56)
  t59 = jnp.log(2.220446049250313e-16)
  t60 = (-t59) ** (-t56)
  t61 = -t60 < t53
  t62 = jnp.where(t61, -t60, t53)
  t64 = jnp.where(-t57 < t62, t62, -t57)
  t65 = abs(t64)
  t66 = t65 ** params.csk_a
  t68 = jnp.exp(-0.1e1 / t66)
  t70 = (0.1e1 - t68) ** t56
  t71 = jnp.where(t61, 1, t70)
  t72 = jnp.where(t53 < -t57, 0, t71)
  t78 = jnp.where(r0 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t29 * t31 * (0.1e1 + 0.5e1 / 0.72e2 * t45 + t53 * t72))
  t80 = jnp.where(t11, t16, -t18)
  t81 = jnp.where(t15, t12, t80)
  t82 = 0.1e1 + t81
  t84 = t82 ** (0.1e1 / 0.3e1)
  t85 = t84 ** 2
  t87 = jnp.where(t82 <= p.zeta_threshold, t25, t85 * t82)
  t89 = r1 ** 2
  t90 = r1 ** (0.1e1 / 0.3e1)
  t91 = t90 ** 2
  t95 = t38 * s2 / t91 / t89
  t103 = 0.5e1 / 0.54e2 * t38 * l1 / t91 / r1 - 0.5e1 / 0.81e2 * t95
  t105 = -t60 < t103
  t106 = jnp.where(t105, -t60, t103)
  t108 = jnp.where(-t57 < t106, t106, -t57)
  t109 = abs(t108)
  t110 = t109 ** params.csk_a
  t112 = jnp.exp(-0.1e1 / t110)
  t114 = (0.1e1 - t112) ** t56
  t115 = jnp.where(t105, 1, t114)
  t116 = jnp.where(t103 < -t57, 0, t115)
  t122 = jnp.where(r1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t6 * t87 * t31 * (0.1e1 + 0.5e1 / 0.72e2 * t95 + t103 * t116))
  res = t78 + t122
  return res

def unpol(r0, s0, l0, tau0, params, p):
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
  t25 = 6 ** (0.1e1 / 0.3e1)
  t26 = jnp.pi ** 2
  t27 = t26 ** (0.1e1 / 0.3e1)
  t28 = t27 ** 2
  t30 = t25 / t28
  t31 = 2 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t34 = r0 ** 2
  t38 = t30 * s0 * t32 / t23 / t34
  t47 = 0.5e1 / 0.54e2 * t30 * l0 * t32 / t23 / r0 - 0.5e1 / 0.81e2 * t38
  t49 = jnp.log(0.1e1 - 2.220446049250313e-16)
  t50 = 0.1e1 / params.csk_a
  t51 = (-t49) ** (-t50)
  t53 = jnp.log(2.220446049250313e-16)
  t54 = (-t53) ** (-t50)
  t55 = -t54 < t47
  t56 = jnp.where(t55, -t54, t47)
  t58 = jnp.where(-t51 < t56, t56, -t51)
  t59 = abs(t58)
  t60 = t59 ** params.csk_a
  t62 = jnp.exp(-0.1e1 / t60)
  t64 = (0.1e1 - t62) ** t50
  t65 = jnp.where(t55, 1, t64)
  t66 = jnp.where(t47 < -t51, 0, t65)
  t72 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, 0.3e1 / 0.2e2 * t4 * t5 * jnp.pi * t21 * t23 * (0.1e1 + 0.5e1 / 0.72e2 * t38 + t47 * t66))
  res = 0.2e1 * t72
  return res