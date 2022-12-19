"""Generated from lda_k_zlp.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t2 = t1 ** 2
  t4 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t7 = 4 ** (0.1e1 / 0.3e1)
  t10 = r0 + r1
  t12 = (r0 - r1) / t10
  t13 = 0.1e1 + t12
  t15 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t16 = t15 ** 2
  t17 = t16 * p.zeta_threshold
  t18 = t13 ** (0.1e1 / 0.3e1)
  t19 = t18 ** 2
  t21 = jnp.where(t13 <= p.zeta_threshold, t17, t19 * t13)
  t22 = 0.1e1 - t12
  t24 = t22 ** (0.1e1 / 0.3e1)
  t25 = t24 ** 2
  t27 = jnp.where(t22 <= p.zeta_threshold, t17, t25 * t22)
  t30 = t10 ** (0.1e1 / 0.3e1)
  t31 = t30 ** 2
  t36 = jnp.log(0.1e1 + 0.5102040816326530612e3 / t30)
  res = 0.10790666666666666667e1 * t2 / t4 * t7 * (t21 / 0.2e1 + t27 / 0.2e1) * t31 * (0.1e1 - 0.196e-2 * t30 * t36)
  return res

def unpol(r0, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t2 = t1 ** 2
  t4 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t7 = 4 ** (0.1e1 / 0.3e1)
  t10 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t11 = t10 ** 2
  t13 = jnp.where(0.1e1 <= p.zeta_threshold, t11 * p.zeta_threshold, 1)
  t14 = r0 ** (0.1e1 / 0.3e1)
  t15 = t14 ** 2
  t20 = jnp.log(0.1e1 + 0.5102040816326530612e3 / t14)
  res = 0.10790666666666666667e1 * t2 / t4 * t7 * t13 * t15 * (0.1e1 - 0.196e-2 * t14 * t20)
  return res