#! /usr/bin/env bash

PYTHONPATH="$PYTHONPATH:src/edeposit/amqp/downloader"

py.test "src/edeposit/amqp/downloader/tests" -vv