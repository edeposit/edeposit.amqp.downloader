#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import pytest
import requests

import downloader


# Variables ===================================================================
TEST_FILE = "http://kitakitsune.org/bhole/test_file"
PROGRESS_FILE = []


# Functions & classes =========================================================
def capture_progress(step, downloaded, content_len):
    print "Step %d (%d / %d)" % (step, downloaded, content_len)

    global PROGRESS_FILE

    PROGRESS_FILE.append(step)


# Tests =======================================================================
def test_head_request():
    headers = downloader.head_request(TEST_FILE)

    assert int(headers["content-length"]) == 1024 * 1024 * 5
    assert "content-type" in headers


def test_head_request_fail():
    with pytest.raises(requests.ConnectionError):
        downloader.head_request("http://azgabash")

    with pytest.raises(requests.HTTPError):
        downloader.head_request("http://kitakitsune.org/čř")


def test_download():
    data = downloader.download(TEST_FILE)

    assert data == 1024 * 1024 * 5 * "f"


def test_download_fail():
    with pytest.raises(requests.ConnectionError):
        downloader.download("http://azgabash")

    with pytest.raises(requests.HTTPError):
        downloader.download("http://kitakitsune.org/čř")


def test_progress():
    data = downloader.progress_download(TEST_FILE, 5, capture_progress)

    assert data == 1024 * 1024 * 5 * "f"
    assert PROGRESS_FILE == range(1, 6)


def test_progress_fail():
    with pytest.raises(requests.ConnectionError):
        downloader.progress_download("http://azgabash", 5, capture_progress)

    with pytest.raises(requests.HTTPError):
        downloader.progress_download(
            "http://kitakitsune.org/čř",
            5,
            capture_progress
        )
