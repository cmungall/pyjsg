# Auto generated from tests/test_jsg_readme/jsg/type_directive_1.jsg by PyJSG version 0.6.0
# Generation date: 2018-06-26 12:41
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import jsg, jsg_array
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")



class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'a': object}
    _strict = True
    
    def __init__(self,
                 a: object = jsg.EmptyAny,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.a = jsg.AnyType(a)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()
