## async
Async aims to make writing asynchronous processing easier. It provides a task-graph 
with interdependent tasks that communicate using blocking channels, allowing 
to delay actual computations until items are requested.
Tasks will automatically be distributed among 0 or more threads for the actual computation.

Even though the GIL effectively prevents true concurrency, operations which block, 
such as file IO, can be sped up with it already. In conjunction with 
custom c extensions which release the GIL, true concurrency can be obtained as well.

## REQUIREMENTS

* Python Nose - for running the tests

Interpreter versions:

* 2.6
* 2.7
* 3.X
 * **NOTE:** it doesn't seem to work deterministically in this version, and must be avoided 

## DEVELOPMENT STATUS

[![Build Status](https://travis-ci.org/gitpython-developers/async.svg)](https://travis-ci.org/gitpython-developers/async)
[![Coverage Status](https://coveralls.io/repos/gitpython-developers/async/badge.png)](https://coveralls.io/r/gitpython-developers/async)

Development was discontinued, as there are much better alternatives, like zeromq.

**Async is considered useless (by me, the author) as the GIL will prevent anything good from happening (it gets slower instead of faster in multi-threaded mode ;)). Please do not use this project, which can be considered nothing more than an exercise I did years ago.**

## SOURCE
The source is available in a git repository at gitorious and github:

git://github.com/gitpython-developers/async.git

Run the tests with 
 cd async
 nosetests

## MAILING LIST

http://groups.google.com/group/git-python

## ISSUE TRACKER

https://github.com/gitpython-developers/async/issues

## LICENSE

New BSD License
