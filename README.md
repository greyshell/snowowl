# Quickstart

[snowowl](https://pypi.org/project/snowowl/) is a collection of common data structures written in `Python`.

> The complete documentation is [here]().

### How to install

```bash
pip install snowowl
```

### How to use 

```
#!/usr/bin/env python3
# author: greyshell
# description: demo Heap library

from snowowl import Heap, HeapType


if __name__ == '__main__':
    arr = [5, 9, 2]

    hmin = Heap(arr)  # create a min heap
    print(hmin.peek())  # peek the min item from the heap
    hmin.insert(1)  # insert an item into the heap
    print(hmin.remove())  # remove an item from the heap
    print(hmin)  # print all items from the heap
    print(len(hmin))  # print the length of the heap

    hmax = Heap(arr, HeapType.MAX)  # create a max heap
    print(hmax.peek())  # peek the max item from the heap
    hmax.insert(1)  # insert an item into the heap
    print(hmax.remove())  # remove an item from the heap
```

### How to uninstall / remove

```
pip uninstall snowowl
```