"""Generated from gga_c_op_xalpha.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t2 = r0 + r1
  t3 = 0.1e1 / t2
  t4 = (r0 - r1) * t3
  t5 = abs(t4)
  t10 = jnp.logical_and(r0 <= p.dens_threshold, r1 <= p.dens_threshold)
  t11 = jnp.logical_or(0.1e1 - t5 <= p.zeta_threshold, t10)
  t14 = p.zeta_threshold - 0.1e1
  t17 = -t14
  t18 = jnp.where(0.1e1 - t4 <= p.zeta_threshold, t17, t4)
  t19 = jnp.where(0.1e1 + t4 <= p.zeta_threshold, t14, t18)
  t20 = t19 ** 2
  t29 = jnp.where(0.2e1 * r1 * t3 <= p.zeta_threshold, t17, t4)
  t30 = jnp.where(0.2e1 * r0 * t3 <= p.zeta_threshold, t14, t29)
  t31 = 0.1e1 + t30
  t35 = 3 ** (0.1e1 / 0.3e1)
  t36 = t35 ** 2
  t38 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t40 = t36 / t38
  t41 = 4 ** (0.1e1 / 0.3e1)
  t42 = 2 ** (0.1e1 / 0.3e1)
  t43 = t41 * t42
  t44 = t31 <= p.zeta_threshold
  t45 = 0.1e1 - t30
  t46 = t45 <= p.zeta_threshold
  t47 = jnp.where(t46, t17, t30)
  t48 = jnp.where(t44, t14, t47)
  t51 = ((0.1e1 + t48) * t2) ** (0.1e1 / 0.3e1)
  t56 = jnp.where(t31 * t2 / 0.2e1 <= p.dens_threshold, 0, t40 * t43 / t51 / 0.9e1)
  t61 = jnp.where(t44, t17, -t30)
  t62 = jnp.where(t46, t14, t61)
  t65 = ((0.1e1 + t62) * t2) ** (0.1e1 / 0.3e1)
  t70 = jnp.where(t45 * t2 / 0.2e1 <= p.dens_threshold, 0, t40 * t43 / t65 / 0.9e1)
  t71 = t56 + t70
  t73 = jnp.where(t71 == 0.e0, 2.220446049250313e-16, t71)
  t77 = t73 ** 2
  t78 = t77 ** 2
  res = jnp.where(t11, 0, -0.25e0 * (0.1e1 - t20) * t2 * (0.390299956e1 / t73 + 0.5764e0) / (0.433132090567376656e2 / t78 + 0.190514637481962976e2 / t77 / t73 + 0.2094820520028e1 / t77))
  return res

def unpol(r0, s0, params, p):
  t1 = 0.1e1 <= p.zeta_threshold
  t3 = r0 / 0.2e1 <= p.dens_threshold
  t4 = jnp.logical_and(t3, t3)
  t5 = jnp.logical_or(t1, t4)
  t6 = p.zeta_threshold - 0.1e1
  t7 = -t6
  t8 = jnp.where(t1, t7, 0)
  t9 = jnp.where(t1, t6, t8)
  t10 = t9 ** 2
  t13 = 0.1e1 + t9
  t17 = 3 ** (0.1e1 / 0.3e1)
  t18 = t17 ** 2
  t20 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t22 = t18 / t20
  t23 = 4 ** (0.1e1 / 0.3e1)
  t24 = 2 ** (0.1e1 / 0.3e1)
  t25 = t23 * t24
  t26 = t13 <= p.zeta_threshold
  t27 = 0.1e1 - t9
  t28 = t27 <= p.zeta_threshold
  t29 = jnp.where(t28, t7, t9)
  t30 = jnp.where(t26, t6, t29)
  t33 = ((0.1e1 + t30) * r0) ** (0.1e1 / 0.3e1)
  t38 = jnp.where(t13 * r0 / 0.2e1 <= p.dens_threshold, 0, t22 * t25 / t33 / 0.9e1)
  t43 = jnp.where(t26, t7, -t9)
  t44 = jnp.where(t28, t6, t43)
  t47 = ((0.1e1 + t44) * r0) ** (0.1e1 / 0.3e1)
  t52 = jnp.where(t27 * r0 / 0.2e1 <= p.dens_threshold, 0, t22 * t25 / t47 / 0.9e1)
  t53 = t38 + t52
  t55 = jnp.where(t53 == 0.e0, 2.220446049250313e-16, t53)
  t59 = t55 ** 2
  t60 = t59 ** 2
  res = jnp.where(t5, 0, -0.25e0 * (0.1e1 - t10) * r0 * (0.390299956e1 / t55 + 0.5764e0) / (0.433132090567376656e2 / t60 + 0.190514637481962976e2 / t59 / t55 + 0.2094820520028e1 / t59))
  return res