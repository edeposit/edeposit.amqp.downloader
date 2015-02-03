#! /usr/bin/env bash

PYTHONPATH="$PYTHONPATH:src/edeposit/amqp"

py.test -s tests 