# -*- coding: utf-8 -*-
from __future__ import absolute_import
import time
from hashlib import md5
from datetime import datetime
from xml.etree import ElementTree
from collections import OrderedDict

import six
import requests
from pytz import timezone

if six.PY3:
    from urllib.parse import (
        parse_qs,
        urlparse,
        unquote,
        urlencode
    )
else:
    from six.moves.urllib.parse import (
        parse_qs,
        urlparse,
        unquote,
        urlencode
    )

from .exceptions import (
    MissingParameter,
    ParameterValueError,
    TokenAuthorizationError
)

def encode_dict(params):
    return {k: six.u(v).encode('utf-8')
            if isinstance(v, str) else v.encode('utf-8')
            if isinstance(v, six.string_types) else v
            for k, v in six.iteritems(params)}


class Alipay(object):
    GATEWAY_URL = 'https://mapi.alipay.com/gateway.do'

    NOTIFY_GATEWAY_URL = 'https://mapi.alipay.com/gateway.do'\
        '?service=notify_verify&partner={partner}&notify_id={notify_id}'

    sign_tuple = ('sign_type', 'MD5', 'MD5')
    sign_key = False

