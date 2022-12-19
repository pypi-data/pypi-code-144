"""Generated from gga_x_sg4.mpl."""

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
  t44 = t29 ** 2
  t45 = t30 ** 2
  t49 = t44 / t31 / t45 / t30
  t50 = s0 ** 2
  t51 = t50 ** 2
  t53 = t35 ** 2
  t55 = t53 ** 2
  t74 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1804e1 - 0.56028717948717948718e0 * (0.1e1 - 0.3123398257303946694e-2 * t41) / (0.1e1 - 0.17835614159590036509e-11 * t49 * t51 * s0 / t36 / t55 / t53 / r0) - 0.24371282051282051282e0 / (0.1e1 + 0.37270642201834862386e-1 * t41)))
  t76 = jnp.where(t10, t15, -t17)
  t77 = jnp.where(t14, t11, t76)
  t78 = 0.1e1 + t77
  t80 = t78 ** (0.1e1 / 0.3e1)
  t82 = jnp.where(t78 <= p.zeta_threshold, t23, t80 * t78)
  t84 = r1 ** 2
  t85 = r1 ** (0.1e1 / 0.3e1)
  t86 = t85 ** 2
  t90 = t34 * s2 / t86 / t84
  t93 = s2 ** 2
  t94 = t93 ** 2
  t96 = t84 ** 2
  t98 = t96 ** 2
  t117 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t82 * t27 * (0.1804e1 - 0.56028717948717948718e0 * (0.1e1 - 0.3123398257303946694e-2 * t90) / (0.1e1 - 0.17835614159590036509e-11 * t49 * t94 * s2 / t85 / t98 / t96 / r1) - 0.24371282051282051282e0 / (0.1e1 + 0.37270642201834862386e-1 * t90)))
  res = t74 + t117
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
  t38 = t21 ** 2
  t39 = t22 ** 2
  t44 = s0 ** 2
  t45 = t44 ** 2
  t48 = t30 ** 2
  t50 = t48 ** 2
  t69 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1804e1 - 0.56028717948717948718e0 * (0.1e1 - 0.3123398257303946694e-2 * t35) / (0.1e1 - 0.14268491327672029207e-10 * t38 / t23 / t39 / t22 * t45 * s0 * t27 / t19 / t50 / t48 / r0) - 0.24371282051282051282e0 / (0.1e1 + 0.37270642201834862386e-1 * t35)))
  res = 0.2e1 * t69
  return res