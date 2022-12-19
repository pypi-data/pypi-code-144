"""Generated from lda_c_gk72.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t3 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t4 = t1 * t3
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t8 = (r0 + r1) ** (0.1e1 / 0.3e1)
  t10 = t6 / t8
  t11 = t4 * t10
  t12 = t11 / 0.4e1
  t14 = jnp.log(t12)
  t24 = t1 ** 2
  t30 = jnp.sqrt(0.4e1)
  t31 = jnp.sqrt(t11)
  t36 = t3 ** 2
  t39 = t8 ** 2
  t53 = jnp.where(t12 < 0.1e2, -0.6156e-1 + 0.1898e-1 * t14, 0.146e0 * t24 / t3 * t5 * t8 + 0.53e1 * t30 / t31 / t11 - 0.49e0 * t1 / t36 * t6 * t39 - 0.16e1 * t30 / t31 / t24 / t36 / t5 * t39)
  res = jnp.where(t12 < 0.7e0, 0.311e-1 * t14 - 0.48e-1 + 0.225e-2 * t4 * t10 * t14 - 0.425e-2 * t11, t53)
  return res

def unpol(r0, params, p):
  t1 = 3 ** (0.1e1 / 0.3e1)
  t3 = (0.1e1 / jnp.pi) ** (0.1e1 / 0.3e1)
  t4 = t1 * t3
  t5 = 4 ** (0.1e1 / 0.3e1)
  t6 = t5 ** 2
  t7 = r0 ** (0.1e1 / 0.3e1)
  t9 = t6 / t7
  t10 = t4 * t9
  t11 = t10 / 0.4e1
  t13 = jnp.log(t11)
  t23 = t1 ** 2
  t29 = jnp.sqrt(0.4e1)
  t30 = jnp.sqrt(t10)
  t35 = t3 ** 2
  t38 = t7 ** 2
  t52 = jnp.where(t11 < 0.1e2, -0.6156e-1 + 0.1898e-1 * t13, 0.146e0 * t23 / t3 * t5 * t7 + 0.53e1 * t29 / t30 / t10 - 0.49e0 * t1 / t35 * t6 * t38 - 0.16e1 * t29 / t30 / t23 / t35 / t5 * t38)
  res = jnp.where(t11 < 0.7e0, 0.311e-1 * t13 - 0.48e-1 + 0.225e-2 * t4 * t9 * t13 - 0.425e-2 * t10, t52)
  return res