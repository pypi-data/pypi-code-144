"""Generated from mgga_x_mbeef.mpl."""

import jax
import jax.numpy as jnp
from jax.numpy import array as array
from jax.numpy import int32 as int32
from jax.numpy import nan as nan
from typing import Callable


def pol(r0, r1, s0, s1, s2, l0, l1, tau0, tau1, params, p):
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
  t20 = t19 + 0.1e1
  t22 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t23 = t22 * p.zeta_threshold
  t24 = t20 ** (0.1e1 / 0.3e1)
  t26 = jnp.where(t20 <= p.zeta_threshold, t23, t24 * t20)
  t27 = t6 ** (0.1e1 / 0.3e1)
  t29 = 6 ** (0.1e1 / 0.3e1)
  t30 = jnp.pi ** 2
  t31 = t30 ** (0.1e1 / 0.3e1)
  t32 = t31 ** 2
  t33 = 0.1e1 / t32
  t34 = t29 * t33
  t35 = r0 ** 2
  t36 = r0 ** (0.1e1 / 0.3e1)
  t37 = t36 ** 2
  t40 = s0 / t37 / t35
  t46 = t34 * t40 / (0.65124e1 + t34 * t40 / 0.24e2)
  t48 = t46 / 0.12e2 - 0.1e1
  t49 = t48 ** 2
  t51 = t49 ** 2
  t53 = t51 * t49
  t62 = 0.5e1 / 0.9e1 * (tau0 / t37 / r0 - t40 / 0.8e1) * t29 * t33
  t64 = 0.1e5 < t62
  t65 = jnp.where(t64, t62, 0.1e5)
  t66 = t65 ** 2
  t71 = t66 ** 2
  t75 = jnp.where(t64, 0.1e5, t62)
  t76 = t75 ** 2
  t77 = 0.1e1 - t76
  t78 = t77 ** 2
  t80 = t76 * t75
  t86 = jnp.where(0.1e5 <= t62, 0.1e1 - 0.3e1 / t66 - 0.1e1 / t66 / t65 + 0.3e1 / t71, -t78 * t77 / (0.1e1 + t80 * (0.1e1 + t80)))
  t87 = t86 ** 2
  t88 = t87 ** 2
  t89 = t88 * t87
  t94 = t88 * t86
  t96 = t87 * t86
  t98 = t88 * t96
  t100 = t49 * t48
  t102 = t51 * t48
  t104 = t51 * t100
  t107 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t49
  t111 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t89 - 0.315e3 / 0.16e2 * t88 + 0.105e3 / 0.16e2 * t87
  t118 = 0.429e3 / 0.16e2 * t98 - 0.693e3 / 0.16e2 * t94 + 0.315e3 / 0.16e2 * t96 - 0.35e2 / 0.16e2 * t86
  t123 = 0.5e1 / 0.2e1 * t100 - t46 / 0.8e1 + 0.3e1 / 0.2e1
  t126 = -0.92294814328125e-1 * t49 - 0.138056183978125e0 * t51 + 0.80024660533125e-1 * t53 - 0.80008813355625e-4 * t89 + 0.3020715669803125e-2 * t88 + 0.7031826877565625e-2 * t87 - 0.4373652639371875e-2 * t86 - 0.945883103563125e-3 * t94 + 0.4646102821846875e-2 * t96 + 0.19735677658125e-4 * t98 + 0.497944638409375e0 * t100 - 0.395061199588125e0 * t102 + 0.106025815520625e0 * t104 + 0.668980219e-8 * t107 * t111 - 0.223014657e-8 * t107 * t118 - 0.182177954e-1 * t123 * t86
  t130 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t87
  t136 = 0.63e2 / 0.8e1 * t94 - 0.35e2 / 0.4e1 * t96 + 0.15e2 / 0.8e1 * t86
  t141 = 0.5e1 / 0.2e1 * t96 - 0.3e1 / 0.2e1 * t86
  t150 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t88 - 0.15e2 / 0.4e1 * t87
  t172 = 0.63e2 / 0.8e1 * t102 - 0.35e2 / 0.4e1 * t100 + 0.5e1 / 0.32e2 * t46 - 0.15e2 / 0.8e1
  t175 = 0.100339208e0 * t48 * t86 - 0.879090772e-2 * t48 * t130 + 0.896739466e-3 * t123 * t136 - 0.845508103e-2 * t123 * t141 + 0.280678872e-1 * t123 * t130 - 0.303347141e-2 * t48 * t141 + 0.119130546e-2 * t48 * t150 + 0.822139896e-3 * t48 * t136 - 0.514204676e-4 * t48 * t111 - 0.940351563e-5 * t48 * t118 - 0.43464346e-1 * t107 * t86 - 0.150103636e-1 * t107 * t130 + 0.293253041e-2 * t107 * t141 + 0.182906057e-2 * t107 * t150 - 0.35104103e-3 * t107 * t136 - 0.188495102e-1 * t172 * t130
  t181 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t51 - 0.15e2 / 0.4e1 * t49
  t205 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t53 - 0.315e3 / 0.16e2 * t51 + 0.105e3 / 0.16e2 * t49
  t216 = -0.884148272e-2 * t172 * t86 + 0.912223751e-8 * t181 * t111 - 0.493824365e-8 * t181 * t118 + 0.209603871e-7 * t181 * t136 - 0.790811707e-7 * t181 * t150 + 0.631891628e-2 * t181 * t141 + 0.162638575e-1 * t181 * t86 - 0.182911291e-1 * t181 * t130 + 0.674910119e-8 * t123 * t118 - 0.216860568e-7 * t123 * t111 + 0.339308972e-2 * t123 * t150 - 0.265114646e-7 * t205 * t141 - 0.957417512e-2 * t205 * t86 + 0.169805915e-6 * t205 * t130 + 0.850272392e-8 * t172 * t118 - 0.138472194e-7 * t172 * t111
  t227 = 0.429e3 / 0.16e2 * t104 - 0.693e3 / 0.16e2 * t102 + 0.315e3 / 0.16e2 * t100 - 0.35e2 / 0.192e3 * t46 + 0.35e2 / 0.16e2
  t251 = 0.1380567225218996875e1 + 0.162238741e-6 * t172 * t150 - 0.376702959e-7 * t172 * t136 - 0.896771404e-2 * t172 * t141 + 0.554588743e-7 * t227 * t150 + 0.505920757e-7 * t227 * t141 - 0.27652468e-6 * t227 * t130 + 0.940675747e-2 * t227 * t86 + 0.694482484e-8 * t205 * t111 - 0.691592964e-8 * t205 * t118 + 0.236391411e-7 * t205 * t136 - 0.416393106e-7 * t205 * t150 + 0.888525527e-8 * t227 * t118 - 0.338128188e-7 * t227 * t136 - 0.774224962e-8 * t227 * t111 - 0.13022208355989583333e-1 * t46
  t257 = jnp.where(r0 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t26 * t27 * (t126 + t175 + t216 + t251))
  t259 = jnp.where(t10, t15, -t17)
  t260 = jnp.where(t14, t11, t259)
  t261 = t260 + 0.1e1
  t263 = t261 ** (0.1e1 / 0.3e1)
  t265 = jnp.where(t261 <= p.zeta_threshold, t23, t263 * t261)
  t267 = r1 ** 2
  t268 = r1 ** (0.1e1 / 0.3e1)
  t269 = t268 ** 2
  t272 = s2 / t269 / t267
  t278 = t34 * t272 / (0.65124e1 + t34 * t272 / 0.24e2)
  t280 = t278 / 0.12e2 - 0.1e1
  t281 = t280 ** 2
  t282 = t281 ** 2
  t285 = t282 * t281
  t294 = 0.5e1 / 0.9e1 * (tau1 / t269 / r1 - t272 / 0.8e1) * t29 * t33
  t296 = 0.1e5 < t294
  t297 = jnp.where(t296, t294, 0.1e5)
  t298 = t297 ** 2
  t303 = t298 ** 2
  t307 = jnp.where(t296, 0.1e5, t294)
  t308 = t307 ** 2
  t309 = 0.1e1 - t308
  t310 = t309 ** 2
  t312 = t308 * t307
  t318 = jnp.where(0.1e5 <= t294, 0.1e1 - 0.3e1 / t298 - 0.1e1 / t298 / t297 + 0.3e1 / t303, -t310 * t309 / (0.1e1 + t312 * (0.1e1 + t312)))
  t319 = t318 ** 2
  t320 = t319 ** 2
  t321 = t320 * t319
  t326 = t320 * t318
  t328 = t319 * t318
  t330 = t320 * t328
  t332 = t282 * t280
  t334 = t281 * t280
  t336 = t282 * t334
  t342 = 0.429e3 / 0.16e2 * t330 - 0.693e3 / 0.16e2 * t326 + 0.315e3 / 0.16e2 * t328 - 0.35e2 / 0.16e2 * t318
  t348 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t321 - 0.315e3 / 0.16e2 * t320 + 0.105e3 / 0.16e2 * t319
  t353 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t320 - 0.15e2 / 0.4e1 * t319
  t356 = -0.138056183978125e0 * t282 - 0.92294814328125e-1 * t281 + 0.80024660533125e-1 * t285 - 0.80008813355625e-4 * t321 + 0.3020715669803125e-2 * t320 + 0.7031826877565625e-2 * t319 - 0.4373652639371875e-2 * t318 - 0.945883103563125e-3 * t326 + 0.4646102821846875e-2 * t328 + 0.19735677658125e-4 * t330 - 0.395061199588125e0 * t332 + 0.497944638409375e0 * t334 + 0.106025815520625e0 * t336 - 0.940351563e-5 * t280 * t342 - 0.514204676e-4 * t280 * t348 + 0.119130546e-2 * t280 * t353
  t360 = 0.63e2 / 0.8e1 * t326 - 0.35e2 / 0.4e1 * t328 + 0.15e2 / 0.8e1 * t318
  t365 = 0.5e1 / 0.2e1 * t328 - 0.3e1 / 0.2e1 * t318
  t369 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t319
  t376 = 0.5e1 / 0.2e1 * t334 - t278 / 0.8e1 + 0.3e1 / 0.2e1
  t392 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t281
  t403 = 0.822139896e-3 * t280 * t360 - 0.303347141e-2 * t280 * t365 - 0.879090772e-2 * t280 * t369 + 0.100339208e0 * t280 * t318 + 0.674910119e-8 * t376 * t342 - 0.216860568e-7 * t376 * t348 + 0.896739466e-3 * t376 * t360 - 0.845508103e-2 * t376 * t365 + 0.339308972e-2 * t376 * t353 + 0.280678872e-1 * t376 * t369 - 0.182177954e-1 * t376 * t318 + 0.668980219e-8 * t392 * t348 - 0.223014657e-8 * t392 * t342 - 0.35104103e-3 * t392 * t360 + 0.182906057e-2 * t392 * t353 + 0.293253041e-2 * t392 * t365
  t412 = 0.63e2 / 0.8e1 * t332 - 0.35e2 / 0.4e1 * t334 + 0.5e1 / 0.32e2 * t278 - 0.15e2 / 0.8e1
  t421 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t282 - 0.15e2 / 0.4e1 * t281
  t439 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t285 - 0.315e3 / 0.16e2 * t282 + 0.105e3 / 0.16e2 * t281
  t448 = -0.43464346e-1 * t392 * t318 - 0.150103636e-1 * t392 * t369 + 0.162238741e-6 * t412 * t353 - 0.188495102e-1 * t412 * t369 - 0.884148272e-2 * t412 * t318 + 0.912223751e-8 * t421 * t348 - 0.493824365e-8 * t421 * t342 + 0.209603871e-7 * t421 * t360 - 0.790811707e-7 * t421 * t353 + 0.631891628e-2 * t421 * t365 + 0.162638575e-1 * t421 * t318 - 0.182911291e-1 * t421 * t369 - 0.416393106e-7 * t439 * t353 - 0.265114646e-7 * t439 * t365 - 0.957417512e-2 * t439 * t318 + 0.169805915e-6 * t439 * t369
  t461 = 0.429e3 / 0.16e2 * t336 - 0.693e3 / 0.16e2 * t332 + 0.315e3 / 0.16e2 * t334 - 0.35e2 / 0.192e3 * t278 + 0.35e2 / 0.16e2
  t483 = 0.1380567225218996875e1 + 0.850272392e-8 * t412 * t342 - 0.138472194e-7 * t412 * t348 - 0.376702959e-7 * t412 * t360 - 0.896771404e-2 * t412 * t365 + 0.554588743e-7 * t461 * t353 - 0.338128188e-7 * t461 * t360 + 0.505920757e-7 * t461 * t365 - 0.27652468e-6 * t461 * t369 + 0.940675747e-2 * t461 * t318 + 0.694482484e-8 * t439 * t348 - 0.691592964e-8 * t439 * t342 + 0.236391411e-7 * t439 * t360 + 0.888525527e-8 * t461 * t342 - 0.774224962e-8 * t461 * t348 - 0.13022208355989583333e-1 * t278
  t489 = jnp.where(r1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t5 * t265 * t27 * (t356 + t403 + t448 + t483))
  res = t257 + t489
  return res

def unpol(r0, s0, l0, tau0, params, p):
  t3 = 3 ** (0.1e1 / 0.3e1)
  t4 = jnp.pi ** (0.1e1 / 0.3e1)
  t7 = 0.1e1 <= p.zeta_threshold
  t8 = p.zeta_threshold - 0.1e1
  t10 = jnp.where(t7, -t8, 0)
  t11 = jnp.where(t7, t8, t10)
  t12 = t11 + 0.1e1
  t14 = p.zeta_threshold ** (0.1e1 / 0.3e1)
  t16 = t12 ** (0.1e1 / 0.3e1)
  t18 = jnp.where(t12 <= p.zeta_threshold, t14 * p.zeta_threshold, t16 * t12)
  t19 = r0 ** (0.1e1 / 0.3e1)
  t21 = 6 ** (0.1e1 / 0.3e1)
  t22 = jnp.pi ** 2
  t23 = t22 ** (0.1e1 / 0.3e1)
  t24 = t23 ** 2
  t25 = 0.1e1 / t24
  t26 = t21 * t25
  t28 = 2 ** (0.1e1 / 0.3e1)
  t29 = t28 ** 2
  t30 = r0 ** 2
  t31 = t19 ** 2
  t33 = 0.1e1 / t31 / t30
  t36 = s0 * t29 * t33
  t42 = t26 * s0 * t29 * t33 / (0.65124e1 + t26 * t36 / 0.24e2)
  t44 = t42 / 0.12e2 - 0.1e1
  t45 = t44 ** 2
  t46 = t45 ** 2
  t49 = t46 * t45
  t59 = 0.5e1 / 0.9e1 * (tau0 * t29 / t31 / r0 - t36 / 0.8e1) * t21 * t25
  t61 = 0.1e5 < t59
  t62 = jnp.where(t61, t59, 0.1e5)
  t63 = t62 ** 2
  t68 = t63 ** 2
  t72 = jnp.where(t61, 0.1e5, t59)
  t73 = t72 ** 2
  t74 = 0.1e1 - t73
  t75 = t74 ** 2
  t77 = t73 * t72
  t83 = jnp.where(0.1e5 <= t59, 0.1e1 - 0.3e1 / t63 - 0.1e1 / t63 / t62 + 0.3e1 / t68, -t75 * t74 / (0.1e1 + t77 * (0.1e1 + t77)))
  t84 = t83 ** 2
  t85 = t84 ** 2
  t86 = t85 * t84
  t91 = t85 * t83
  t93 = t84 * t83
  t95 = t85 * t93
  t97 = t45 * t44
  t99 = t46 * t44
  t101 = t46 * t97
  t105 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t85 - 0.15e2 / 0.4e1 * t84
  t111 = 0.63e2 / 0.8e1 * t91 - 0.35e2 / 0.4e1 * t93 + 0.15e2 / 0.8e1 * t83
  t115 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t45
  t118 = -0.138056183978125e0 * t46 - 0.92294814328125e-1 * t45 + 0.80024660533125e-1 * t49 - 0.80008813355625e-4 * t86 + 0.3020715669803125e-2 * t85 + 0.7031826877565625e-2 * t84 - 0.4373652639371875e-2 * t83 - 0.945883103563125e-3 * t91 + 0.4646102821846875e-2 * t93 + 0.19735677658125e-4 * t95 + 0.497944638409375e0 * t97 - 0.395061199588125e0 * t99 + 0.106025815520625e0 * t101 + 0.119130546e-2 * t44 * t105 + 0.822139896e-3 * t44 * t111 - 0.43464346e-1 * t115 * t83
  t120 = -0.1e1 / 0.2e1 + 0.3e1 / 0.2e1 * t84
  t125 = 0.5e1 / 0.2e1 * t93 - 0.3e1 / 0.2e1 * t83
  t135 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t86 - 0.315e3 / 0.16e2 * t85 + 0.105e3 / 0.16e2 * t84
  t142 = 0.429e3 / 0.16e2 * t95 - 0.693e3 / 0.16e2 * t91 + 0.315e3 / 0.16e2 * t93 - 0.35e2 / 0.16e2 * t83
  t147 = 0.5e1 / 0.2e1 * t97 - t42 / 0.8e1 + 0.3e1 / 0.2e1
  t164 = 0.3e1 / 0.8e1 + 0.35e2 / 0.8e1 * t46 - 0.15e2 / 0.4e1 * t45
  t171 = -0.150103636e-1 * t115 * t120 + 0.293253041e-2 * t115 * t125 + 0.182906057e-2 * t115 * t105 - 0.35104103e-3 * t115 * t111 + 0.668980219e-8 * t115 * t135 - 0.223014657e-8 * t115 * t142 - 0.182177954e-1 * t147 * t83 + 0.280678872e-1 * t147 * t120 - 0.845508103e-2 * t147 * t125 + 0.339308972e-2 * t147 * t105 + 0.100339208e0 * t44 * t83 - 0.879090772e-2 * t44 * t120 - 0.303347141e-2 * t44 * t125 - 0.493824365e-8 * t164 * t142 + 0.912223751e-8 * t164 * t135 + 0.209603871e-7 * t164 * t111
  t194 = -0.5e1 / 0.16e2 + 0.231e3 / 0.16e2 * t49 - 0.315e3 / 0.16e2 * t46 + 0.105e3 / 0.16e2 * t45
  t200 = 0.63e2 / 0.8e1 * t99 - 0.35e2 / 0.4e1 * t97 + 0.5e1 / 0.32e2 * t42 - 0.15e2 / 0.8e1
  t213 = 0.631891628e-2 * t164 * t125 - 0.790811707e-7 * t164 * t105 - 0.182911291e-1 * t164 * t120 + 0.162638575e-1 * t164 * t83 - 0.216860568e-7 * t147 * t135 + 0.674910119e-8 * t147 * t142 + 0.896739466e-3 * t147 * t111 - 0.514204676e-4 * t44 * t135 - 0.940351563e-5 * t44 * t142 - 0.957417512e-2 * t194 * t83 + 0.850272392e-8 * t200 * t142 - 0.376702959e-7 * t200 * t111 - 0.138472194e-7 * t200 * t135 + 0.162238741e-6 * t200 * t105 - 0.896771404e-2 * t200 * t125 - 0.188495102e-1 * t200 * t120
  t220 = 0.429e3 / 0.16e2 * t101 - 0.693e3 / 0.16e2 * t99 + 0.315e3 / 0.16e2 * t97 - 0.35e2 / 0.192e3 * t42 + 0.35e2 / 0.16e2
  t248 = 0.1380567225218996875e1 - 0.884148272e-2 * t200 * t83 + 0.505920757e-7 * t220 * t125 - 0.27652468e-6 * t220 * t120 + 0.940675747e-2 * t220 * t83 - 0.691592964e-8 * t194 * t142 + 0.694482484e-8 * t194 * t135 + 0.236391411e-7 * t194 * t111 - 0.416393106e-7 * t194 * t105 + 0.169805915e-6 * t194 * t120 - 0.265114646e-7 * t194 * t125 + 0.888525527e-8 * t220 * t142 - 0.338128188e-7 * t220 * t111 - 0.774224962e-8 * t220 * t135 + 0.554588743e-7 * t220 * t105 - 0.13022208355989583333e-1 * t42
  t254 = jnp.where(r0 / 0.2e1 <= p.dens_threshold, 0, -0.3e1 / 0.8e1 * t3 / t4 * t18 * t19 * (t118 + t171 + t213 + t248))
  res = 0.2e1 * t254
  return res