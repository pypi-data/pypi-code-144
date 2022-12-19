"""Generated from gga_x_mpbe.mpl."""

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
  t31 = jnp.pi ** 2
  t32 = t31 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t34 = 0.1e1 / t33
  t35 = params.c1 * t29 * t34
  t36 = r0 ** 2
  t37 = r0 ** (0.1e1 / 0.3e1)
  t38 = t37 ** 2
  t40 = 0.1e1 / t38 / t36
  t42 = params.a * t29
  t47 = 0.1e1 + t42 * t34 * s0 * t40 / 0.24e2
  t52 = t29 ** 2
  t56 = params.c2 * t52 / t32 / t31
  t57 = s0 ** 2
  t58 = t36 ** 2
  t63 = t47 ** 2
  t68 = t31 ** 2
  t70 = params.c3 / t68
  t72 = t58 ** 2
  t84 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 + t35 * s0 * t40 / t47 / 0.24e2 + t56 * t57 / t37 / t58 / r0 / t63 / 0.576e3 + t70 * t57 * s0 / t72 / t63 / t47 / 0.2304e4))
  t86 = jnp.where(t10, t15, -t17)
  t87 = jnp.where(t14, t11, t86)
  t88 = 0.1e1 + t87
  t90 = t88 ** (0.1e1 / 0.3e1)
  t92 = jnp.where(t88 <= p.zeta_threshold, t23, t90 * t88)
  t94 = r1 ** 2
  t95 = r1 ** (0.1e1 / 0.3e1)
  t96 = t95 ** 2
  t98 = 0.1e1 / t96 / t94
  t104 = 0.1e1 + t42 * t34 * s2 * t98 / 0.24e2
  t109 = s2 ** 2
  t110 = t94 ** 2
  t115 = t104 ** 2
  t121 = t110 ** 2
  t133 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t92 * t27 * (0.1e1 + t35 * s2 * t98 / t104 / 0.24e2 + t56 * t109 / t95 / t110 / r1 / t115 / 0.576e3 + t70 * t109 * s2 / t121 / t115 / t104 / 0.2304e4))
  res = t84 + t133
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
  t23 = jnp.pi ** 2
  t24 = t23 ** (0.1e1 / 0.3e1)
  t25 = t24 ** 2
  t26 = 0.1e1 / t25
  t28 = 2 ** (0.1e1 / 0.3e1)
  t29 = t28 ** 2
  t30 = s0 * t29
  t31 = r0 ** 2
  t32 = t19 ** 2
  t34 = 0.1e1 / t32 / t31
  t40 = 0.1e1 + params.a * t21 * t26 * t30 * t34 / 0.24e2
  t46 = t21 ** 2
  t51 = s0 ** 2
  t53 = t31 ** 2
  t57 = t40 ** 2
  t63 = t23 ** 2
  t67 = t53 ** 2
  t79 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 + params.c1 * t21 * t26 * t30 * t34 / t40 / 0.24e2 + params.c2 * t46 / t24 / t23 * t51 * t28 / t19 / t53 / r0 / t57 / 0.288e3 + params.c3 / t63 * t51 * s0 / t67 / t57 / t40 / 0.576e3))
  res = 0.2e1 * t79
  return res