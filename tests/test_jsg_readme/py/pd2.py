# Auto generated from tests/test_jsg_readme/jsg/pd2.jsg by PyJSG version 0.5.3
# Generation date: 2018-04-19 11:55
#
import sys
from typing import Optional, Dict, List, Union
if sys.version_info < (3, 7):
    from typing import _ForwardRef as ForwardRef
    from pyjsg.jsglib import typing_patch_36
else:
    from typing import ForwardRef
    from pyjsg.jsglib import typing_patch_37

from pyjsg.jsglib import jsg
from pyjsg.jsglib.jsg import isinstance_

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE = "id"
_CONTEXT.TYPE_EXCEPTIONS.append("person")



class person(jsg.JSGObject):
    _reference_types = []
    _members = {'name': str,
                'age': int}
    _strict = True
    
    def __init__(self,
                 name: str = None,
                 age: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.name = jsg.String(name)
        self.age = jsg.Integer(age)
        super().__init__(self._context, **_kwargs)


class membership(jsg.JSGObject):
    _reference_types = []
    _members = {'list_name': str,
                'members': List[person]}
    _strict = True
    
    def __init__(self,
                 list_name: str = None,
                 members: List[person] = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.list_name = jsg.String(list_name)
        self.members = members
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()
