"""Generated from lda_c_vwn.mpl."""

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
  t7 = r0 + r1
  t8 = t7 ** (0.1e1 / 0.3e1)
  t10 = t6 / t8
  t11 = t4 * t10
  t12 = t11 / 0.4e1
  t13 = jnp.sqrt(t11)
  t16 = 0.1e1 / (t12 + 0.186372e1 * t13 + 0.129352e2)
  t20 = jnp.log(t4 * t10 * t16 / 0.4e1)
  t21 = 0.310907e-1 * t20
  t25 = jnp.arctan(0.61519908197590802322e1 / (t13 + 0.372744e1))
  t26 = 0.38783294878113014393e-1 * t25
  t27 = t13 / 0.2e1
  t29 = (t27 + 0.10498e0) ** 2
  t31 = jnp.log(t29 * t16)
  t32 = 0.96902277115443742139e-3 * t31
  t33 = jnp.pi ** 2
  t37 = 0.1e1 / (t12 + 0.565535e0 * t13 + 0.130045e2)
  t41 = jnp.log(t4 * t10 * t37 / 0.4e1)
  t45 = jnp.arctan(0.71231089178181179908e1 / (t13 + 0.113107e1))
  t48 = (t27 + 0.47584e-2) ** 2
  t50 = jnp.log(t48 * t37)
  t54 = r0 - r1
  t56 = t54 / t7
  t57 = 0.1e1 + t56
  t59 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t60 = t59 * p.zeta_threshold
  t61 = t57 ** (0.1e1 / 0.3e1)
  t63 = jnp.where(t57 <= p.zeta_threshold, t60, t61 * t57)
  t64 = 0.1e1 - t56
  t66 = t64 ** (0.1e1 / 0.3e1)
  t68 = jnp.where(t64 <= p.zeta_threshold, t60, t66 * t64)
  t69 = t63 + t68 - 0.2e1
  t71 = 2 ** (0.1e1 / 0.3e1)
  t72 = t71 - 0.1e1
  t74 = 0.1e1 / t72 / 0.2e1
  t75 = t54 ** 2
  t76 = t75 ** 2
  t77 = t7 ** 2
  t78 = t77 ** 2
  t79 = 0.1e1 / t78
  t89 = 0.1e1 / (t12 + 0.353021e1 * t13 + 0.180578e2)
  t93 = jnp.log(t4 * t10 * t89 / 0.4e1)
  t98 = jnp.arctan(0.473092690956011283e1 / (t13 + 0.706042e1))
  t101 = (t27 + 0.325e0) ** 2
  t103 = jnp.log(t101 * t89)
  res = t21 + t26 + t32 - 0.3e1 / 0.8e1 / t33 * (t41 + 0.317708004743941464e0 * t45 + 0.41403379428206274608e-3 * t50) * t69 * t74 * (-t76 * t79 + 0.1e1) * t72 + (0.1554535e-1 * t93 + 0.52491393169780936218e-1 * t98 + 0.22478670955426118383e-2 * t103 - t21 - t26 - t32) * t69 * t74 * t76 * t79
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
  t12 = jnp.sqrt(t10)
  t15 = 0.1e1 / (t11 + 0.186372e1 * t12 + 0.129352e2)
  t19 = jnp.log(t4 * t9 * t15 / 0.4e1)
  t24 = jnp.arctan(0.61519908197590802322e1 / (t12 + 0.372744e1))
  t26 = t12 / 0.2e1
  t28 = (t26 + 0.10498e0) ** 2
  t30 = jnp.log(t28 * t15)
  t32 = jnp.pi ** 2
  t36 = 0.1e1 / (t11 + 0.565535e0 * t12 + 0.130045e2)
  t40 = jnp.log(t4 * t9 * t36 / 0.4e1)
  t44 = jnp.arctan(0.71231089178181179908e1 / (t12 + 0.113107e1))
  t47 = (t26 + 0.47584e-2) ** 2
  t49 = jnp.log(t47 * t36)
  t54 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t56 = jnp.where(0.1e1 <= p.zeta_threshold, t54 * p.zeta_threshold, 1)
  t59 = 2 ** (0.1e1 / 0.3e1)
  t60 = t59 - 0.1e1
  res = 0.310907e-1 * t19 + 0.38783294878113014393e-1 * t24 + 0.96902277115443742139e-3 * t30 - 0.1e1 / t32 * (t40 + 0.317708004743941464e0 * t44 + 0.41403379428206274608e-3 * t49) * (0.9e1 * t56 - 0.9e1) / 0.24e2
  return res