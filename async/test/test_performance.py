# Copyright (C) 2010, 2011 Sebastian Thiel (byronimo@gmail.com) and contributors
#
# This module is part of async and is released under
# the New BSD License: http://www.opensource.org/licenses/bsd-license.php
"""Channel testing"""
from .lib import *
from .task import *

from async.pool import *
from async.thread import terminate_threads
from async.util import cpu_count

import time
import sys



class TestThreadPoolPerformance(TestBase):

    max_threads = cpu_count()

    def test_base(self):
        # create a dependency network, and see how the performance changes
        # when adjusting the amount of threads
        pool = ThreadPool(0)
        ni = 1000               # number of items to process
        print(self.max_threads)
        for num_threads in range(self.max_threads*2 + 1):
            pool.set_size(num_threads)
            for num_transformers in (1, 5, 10):
                for read_mode in range(2):
                    ts, rcs = add_task_chain(pool, ni, count=num_transformers,
                                                feedercls=IteratorThreadTask,
                                                transformercls=TestPerformanceThreadTask,
                                                include_verifier=False)

                    mode_info = "read(0)"
                    if read_mode == 1:
                        mode_info = "read(1) * %i" % ni
                    # END mode info
                    fmt = "Threadcount=%%i: Produced %%i items using %s in %%i transformations in %%f s (%%f items / s)" % mode_info
                    reader = rcs[-1]
                    st = time.time()
                    if read_mode == 1:
                        for i in range(ni):
                            assert len(reader.read(1)) == 1
                        # END for each item to read
                    else:
                        assert len(reader.read(0)) == ni
                    # END handle read mode
                    elapsed = time.time() - st
                    print(fmt % (num_threads, ni, num_transformers, elapsed, ni / elapsed), file=sys.stderr)
                # END for each read-mode
            # END for each amount of processors
        # END for each thread count
