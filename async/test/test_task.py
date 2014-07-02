# Copyright (C) 2010, 2011 Sebastian Thiel (byronimo@gmail.com) and contributors
#
# This module is part of async and is released under
# the New BSD License: http://www.opensource.org/licenses/bsd-license.php
"""Channel testing"""
from .lib import *
from async.util import *
from async.task import *

import time

class TestTask(TestBase):
    
    max_threads = cpu_count()
    
    def test_iterator_task(self):
        # tested via test_pool
        pass
        
