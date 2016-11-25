#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Edward

import GeneralSetting
import sys
try:
    cmd = sys.argv[1]
    if cmd == "start":
        import modules.core.Root
    else:
        print("Please add 'start' as the first parameter")
except:
    print("Please add 'start' as the first parameter 1")