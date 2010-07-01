#!/usr/bin/env python
from distutils.core import setup, Extension 
    
setup(name = "async",
      version = "0.6.0",
      description = "Async Framework",
      author = "Sebastian Thiel",
      author_email = "byronimo@gmail.com",
      url = "http://gitorious.org/git-python/async",
      packages = ('async', 'async.mod', 'async.test', 'async.test.mod'),
      package_data={'async' : ['AUTHORS', 'README']},
      package_dir = {'async':''},
      ext_modules=[Extension('async.mod.zlib', ['mod/zlibmodule.c'])],
      license = "BSD License",
      long_description = """Async is a framework to process interdependent tasks in a pool of workers"""
      )
