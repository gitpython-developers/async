.. _tutorial-label:

###########
Usage Guide
###########

******
Design
******
The central instance within *async* is the **Pool**. A pool keeps a set of 0 or more workers which can run asynchronoously and process **Task**\ s. Tasks are added to the pool using the ``add_task`` function. Once added, the caller receives a **ChannelReader** instance which connects to a channel. Calling ``read`` on the instance will trigger the actual computation. A ChannelReader can serve as input for another task as well, which once added to the Pool, indicates a dependency between these tasks. To obtain one item from task 2, one item needs to be produced by task 1 beforehand - the pool takes care of the dependency handling when scheduling items to be processed.

Task instances allow to define the minimum amount of items to be processed on each request, and the maximum amount of items per batch. This chunking behaviour allows you to have fine-grained control about the memory requirements as well as the actually achieved concurrency for your chain of tasks.

Task chunks are the units actually being processed by the workers, the pool assures these are processed in the right order. Chunks help to bridge the gap between items that take a long time to process, and those which are quickly generated. Generally, slow tasks should have small chunks, otherwise some of the workers might just end up waiting for input while slowly processing items of a big chunk take place in another worker. If chunks are too big, and there are many workers, it may also be that some workers don't get any work. By default, the size of the chunk is entirely determined by the amount of items requested by the reader.

**************
The ThreadPool
**************
A thread pool is a pool implementation which uses threads as workers. ``ChannelReader``\ s are blocking channels which are used as a means of communication  between tasks which are currently being processed.

The ``set_size`` method is essential, as it determines the amount of workers in the pool. It defaults to 0 for newly created pools, which is equal to a fully synchronized mode of operation - all processing is effectively done by the calling thread::
    
    from async.pool import ThreadPool
    
    p = ThreadPool()
    # default size is 0, synchronous mode
    assert p.size() == 0
    
    # now tasks would be processed asynchronously
    p.set_size(1)
    assert p.size() == 1

Currently this is the only implementation, but it was designed with the ``Multiprocessing`` package in mind, which shouldn't make it too hard to implement that in future releases.

*****
Tasks
*****
A task encapsulates properties of a task, and how its items should be processed. The processing is usually performed per item, calling a function with one item, to receive a processed item back which will be written into the output channel. The read-end of that channel is either held by the client of the items, or by another task which performs additional processing.

In the following example, a simple task is created which takes integers and multiplies them by themselves::
    
    from async.task import IteratorThreadTask
    
    # A task performing processing on items from an iterator
    t = IteratorThreadTask(iter(range(10)), "power", lambda i: i*i)
    reader = p.add_task(t)
    
    # read all items - they where procesed by worker 1
    items = reader.read()
    assert len(items) == 10 and items[0] == 0 and items[-1] == 81
    
.. note:: 
    Due to the gil, it makes no sense to process anything using pure python - it will never run concurrently with other workers, but only asynchronously.
    Concurrency can only be achieved when using c-extensions which release the GIL before long-running or blocking portions of their code.

*****************************
Channels, Readers and Writers
*****************************
Channels are the means of communication between tasks as well as clients to finally receive the processed items. A channel has one or more write-ends and and one or more read-ends. Readers will block if there are less than the requested amount of items, but will wake up once the missing items where sent through the write-end.

A channel's major difference to a queue is its ability to be closed, which will immediately wake up all waiting readers.

Reader Callbacks
================
The reader returned by the Pool's ``add_task`` method is a specialized version of a ``CallbackChannelReader``, which allows to setup functions to be called before and after an item is read. This allows for just-in-time notification of asynchronous events, as well as to apply item transformations. 

**************
Chaining Tasks
**************
When using different task types, chains between tasks can be created. These will be understood by the pool, which then realizes the implicit task dependency and will schedule the tasks in the right order.

The following example creates two tasks which combine their results. As the pool only has one worker, and as the chunk size is maximized, we can be sure that the items are returned in order::
    
    from async.task import ChannelThreadTask
    
    t = IteratorThreadTask(iter(range(10)), "power", lambda i: i*i)
    reader = p.add_task(t)
    
    # chain both by linking their readers
    tmult = ChannelThreadTask(reader, "mult", lambda i: i*2)
    result_reader = p.add_task(tmult)
    
    # read all
    items = result_reader.read()
    assert len(items) == 10 and items[0] == 0 and items[-1] == 162


