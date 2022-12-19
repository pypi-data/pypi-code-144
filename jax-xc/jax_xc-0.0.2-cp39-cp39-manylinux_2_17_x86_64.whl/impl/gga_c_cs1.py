"""Generated from gga_c_cs1.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t1 = r0 - r1
  t2 = t1 ** 2
  t3 = r0 + r1
  t4 = t3 ** 2
  t8 = t3 ** (0.1e1 / 0.3e1)
  t15 = s0 + 0.2e1 * s1 + s2
  t16 = t15 ** 2
  t17 = t4 ** 2
  t22 = t8 ** 2
  t28 = (0.1e1 + 0.6e-2 * t15 / t22 / t4) ** 2
  t36 = t1 / t3
  t37 = 0.1e1 + t36
  t39 = jnp.where(t37 <= p.zeta_threshold, p.zeta_threshold, t37)
  t40 = r0 ** (0.1e1 / 0.3e1)
  t44 = s0 ** 2
  t45 = r0 ** 2
  t46 = t45 ** 2
  t51 = t40 ** 2
  t57 = (0.1e1 + 0.6e-2 * s0 / t51 / t45) ** 2
  t65 = 0.1e1 - t36
  t67 = jnp.where(t65 <= p.zeta_threshold, p.zeta_threshold, t65)
  t68 = r1 ** (0.1e1 / 0.3e1)
  t72 = s2 ** 2
  t73 = r1 ** 2
  t74 = t73 ** 2
  t79 = t68 ** 2
  t85 = (0.1e1 + 0.6e-2 * s2 / t79 / t73) ** 2
  res = (0.1e1 - t2 / t4) / (0.1e1 + 0.349e0 / t8) * (-0.159068e0 + 0.286308e-6 * t16 / t8 / t17 / t3 / t28) / 0.4e1 + t39 * t40 / (t40 + 0.349e0) * (-0.18897e-1 + 0.558864e-5 * t44 / t40 / t46 / r0 / t57) / 0.2e1 + t67 * t68 / (t68 + 0.349e0) * (-0.18897e-1 + 0.558864e-5 * t72 / t68 / t74 / r1 / t85) / 0.2e1
  return res

def unpol(r0, s0, params, p):
  t1 = r0 ** (0.1e1 / 0.3e1)
  t6 = s0 ** 2
  t7 = r0 ** 2
  t8 = t7 ** 2
  t11 = 0.1e1 / t1 / t8 / r0
  t13 = t1 ** 2
  t15 = 0.1e1 / t13 / t7
  t19 = (0.1e1 + 0.6e-2 * s0 * t15) ** 2
  t27 = jnp.where(0.1e1 <= p.zeta_threshold, p.zeta_threshold, 1)
  t28 = 2 ** (0.1e1 / 0.3e1)
  t29 = t28 ** 2
  t41 = (0.1e1 + 0.6e-2 * s0 * t29 * t15) ** 2
  res = 0.1e1 / (0.1e1 + 0.349e0 / t1) * (-0.159068e0 + 0.286308e-6 * t6 * t11 / t19) / 0.4e1 + t27 * t29 * t1 / (t29 * t1 / 0.2e1 + 0.349e0) * (-0.18897e-1 + 0.1117728e-4 * t6 * t28 * t11 / t41) / 0.2e1
  return res