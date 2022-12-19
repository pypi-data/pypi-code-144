"""Generated from hyb_mgga_x_dldf.mpl."""

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
  t28 = t6 ** (0.1e1 / 0.3e1)
  t29 = 6 ** (0.1e1 / 0.3e1)
  t30 = jnp.pi ** 2
  t31 = t30 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t34 = t29 / t32
  t35 = r0 ** 2
  t36 = r0 ** (0.1e1 / 0.3e1)
  t37 = t36 ** 2
  t48 = t29 ** 2
  t50 = 0.3e1 / 0.1e2 * t48 * t32
  t53 = tau0 / t37 / r0
  t54 = t50 - t53
  t55 = t50 + t53
  t59 = t54 ** 2
  t60 = t55 ** 2
  t69 = t59 ** 2
  t70 = t60 ** 2
  t78 = jnp.where(r0 <= p.dens_threshold, 0, -0.1445951625e0 * t5 * t26 * t28 * (0.58827323e1 - 0.2384107471346329e2 / (0.48827323e1 + 0.146297e-1 * t34 * s0 / t37 / t35)) * (0.1e1 - 0.1637571e0 * t54 / t55 - 0.1880028e0 * t59 / t60 - 0.4490609e0 * t59 * t54 / t60 / t55 - 0.82359e-2 * t69 / t70))
  t80 = jnp.where(t10, t15, -t17)
  t81 = jnp.where(t14, t11, t80)
  t82 = 0.1e1 + t81
  t84 = t82 ** (0.1e1 / 0.3e1)
  t86 = jnp.where(t82 <= p.zeta_threshold, t23, t84 * t82)
  t88 = r1 ** 2
  t89 = r1 ** (0.1e1 / 0.3e1)
  t90 = t89 ** 2
  t103 = tau1 / t90 / r1
  t104 = t50 - t103
  t105 = t50 + t103
  t109 = t104 ** 2
  t110 = t105 ** 2
  t119 = t109 ** 2
  t120 = t110 ** 2
  t128 = jnp.where(r1 <= p.dens_threshold, 0, -0.1445951625e0 * t5 * t86 * t28 * (0.58827323e1 - 0.2384107471346329e2 / (0.48827323e1 + 0.146297e-1 * t34 * s2 / t90 / t88)) * (0.1e1 - 0.1637571e0 * t104 / t105 - 0.1880028e0 * t109 / t110 - 0.4490609e0 * t109 * t104 / t110 / t105 - 0.82359e-2 * t119 / t120))
  res = t78 + t128
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
  t20 = r0 ** (0.1e1 / 0.3e1)
  t21 = 6 ** (0.1e1 / 0.3e1)
  t22 = jnp.pi ** 2
  t23 = t22 ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t27 = 2 ** (0.1e1 / 0.3e1)
  t28 = t27 ** 2
  t30 = r0 ** 2
  t31 = t20 ** 2
  t42 = t21 ** 2
  t44 = 0.3e1 / 0.1e2 * t42 * t24
  t48 = tau0 * t28 / t31 / r0
  t49 = t44 - t48
  t50 = t44 + t48
  t54 = t49 ** 2
  t55 = t50 ** 2
  t64 = t54 ** 2
  t65 = t55 ** 2
  t73 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.1445951625e0 * t3 / t4 * t18 * t20 * (0.58827323e1 - 0.2384107471346329e2 / (0.48827323e1 + 0.146297e-1 * t21 / t24 * s0 * t28 / t31 / t30)) * (0.1e1 - 0.1637571e0 * t49 / t50 - 0.1880028e0 * t54 / t55 - 0.4490609e0 * t54 * t49 / t55 / t50 - 0.82359e-2 * t64 / t65))
  res = 0.2e1 * t73
  return res