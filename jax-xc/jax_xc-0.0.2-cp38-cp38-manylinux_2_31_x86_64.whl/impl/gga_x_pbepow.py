"""Generated from gga_x_pbepow.mpl."""

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
  t40 = s0 / t37 / t35
  t47 = (t34 * t40 / (0.91464571985215458336e0 * t34 * t40 + 0.804e0)) ** 0.1e3
  t57 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (0.1e1 - 0.91464571985215458336e-2 * t34 * t40 * (0.13344141567995010044e-3 * t47 - 0.1e1)))
  t59 = jnp.where(t10, t15, -t17)
  t60 = jnp.where(t14, t11, t59)
  t61 = 0.1e1 + t60
  t63 = t61 ** (0.1e1 / 0.3e1)
  t65 = jnp.where(t61 <= p.zeta_threshold, t23, t63 * t61)
  t67 = r1 ** 2
  t68 = r1 ** (0.1e1 / 0.3e1)
  t69 = t68 ** 2
  t72 = s2 / t69 / t67
  t79 = (t34 * t72 / (0.91464571985215458336e0 * t34 * t72 + 0.804e0)) ** 0.1e3
  t89 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t65 * t27 * (0.1e1 - 0.91464571985215458336e-2 * t34 * t72 * (0.13344141567995010044e-3 * t79 - 0.1e1)))
  res = t57 + t89
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
  t26 = t21 / t24
  t27 = t26 * s0
  t28 = 2 ** (0.1e1 / 0.3e1)
  t29 = t28 ** 2
  t30 = r0 ** 2
  t31 = t19 ** 2
  t33 = 0.1e1 / t31 / t30
  t34 = t29 * t33
  t43 = (t27 * t34 / (0.91464571985215458336e0 * t26 * s0 * t29 * t33 + 0.804e0)) ** 0.1e3
  t53 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (0.1e1 - 0.91464571985215458336e-2 * t27 * t34 * (0.13344141567995010044e-3 * t43 - 0.1e1)))
  res = 0.2e1 * t53
  return res