"""Generated from mgga_x_mbrxc_bg.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
  t2 = r0 + r1
  t3 = 0.1e1 / t2
  t6 = 0.2e1 * r0 * t3 <= p.zeta_threshold
  t7 = p.zeta_threshold - 0.1e1
  t10 = 0.2e1 * r1 * t3 <= p.zeta_threshold
  t11 = -t7
  t13 = (r0 - r1) * t3
  t14 = jnp.where(t10, t11, t13)
  t15 = jnp.where(t6, t7, t14)
  t16 = 0.1e1 + t15
  t18 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t19 = t18 * p.zeta_threshold
  t20 = t16 ** (0.1e1 / 0.3e1)
  t22 = jnp.where(t16 <= p.zeta_threshold, t19, t20 * t16)
  t23 = t2 ** (0.1e1 / 0.3e1)
  t25 = 32 ** (0.1e1 / 0.3e1)
  t27 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t29 = t25 / t27
  t31 = 4 ** (0.1e1 / 0.3e1)
  t32 = r0 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t38 = 6 ** (0.1e1 / 0.3e1)
  t39 = t38 ** 2
  t40 = jnp.pi ** 2
  t41 = t40 ** (0.1e1 / 0.3e1)
  t42 = t41 ** 2
  t44 = 0.3e1 / 0.1e2 * t39 * t42
  t45 = r0 ** 2
  t50 = s0 ** 2
  t51 = t45 ** 2
  t57 = 0.149492e0 * tau0 / t33 / r0 - t44 + 0.147e0 * s0 / t33 / t45 + 0.32e-2 * t50 / t32 / t51 / r0
  t58 = abs(t57)
  t61 = jnp.where(0.e0 < t57, 0.5e-12, -0.5e-12)
  t62 = jnp.where(t58 < 0.5e-12, t61, t57)
  t63 = mbrxc_x(t62)
  t65 = jnp.exp(t63 / 0.3e1)
  t67 = jnp.exp(-t63)
  t68 = t63 ** 2
  t76 = (0.1e1 + t63) ** (0.1e1 / 0.3e1)
  t82 = jnp.where(r0 <= p.dens_threshold, 0, -t22 * t23 * t29 * t31 * t65 * (0.8e1 - t67 * (t68 + 0.5e1 * t63 + 0.8e1)) / t63 / t76 / 0.64e2)
  t84 = jnp.where(t6, t11, -t13)
  t85 = jnp.where(t10, t7, t84)
  t86 = 0.1e1 + t85
  t88 = t86 ** (0.1e1 / 0.3e1)
  t90 = jnp.where(t86 <= p.zeta_threshold, t19, t88 * t86)
  t93 = r1 ** (0.1e1 / 0.3e1)
  t94 = t93 ** 2
  t99 = r1 ** 2
  t104 = s2 ** 2
  t105 = t99 ** 2
  t111 = 0.149492e0 * tau1 / t94 / r1 - t44 + 0.147e0 * s2 / t94 / t99 + 0.32e-2 * t104 / t93 / t105 / r1
  t112 = abs(t111)
  t115 = jnp.where(0.e0 < t111, 0.5e-12, -0.5e-12)
  t116 = jnp.where(t112 < 0.5e-12, t115, t111)
  t117 = mbrxc_x(t116)
  t119 = jnp.exp(t117 / 0.3e1)
  t121 = jnp.exp(-t117)
  t122 = t117 ** 2
  t130 = (0.1e1 + t117) ** (0.1e1 / 0.3e1)
  t136 = jnp.where(r1 <= p.dens_threshold, 0, -t90 * t23 * t29 * t31 * t119 * (0.8e1 - t121 * (t122 + 0.5e1 * t117 + 0.8e1)) / t117 / t130 / 0.64e2)
  res = t82 + t136
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t3 = 0.1e1 <= p.zeta_threshold
  t4 = p.zeta_threshold - 0.1e1
  t6 = jnp.where(t3, -t4, 0)
  t7 = jnp.where(t3, t4, t6)
  t8 = 0.1e1 + t7
  t10 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t12 = t8 ** (0.1e1 / 0.3e1)
  t14 = jnp.where(t8 <= p.zeta_threshold, t10 * p.zeta_threshold, t12 * t8)
  t15 = r0 ** (0.1e1 / 0.3e1)
  t17 = 32 ** (0.1e1 / 0.3e1)
  t19 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t23 = 4 ** (0.1e1 / 0.3e1)
  t24 = 2 ** (0.1e1 / 0.3e1)
  t25 = t24 ** 2
  t27 = t15 ** 2
  t32 = 6 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t34 = jnp.pi ** 2
  t35 = t34 ** (0.1e1 / 0.3e1)
  t36 = t35 ** 2
  t40 = r0 ** 2
  t45 = s0 ** 2
  t47 = t40 ** 2
  t53 = 0.149492e0 * tau0 * t25 / t27 / r0 - 0.3e1 / 0.1e2 * t33 * t36 + 0.147e0 * s0 * t25 / t27 / t40 + 0.64e-2 * t45 * t24 / t15 / t47 / r0
  t54 = abs(t53)
  t57 = jnp.where(0.e0 < t53, 0.5e-12, -0.5e-12)
  t58 = jnp.where(t54 < 0.5e-12, t57, t53)
  t59 = mbrxc_x(t58)
  t61 = jnp.exp(t59 / 0.3e1)
  t63 = jnp.exp(-t59)
  t64 = t59 ** 2
  t72 = (0.1e1 + t59) ** (0.1e1 / 0.3e1)
  t78 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -t14 * t15 * t17 / t19 * t23 * t61 * (0.8e1 - t63 * (t64 + 0.5e1 * t59 + 0.8e1)) / t59 / t72 / 0.64e2)
  res = 0.2e1 * t78
  return res