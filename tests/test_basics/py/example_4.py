# Auto generated from test_basics/jsg/example_4.jsg by PyJSG version 0.9.0
# Generation date: 2019-03-17 15:24
#
import typing
import pyjsg.jsglib as jsg

# .TYPE and .IGNORE settings
_CONTEXT = jsg.JSGContext()
_CONTEXT.TYPE_EXCEPTIONS.append("doc")


class NAME(jsg.JSGString):
    pattern = jsg.JSGPattern(r'.*')


class TEMPLATE(jsg.JSGString):
    pattern = jsg.JSGPattern(r'\{.*\}')


nameOrTemplate = typing.Union[NAME, TEMPLATE]


class doc(jsg.JSGObject):
    _reference_types = []
    _members = {'street': nameOrTemplate}
    _strict = True

    def __init__(self,
                 street: typing.Union[str, str] = None,
                 **_kwargs: typing.Dict[str, object]):
        super().__init__(_CONTEXT, **_kwargs)
        self.street = street


_CONTEXT.NAMESPACE = locals()
