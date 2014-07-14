# Copyright (C) 2010, 2011 Sebastian Thiel (byronimo@gmail.com) and contributors
#
# This module is part of async and is released under
# the New BSD License: http://www.opensource.org/licenses/bsd-license.php
# -*- coding: utf-8 -*-
""" Test thead classes and functions"""
from .lib import *
from async.thread import *
try:
    from queue import Queue
except ImportError:
    from Queue import Queue

import time

class TestWorker(WorkerThread):
    def __init__(self, *args, **kwargs):
        super(TestWorker, self).__init__(*args, **kwargs)
        self.reset()

    def fun(self, arg):
        self.called = True
        self.arg = arg
        return True

    def make_assertion(self):
        assert self.called
        assert self.arg
        self.reset()

    def reset(self):
        self.called = False
        self.arg = None


class TestThreads(TestBase):

    @terminate_threads
    def test_worker_thread(self):
        worker = TestWorker()
        assert isinstance(worker.start(), WorkerThread)

        # test different method types
        standalone_func = lambda *args, **kwargs: worker.fun(*args, **kwargs)
        for function in (TestWorker.fun, worker.fun, standalone_func):
            worker.inq.put((function, 1))
            time.sleep(0.01)
            worker.make_assertion()
        # END for each function type

        worker.stop_and_join()
