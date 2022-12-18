# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.


import collections

from sys import version_info as _version_info
if _version_info < (3, 7, 0):
    raise RuntimeError("Python 3.7 or later required")

from . import _ITKCommonPython


from . import _RansacPython



from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _itkRansacPython
else:
    import _itkRansacPython

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _itkRansacPython.SWIG_PyInstanceMethod_New
_swig_new_static_method = _itkRansacPython.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import collections.abc
import itk.itkPointPython
import itk.itkVectorPython
import itk.vnl_vector_refPython
import itk.vnl_vectorPython
import itk.vnl_matrixPython
import itk.stdcomplexPython
import itk.pyBasePython
import itk.itkFixedArrayPython
import itk.ITKCommonBasePython
import itk.itkMatrixPython
import itk.vnl_matrix_fixedPython
import itk.itkCovariantVectorPython
class itkParametersEstimatorPD6(itk.ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkParametersEstimatorPD6 class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    Estimate = _swig_new_instance_method(_itkRansacPython.itkParametersEstimatorPD6_Estimate)
    LeastSquaresEstimate = _swig_new_instance_method(_itkRansacPython.itkParametersEstimatorPD6_LeastSquaresEstimate)
    Agree = _swig_new_instance_method(_itkRansacPython.itkParametersEstimatorPD6_Agree)
    AgreeMultiple = _swig_new_instance_method(_itkRansacPython.itkParametersEstimatorPD6_AgreeMultiple)
    SetMinimalForEstimate = _swig_new_instance_method(_itkRansacPython.itkParametersEstimatorPD6_SetMinimalForEstimate)
    GetMinimalForEstimate = _swig_new_instance_method(_itkRansacPython.itkParametersEstimatorPD6_GetMinimalForEstimate)
    __swig_destroy__ = _itkRansacPython.delete_itkParametersEstimatorPD6
    cast = _swig_new_static_method(_itkRansacPython.itkParametersEstimatorPD6_cast)

# Register itkParametersEstimatorPD6 in _itkRansacPython:
_itkRansacPython.itkParametersEstimatorPD6_swigregister(itkParametersEstimatorPD6)
itkParametersEstimatorPD6_cast = _itkRansacPython.itkParametersEstimatorPD6_cast


def itkRANSACPD6S_New():
    return itkRANSACPD6S.New()

class itkRANSACPD6S(itk.ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkRANSACPD6S class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRansacPython.itkRANSACPD6S___New_orig__)
    Clone = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6S_Clone)
    SetNumberOfThreads = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6S_SetNumberOfThreads)
    SetMaxIteration = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6S_SetMaxIteration)
    GetNumberOfThreads = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6S_GetNumberOfThreads)
    SetParametersEstimator = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6S_SetParametersEstimator)
    SetData = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6S_SetData)
    SetAgreeData = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6S_SetAgreeData)
    Compute = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6S_Compute)
    __swig_destroy__ = _itkRansacPython.delete_itkRANSACPD6S
    cast = _swig_new_static_method(_itkRansacPython.itkRANSACPD6S_cast)

    def New(*args, **kargs):
        """New() -> itkRANSACPD6S

        Create a new object of the class itkRANSACPD6S and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRANSACPD6S.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRANSACPD6S.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRANSACPD6S.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRANSACPD6S in _itkRansacPython:
_itkRansacPython.itkRANSACPD6S_swigregister(itkRANSACPD6S)
itkRANSACPD6S___New_orig__ = _itkRansacPython.itkRANSACPD6S___New_orig__
itkRANSACPD6S_cast = _itkRansacPython.itkRANSACPD6S_cast


def itkRANSACPD6V_New():
    return itkRANSACPD6V.New()

class itkRANSACPD6V(itk.ITKCommonBasePython.itkObject):
    r"""Proxy of C++ itkRANSACPD6V class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRansacPython.itkRANSACPD6V___New_orig__)
    Clone = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6V_Clone)
    SetNumberOfThreads = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6V_SetNumberOfThreads)
    SetMaxIteration = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6V_SetMaxIteration)
    GetNumberOfThreads = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6V_GetNumberOfThreads)
    SetParametersEstimator = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6V_SetParametersEstimator)
    SetData = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6V_SetData)
    SetAgreeData = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6V_SetAgreeData)
    Compute = _swig_new_instance_method(_itkRansacPython.itkRANSACPD6V_Compute)
    __swig_destroy__ = _itkRansacPython.delete_itkRANSACPD6V
    cast = _swig_new_static_method(_itkRansacPython.itkRANSACPD6V_cast)

    def New(*args, **kargs):
        """New() -> itkRANSACPD6V

        Create a new object of the class itkRANSACPD6V and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkRANSACPD6V.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkRANSACPD6V.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkRANSACPD6V.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkRANSACPD6V in _itkRansacPython:
_itkRansacPython.itkRANSACPD6V_swigregister(itkRANSACPD6V)
itkRANSACPD6V___New_orig__ = _itkRansacPython.itkRANSACPD6V___New_orig__
itkRANSACPD6V_cast = _itkRansacPython.itkRANSACPD6V_cast


def itkLandmarkRegistrationEstimatorD6S_New():
    return itkLandmarkRegistrationEstimatorD6S.New()

class itkLandmarkRegistrationEstimatorD6S(itkParametersEstimatorPD6):
    r"""Proxy of C++ itkLandmarkRegistrationEstimatorD6S class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6S___New_orig__)
    Clone = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6S_Clone)
    Estimate = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6S_Estimate)
    LeastSquaresEstimate = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6S_LeastSquaresEstimate)
    SetDelta = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6S_SetDelta)
    GetDelta = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6S_GetDelta)
    SetAgreeData = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6S_SetAgreeData)
    __swig_destroy__ = _itkRansacPython.delete_itkLandmarkRegistrationEstimatorD6S
    cast = _swig_new_static_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6S_cast)

    def New(*args, **kargs):
        """New() -> itkLandmarkRegistrationEstimatorD6S

        Create a new object of the class itkLandmarkRegistrationEstimatorD6S and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLandmarkRegistrationEstimatorD6S.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLandmarkRegistrationEstimatorD6S.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLandmarkRegistrationEstimatorD6S.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLandmarkRegistrationEstimatorD6S in _itkRansacPython:
_itkRansacPython.itkLandmarkRegistrationEstimatorD6S_swigregister(itkLandmarkRegistrationEstimatorD6S)
itkLandmarkRegistrationEstimatorD6S___New_orig__ = _itkRansacPython.itkLandmarkRegistrationEstimatorD6S___New_orig__
itkLandmarkRegistrationEstimatorD6S_cast = _itkRansacPython.itkLandmarkRegistrationEstimatorD6S_cast


def itkLandmarkRegistrationEstimatorD6V_New():
    return itkLandmarkRegistrationEstimatorD6V.New()

class itkLandmarkRegistrationEstimatorD6V(itkParametersEstimatorPD6):
    r"""Proxy of C++ itkLandmarkRegistrationEstimatorD6V class."""

    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __New_orig__ = _swig_new_static_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6V___New_orig__)
    Clone = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6V_Clone)
    Estimate = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6V_Estimate)
    LeastSquaresEstimate = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6V_LeastSquaresEstimate)
    SetDelta = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6V_SetDelta)
    GetDelta = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6V_GetDelta)
    SetAgreeData = _swig_new_instance_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6V_SetAgreeData)
    __swig_destroy__ = _itkRansacPython.delete_itkLandmarkRegistrationEstimatorD6V
    cast = _swig_new_static_method(_itkRansacPython.itkLandmarkRegistrationEstimatorD6V_cast)

    def New(*args, **kargs):
        """New() -> itkLandmarkRegistrationEstimatorD6V

        Create a new object of the class itkLandmarkRegistrationEstimatorD6V and set the input and the parameters if some
        named or non-named arguments are passed to that method.

        New() tries to assign all the non named parameters to the input of the new objects - the
        first non named parameter in the first input, etc.

        The named parameters are used by calling the method with the same name prefixed by 'Set'.

        Ex:

          itkLandmarkRegistrationEstimatorD6V.New(reader, threshold=10)

        is (most of the time) equivalent to:

          obj = itkLandmarkRegistrationEstimatorD6V.New()
          obj.SetInput(0, reader.GetOutput())
          obj.SetThreshold(10)
        """
        obj = itkLandmarkRegistrationEstimatorD6V.__New_orig__()
        from itk.support import template_class
        template_class.New(obj, *args, **kargs)
        return obj
    New = staticmethod(New)


# Register itkLandmarkRegistrationEstimatorD6V in _itkRansacPython:
_itkRansacPython.itkLandmarkRegistrationEstimatorD6V_swigregister(itkLandmarkRegistrationEstimatorD6V)
itkLandmarkRegistrationEstimatorD6V___New_orig__ = _itkRansacPython.itkLandmarkRegistrationEstimatorD6V___New_orig__
itkLandmarkRegistrationEstimatorD6V_cast = _itkRansacPython.itkLandmarkRegistrationEstimatorD6V_cast



