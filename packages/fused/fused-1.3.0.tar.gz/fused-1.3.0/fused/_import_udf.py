from typing import Any

from .core import import_from_github
from .core import import_udf as _import_udf


def import_udf(url_or_udf: str, /, *, cache_key: Any = None):
    if "/" in url_or_udf:
        email, udf_name = url_or_udf.split("/", maxsplit=1)
        return _import_udf(email, udf_name, cache_key=cache_key)
    else:
        return import_from_github(url_or_udf, cache_key=cache_key)
