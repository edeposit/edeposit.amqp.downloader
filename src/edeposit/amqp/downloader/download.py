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


def progress_download(url, steps, callback):
    output = bytes()

    response = requests.get(url, stream=True)
    total_length = response.headers.get('content-length')

    if total_length is None:  # no content length header
        return response.content

    total_length = int(total_length)

    last_step = 0
    downloaded_len = 0
    step = int(total_length / steps)
    for data in response.iter_content():
        downloaded_len += len(data)
        output += data

        progress = int(downloaded_len / step)
        if progress != last_step:
            callback(progress)

    return output
