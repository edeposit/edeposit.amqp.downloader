#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from collections import namedtuple


# Functions & classes =========================================================
class DownloadedFile(namedtuple("DownloadedFile", ["url", "base64_data"])):
    pass


class Progress(namedtuple("Progress", ["url", "step", "downloaded",
                                                      "content_length"])):
    pass


class Exists(namedtuple("Exists", ["url", "result", "headers"])):
    pass
