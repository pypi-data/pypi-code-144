"""Generated from gga_x_airy.mpl."""

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
  t30 = t29 ** 2
  t31 = jnp.pi ** 2
  t32 = t31 ** (0.1e1 / 0.3e1)
  t34 = t30 / t32
  t35 = jnp.sqrt(s0)
  t36 = r0 ** (0.1e1 / 0.3e1)
  t40 = t34 * t35 / t36 / r0
  t41 = t40 ** 0.2626712e1
  t44 = (0.1e1 + 0.13471619689594796103e-3 * t41) ** (-0.657946e0)
  t47 = t40 ** 0.3217063e1
  t49 = t40 ** 0.3223476e1
  t52 = t40 ** 0.3473804e1
  t61 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.60146019220211109872e-4 * t41 * t44 + (0.1e1 - 0.45212413010769857073e-1 * t47 + 0.45402221956620378581e-1 * t49) / (0.1e1 + 0.47702180224903349918e-3 * t52)))
  t63 = jnp.where(t10, t15, -t17)
  t64 = jnp.where(t14, t11, t63)
  t65 = 0.1e1 + t64
  t67 = t65 ** (0.1e1 / 0.3e1)
  t69 = jnp.where(t65 <= p.zeta_threshold, t23, t67 * t65)
  t71 = jnp.sqrt(s2)
  t72 = r1 ** (0.1e1 / 0.3e1)
  t76 = t34 * t71 / t72 / r1
  t77 = t76 ** 0.2626712e1
  t80 = (0.1e1 + 0.13471619689594796103e-3 * t77) ** (-0.657946e0)
  t83 = t76 ** 0.3217063e1
  t85 = t76 ** 0.3223476e1
  t88 = t76 ** 0.3473804e1
  t97 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t69 * t27 * (0.60146019220211109872e-4 * t77 * t80 + (0.1e1 - 0.45212413010769857073e-1 * t83 + 0.45402221956620378581e-1 * t85) / (0.1e1 + 0.47702180224903349918e-3 * t88)))
  res = t61 + t97
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
  t22 = t21 ** 2
  t23 = jnp.pi ** 2
  t24 = t23 ** (0.1e1 / 0.3e1)
  t27 = jnp.sqrt(s0)
  t28 = 2 ** (0.1e1 / 0.3e1)
  t33 = t22 / t24 * t27 * t28 / t19 / r0
  t34 = t33 ** 0.2626712e1
  t37 = (0.1e1 + 0.13471619689594796103e-3 * t34) ** (-0.657946e0)
  t40 = t33 ** 0.3217063e1
  t42 = t33 ** 0.3223476e1
  t45 = t33 ** 0.3473804e1
  t54 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.60146019220211109872e-4 * t34 * t37 + (0.1e1 - 0.45212413010769857073e-1 * t40 + 0.45402221956620378581e-1 * t42) / (0.1e1 + 0.47702180224903349918e-3 * t45)))
  res = 0.2e1 * t54
  return res