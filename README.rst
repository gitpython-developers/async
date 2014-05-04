async
=====
Async aims to make writing asyncronous processing easier. It provides a task-graph 
with interdependent tasks that communicate using blocking channels, allowing 
to delay actual computations until items are requested.
Tasks will automatically be distributed among 0 or more threads for the actual computation.

Even though the GIL effectively prevents true concurrency, operations which block, 
such as file IO, can be sped up with it already. In conjuction with 
custom c extensions which release the GIL, true concurrency can be obtained as well.

REQUIREMENTS
============

* Python Nose - for running the tests

DEVELOPMENT STATUS
===================

Development was discontinued, as there are much better alternatives, like zeromq.

SOURCE
======
The source is available in a git repository at gitorious and github:

git://github.com/gitpython-developers/async.git

Run the tests with 
 cd async
 nosetests

MAILING LIST
============
http://groups.google.com/group/git-python

ISSUE TRACKER
=============
https://github.com/gitpython-developers/async/issues

LICENSE
=======
New BSD License
