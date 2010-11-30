########
Overview
########

*Async* is one more attempt to make the definition and execution of asynchronous interdependent operations easy. For that to work, you may define tasks which communicate with each other by channels. Channels transfer items, which is very similar to bytes flowing through pipes uses in inter-process communication. Items will only be generated on demand, that is when you read from the respective output channel.

As it turned out, the GIL is far more restricting than initially thought, which effectively means true concurrency can only be obtained during input output to files and sockets, as well as specifically written versions of existing c python extensions which release the GIL before lengthy operations. Many of the currently available c extensions, such as zlib, lock everything down to just one thread at a time, even though this isn't a strict technical requirement.

If you want to make good use of *async*, you will have to carefully plan the operation, and you might end up writing a new or altering existing c-extensions for this.

If you have 10 minutes, watch a more graphical presentation `on youtube <http://www.youtube.com/watch?v=wy1yB1M-dcQ>`_.

================
Installing Async
================
Its easiest to install async using the *easy_install*  program, which is part of the `setuptools`_::
    
    $ easy_install async
    
As the command will install async in your respective python distribution, you will most likely need root permissions to authorize the required changes.

If you have downloaded the source archive, the package can be installed by running the ``setup.py`` script::
    
    $ python setup.py install
    
===============
Getting Started
===============
It is advised to have a look at the :ref:`Usage Guide <tutorial-label>` for a brief introduction.
    

=================
Source Repository
=================
The latest source can be cloned using git from github:

 * git://github.com/gitpython-developers/async.git
 
 
License Information
===================
*Async* is licensed under the New BSD License.


.. _setuptools: http://peak.telecommunity.com/DevCenter/setuptools
