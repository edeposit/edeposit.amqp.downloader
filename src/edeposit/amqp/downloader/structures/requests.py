#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
from collections import namedtuple


# Variables ===================================================================
# Functions & classes =========================================================
class Download(namedtuple("Download", ["url"])):
    pass


class ProgressDownload(namedtuple("ProgressDownload", ["url", "steps"])):
    pass


class CheckExistence(namedtuple("CheckExistence", ["url"])):
    pass
