#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Interpreter version: python 2.7
#
# Imports =====================================================================
import downloader


# Variables ===================================================================
TEST_FILE = "http://kitakitsune.org/bhole/test_file"


# Functions & classes =========================================================
def capture_progress(step, downloaded, content_len):
    print "Step %d (%d / %d)" % (step, downloaded, content_len)


# Tests =======================================================================
def test_head_request():
    headers = downloader.head_request(TEST_FILE)

    assert int(headers["content-length"]) == 1024 * 1024 * 5
    assert "content-type" in headers


def test_download():
    data = downloader.download(TEST_FILE)

    assert data == 1024 * 1024 * 5 * "f"


def test_progress():
    data = downloader.progress_download(TEST_FILE, 5, capture_progress)

    assert data == 1024 * 1024 * 5 * "f"

