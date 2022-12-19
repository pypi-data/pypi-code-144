"""Generated from gga_x_pw86.mpl."""

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
  t30 = params.aa * t29
  t31 = jnp.pi ** 2
  t32 = t31 ** (0.1e1 / 0.3e1)
  t33 = t32 ** 2
  t34 = 0.1e1 / t33
  t36 = r0 ** 2
  t37 = r0 ** (0.1e1 / 0.3e1)
  t38 = t37 ** 2
  t44 = t29 ** 2
  t45 = params.bb * t44
  t47 = 0.1e1 / t32 / t31
  t48 = s0 ** 2
  t50 = t36 ** 2
  t57 = t31 ** 2
  t59 = params.cc / t57
  t61 = t50 ** 2
  t67 = (0.1e1 + t30 * t34 * s0 / t38 / t36 / 0.24e2 + t45 * t47 * t48 / t37 / t50 / r0 / 0.576e3 + t59 * t48 * s0 / t61 / 0.2304e4) ** (0.1e1 / 0.15e2)
  t71 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * t67)
  t73 = jnp.where(t10, t15, -t17)
  t74 = jnp.where(t14, t11, t73)
  t75 = 0.1e1 + t74
  t77 = t75 ** (0.1e1 / 0.3e1)
  t79 = jnp.where(t75 <= p.zeta_threshold, t23, t77 * t75)
  t82 = r1 ** 2
  t83 = r1 ** (0.1e1 / 0.3e1)
  t84 = t83 ** 2
  t90 = s2 ** 2
  t92 = t82 ** 2
  t100 = t92 ** 2
  t106 = (0.1e1 + t30 * t34 * s2 / t84 / t82 / 0.24e2 + t45 * t47 * t90 / t83 / t92 / r1 / 0.576e3 + t59 * t90 * s2 / t100 / 0.2304e4) ** (0.1e1 / 0.15e2)
  t110 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t79 * t27 * t106)
  res = t71 + t110
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
  t28 = 2 ** (0.1e1 / 0.3e1)
  t29 = t28 ** 2
  t31 = r0 ** 2
  t32 = t19 ** 2
  t38 = t21 ** 2
  t43 = s0 ** 2
  t45 = t31 ** 2
  t52 = t23 ** 2
  t56 = t45 ** 2
  t62 = (0.1e1 + params.aa * t21 / t25 * s0 * t29 / t32 / t31 / 0.24e2 + params.bb * t38 / t24 / t23 * t43 * t28 / t19 / t45 / r0 / 0.288e3 + params.cc / t52 * t43 * s0 / t56 / 0.576e3) ** (0.1e1 / 0.15e2)
  t66 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * t62)
  res = 0.2e1 * t66
  return res