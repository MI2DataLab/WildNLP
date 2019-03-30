How to contribute
=================
Already implemented functions by no means exhaust
all the possibilities for corruptin a text.

There are also many popular datasets that we still don't support.

If you'd like to extend the module, you're more than welcome! :)


General remarks
---------------
1. Unit tests are boring but sometimes also helpful.
2. Documenting your work helps other to use it.


How to add an Aspect
--------------------
All the aspects inherits from the Aspect class.
The only thin you should remeber is to implement the
__call__ function accepting a single argument (string)
and returning a single output (string).

That's it, we leave the details to you! Remeber that
natural language is tricky, there are punctuation marks, 
capitalizations, apostrophes etc, that you may would like to leave
intact if it's not the target of your aspect.

.. caution:: Every aspect must implement __call__ function
  accepting a string as an input and outputing a string.

How to add a dataset support
----------------------------
All the datasets inherits from the Dataset class.
There are only 3 methods that it must implement.

1. **load** - load a dataset from file to an iterable internal object.

2. **apply** - iterate through all elements (strings) in a dataset
and modify them one by one.

3. **save** - save the dataset in the same exact format as the original one.

.. caution:: Saved dataset should have the same format as the original one.
