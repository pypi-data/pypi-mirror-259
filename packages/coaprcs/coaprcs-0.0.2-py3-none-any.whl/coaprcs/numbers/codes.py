# SPDX-FileCopyrightText: Christian Amsüss and the aiocoap contributors
#
# SPDX-License-Identifier: MIT

"""List of known values for the CoAP "Code" field.

The values in this module correspond to the IANA registry "`CoRE Parameters`_",
subregistries "CoAP Method Codes" and "CoAP Response Codes".

The codes come with methods that can be used to get their rough meaning, see
the :class:`Code` class for details.

.. _`CoRE Parameters`: https://www.iana.org/assignments/core-parameters/core-parameters.xhtml
"""

import warnings
import random

from ..util import ExtensibleIntEnum

class Code(ExtensibleIntEnum):
    """Value for the CoAP "Code" field.

    As the number range for the code values is separated, the rough meaning of
    a code can be determined using the :meth:`is_request`, :meth:`is_response` and
    :meth:`is_successful` methods."""

EMPTY = 0
GET = 1
POST = 2
PUT = 3
DELETE = 4
FETCH = 5
PATCH = 6
iPATCH = 7
#Aleatorizar---------------------------------------

lista_original = [65,66,67,68,69,95,128,129,130,131,132,133,134,136,(4<<5)+9,140,141,143,(4<<5)+22,(4<<5)+29,160,161,162,163,164,165,(5<<5)+8]
lista_auxiliar = lista_original
#lista_original = [65,66,67,68,69,95,128,129,130,131,132,133,134,136,140,141,143,160,161,162,163,164,165]
print("Lista original",lista_auxiliar)
#print("Lista original:", lista_original)
random.shuffle(lista_original)
print("Lista reordenada:", lista_original)

for indice, valor in enumerate(lista_original):
    if indice == 0:
        CREATED = valor #2.01
    elif indice == 1:
        DELETED = valor #2.02
    elif indice == 2:
        VALID = valor #2.03
    elif indice == 3:
        CHANGED = valor #2.04
    elif indice == 4:
        CONTENT = valor #2.05

    elif indice == 5:
        CONTINUE = valor #2.31
    elif indice == 6:
        BAD_REQUEST = valor #4.00
    elif indice == 7:
        UNAUTHORIZED = valor #4.01
    elif indice == 8:
        BAD_OPTION = valor #4.02
    elif indice == 9:    
        FORBIDDEN = valor #4.03
    elif indice == 10:
        NOT_FOUND = valor #4.04
    elif indice == 11:
        METHOD_NOT_ALLOWED = valor #4.05
    elif indice == 12:
        NOT_ACCEPTABLE = valor #4.06
    elif indice == 13:
        REQUEST_ENTITY_INCOMPLETE = valor #4.08
    elif indice == 14:
        CONFLICT = (4 << 5) + 9 #4.09
    elif indice == 15:    
        PRECONDITION_FAILED = valor #4.12
    elif indice == 16:
        REQUEST_ENTITY_TOO_LARGE = valor #4.13
    elif indice == 17:
        UNSUPPORTED_CONTENT_FORMAT = 143 #4.15
    @property
    def UNSUPPORTED_MEDIA_TYPE(self):
        warnings.warn("UNSUPPORTED_MEDIA_TYPE is a deprecated alias for UNSUPPORTED_CONTENT_FORMAT")
        return self.UNSUPPORTED_CONTENT_FORMAT
    
    if indice == 18:
        UNPROCESSABLE_ENTITY = (4 << 5) + 22 #4.22
    elif indice == 19:    
        TOO_MANY_REQUESTS = (4 << 5) + 29 #4.29
    elif indice == 20:    
        INTERNAL_SERVER_ERROR = valor #5.00
    elif indice == 21:
        NOT_IMPLEMENTED = valor #5.01
    elif indice == 22:
        BAD_GATEWAY = valor #5.02
    elif indice == 23:
        SERVICE_UNAVAILABLE = valor #5.03
    elif indice == 24:
        GATEWAY_TIMEOUT = valor #5.04
    elif indice == 25:
        PROXYING_NOT_SUPPORTED = valor #5.05
    elif indice == 26:
        HOP_LIMIT_REACHED = (5 << 5) + 8 #5.08
    #---------------------------------------------------
    CSM = 225
    PING = 226
    PONG = 227
    RELEASE = 228
    ABORT = 229

    def is_request(self):
        """True if the code is in the request code range"""
        return True if (self >= 1 and self < 32) else False


    def is_response(self):
        """True if the code is in the response code range"""
        return True if (self >= 64 and self < 192) else False

    def is_signalling(self):
        return True if self >= 224 else False


    def is_successful(self):
        """True if the code is in the successful subrange of the response code range"""
        return True if (self >= 64 and self < 96) else False

    def can_have_payload(self):
        """True if a message with that code can carry a payload. This is not
        checked for strictly, but used as an indicator."""
        return self.is_response() or self in (self.POST, self.PUT, self.FETCH, self.PATCH, self.iPATCH)

    @property
    def class_(self):
        """The class of a code (distinguishing whether it's successful, a
        request or a response error or more).

        >>> Code.CONTENT
        <Successful Response Code 69 "2.05 Content">
        >>> Code.CONTENT.class_
        2
        >>> Code.BAD_GATEWAY
        <Response Code 162 "5.02 Bad Gateway">
        >>> Code.BAD_GATEWAY.class_
        5
        """
        return self >> 5

    @property
    def dotted(self):
        """The numeric value three-decimal-digits (c.dd) form"""
        return "%d.%02d" % divmod(self, 32)

    @property
    def name_printable(self):
        """The name of the code in human-readable form"""
        return self.name.replace('_', ' ').title()

    def __str__(self):
        """
        >>> print(Code.GET)
        GET
        >>> print(Code.CONTENT)
        2.05 Content
        >>> print(Code.BAD_GATEWAY)
        5.02 Bad Gateway
        >>> print(Code(32))
        32
        """
        if self.is_request() or self is self.EMPTY:
            return self.name
        elif self.is_response() or self.is_signalling():
            return "%s %s" % (self.dotted, self.name_printable)
        else:
            return "%d" % self

    def _classification(self):
        return ("Successful " if self.is_successful() else "") + ("Request " if self.is_request() else "Response " if self.is_response() else "")

    def __repr__(self):
        """
        >>> Code.GET
        <Request Code 1 "GET">
        >>> Code.CONTENT
        <Successful Response Code 69 "2.05 Content">
        >>> Code.BAD_GATEWAY
        <Response Code 162 "5.02 Bad Gateway">
        >>> Code(32)
        <Code 32 "32">
        """
        return '<%sCode %d "%s">' % (self._classification(), self, self)

    name = property(lambda self: self._name if hasattr(self, "_name") else "(unknown)", lambda self, value: setattr(self, "_name", value), doc="The constant name of the code (equals name_printable readable in all-caps and with underscores)")

    def _repr_html_(self):
        import html
        if hasattr(self, "_name"):
            return f'<abbr title="{self._classification()}Code {self.dotted}">{html.escape(self.name)}</abbr>'
        else:
            return f'<abbr title="Unknown {self._classification()}Code">{self.dotted}</abbr>'

for k in vars(Code):
    if isinstance(getattr(Code, k), Code):
        locals()[k] = getattr(Code, k)

__all__ = ['Code'] + [k for (k, v) in locals().items() if isinstance(v, Code)]
