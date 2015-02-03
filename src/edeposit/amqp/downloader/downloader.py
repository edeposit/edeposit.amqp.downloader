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

    # handle lenght of the file
    total_length = response.headers.get('content-length')

    if total_length is None:  # no content length header
        return response.content

    total_length = int(total_length)

    # download files and compute progress
    last_step_number = 0
    downloaded_len = 0
    step_len = int(total_length / steps)
    for data in response.iter_content(5*1024):
        downloaded_len += len(data)
        output += data

        step_number = int(downloaded_len / step_len)
        if step_number != last_step_number:
            callback(step_number, downloaded_len, total_length)
            last_step_number = step_number

    return output
