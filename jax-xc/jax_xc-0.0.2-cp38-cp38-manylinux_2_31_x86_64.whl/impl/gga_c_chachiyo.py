"""Generated from gga_c_chachiyo.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t2 = t1 ** 2
  t5 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t7 = 4 ** (0.1e1 / 0.3e1)
  t9 = r0 + r1
  t10 = t9 ** (0.1e1 / 0.3e1)
  t11 = 0.1e1 / t5 * t7 * t10
  t15 = t5 ** 2
  t17 = t7 ** 2
  t19 = t10 ** 2
  t20 = 0.1e1 / t15 * t17 * t19
  t24 = jnp.log(0.1e1 + params.bp * t2 * t11 / 0.3e1 + params.cp * t1 * t20 / 0.3e1)
  t25 = params.ap * t24
  t33 = jnp.log(0.1e1 + params.bf * t2 * t11 / 0.3e1 + params.cf * t1 * t20 / 0.3e1)
  t38 = (r0 - r1) / t9
  t39 = 0.1e1 + t38
  t41 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t42 = t41 ** 2
  t43 = t39 ** (0.1e1 / 0.3e1)
  t44 = t43 ** 2
  t45 = jnp.where(t39 <= p.zeta_threshold, t42, t44)
  t46 = 0.1e1 - t38
  t48 = t46 ** (0.1e1 / 0.3e1)
  t49 = t48 ** 2
  t50 = jnp.where(t46 <= p.zeta_threshold, t42, t49)
  t52 = t45 / 0.2e1 + t50 / 0.2e1
  t53 = t52 ** 2
  t58 = t25 + (params.af * t33 - t25) * (-0.2e1 * t53 * t52 + 0.2e1)
  t59 = jnp.pi ** (0.1e1 / 0.3e1)
  t61 = t9 ** 2
  t72 = (0.1e1 + t2 * t59 / t10 / t61 * (s0 + 0.2e1 * s1 + s2) / 0.48e2) ** (params.h / t58)
  res = t58 * t72
  return res

def unpol(r0, s0, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t2 = t1 ** 2
  t5 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t7 = 4 ** (0.1e1 / 0.3e1)
  t9 = r0 ** (0.1e1 / 0.3e1)
  t10 = 0.1e1 / t5 * t7 * t9
  t14 = t5 ** 2
  t16 = t7 ** 2
  t18 = t9 ** 2
  t19 = 0.1e1 / t14 * t16 * t18
  t23 = jnp.log(0.1e1 + params.bp * t2 * t10 / 0.3e1 + params.cp * t1 * t19 / 0.3e1)
  t24 = params.ap * t23
  t32 = jnp.log(0.1e1 + params.bf * t2 * t10 / 0.3e1 + params.cf * t1 * t19 / 0.3e1)
  t36 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t37 = t36 ** 2
  t38 = jnp.where(0.1e1 <= p.zeta_threshold, t37, 1)
  t39 = t38 ** 2
  t44 = t24 + (params.af * t32 - t24) * (-0.2e1 * t39 * t38 + 0.2e1)
  t45 = jnp.pi ** (0.1e1 / 0.3e1)
  t47 = r0 ** 2
  t56 = (0.1e1 + t2 * t45 / t9 / t47 * s0 / 0.48e2) ** (params.h / t44)
  res = t44 * t56
  return res