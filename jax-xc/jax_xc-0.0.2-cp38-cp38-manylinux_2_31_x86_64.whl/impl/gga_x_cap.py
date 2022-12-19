"""Generated from gga_x_cap.mpl."""

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
  t32 = jnp.pi ** 2
  t33 = t32 ** (0.1e1 / 0.3e1)
  t34 = 0.1e1 / t33
  t35 = params.alphaoAx * t30 * t34
  t36 = jnp.sqrt(s0)
  t37 = r0 ** (0.1e1 / 0.3e1)
  t40 = t36 / t37 / r0
  t41 = t30 * t34
  t45 = jnp.log(0.1e1 + t41 * t40 / 0.12e2)
  t57 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 - t35 * t40 * t45 / (params.c * t45 + 0.1e1) / 0.12e2))
  t59 = jnp.where(t10, t15, -t17)
  t60 = jnp.where(t14, t11, t59)
  t61 = 0.1e1 + t60
  t63 = t61 ** (0.1e1 / 0.3e1)
  t65 = jnp.where(t61 <= p.zeta_threshold, t23, t63 * t61)
  t67 = jnp.sqrt(s2)
  t68 = r1 ** (0.1e1 / 0.3e1)
  t71 = t67 / t68 / r1
  t75 = jnp.log(0.1e1 + t41 * t71 / 0.12e2)
  t87 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t65 * t27 * (0.1e1 - t35 * t71 * t75 / (params.c * t75 + 0.1e1) / 0.12e2))
  res = t57 + t87
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
  t24 = jnp.pi ** 2
  t25 = t24 ** (0.1e1 / 0.3e1)
  t26 = 0.1e1 / t25
  t27 = jnp.sqrt(s0)
  t30 = 2 ** (0.1e1 / 0.3e1)
  t32 = 0.1e1 / t19 / r0
  t40 = jnp.log(0.1e1 + t22 * t26 * t27 * t30 * t32 / 0.12e2)
  t52 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 - params.alphaoAx * t22 * t26 * t27 * t30 * t32 * t40 / (params.c * t40 + 0.1e1) / 0.12e2))
  res = 0.2e1 * t52
  return res