#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
from .utils import get_logger

logger = get_logger(__file__)


class Checker(object):
    def check_command(self, command):
        if command == 'dir':
            return False
        return True
