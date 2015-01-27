#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import requests


# Variables ===================================================================



# Functions & classes =========================================================
def head_request(url):
    resp = requests.head(url)

    resp.raise_for_status()

    return dict(resp.headers)


def download(url):
    resp = requests.get(url)

    resp.raise_for_status()

    return resp.content


def progress_download(url):
    pass
