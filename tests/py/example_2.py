# Auto generated from jsg/example_2.jsg by PyJSG version 0.3.1
# Generation date: 2017-12-17 21:15
#
from typing import Optional, Dict, List, Union, _ForwardRef

from pyjsg.jsglib import jsg
from pyjsg.jsglib import typing_patch

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")



class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'street': str,
                'no': int}
    _strict = True
    
    def __init__(self,
                 street: str = None,
                 no: int = None,
                 **_kwargs: Dict[str, object]):
        self._context = _CONTEXT
        self.street = jsg.String(street)
        self.no = jsg.Integer(no)
        super().__init__(self._context, **_kwargs)


_CONTEXT.NAMESPACE = locals()
