# coding: utf-8
from __future__ import (
    absolute_import,
    print_function,
    unicode_literals,
)

from pydocx.models import XmlModel, XmlCollection
from pydocx.openxml.wordprocessing.picture import Picture


class Fallback(XmlModel):
    XML_TAG = 'Fallback'
    # TODO #204: actually include all of the children defined in the spec.
    children = XmlCollection(Picture)
