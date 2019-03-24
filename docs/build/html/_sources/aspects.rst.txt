Aspects
=======
Functions that can be applied to sentences to corrupt them in a controled way.
Corrupted sentences can be then used to test NLP models' robustness.


Utility functions
-----------------

.. automodule:: wildnlp.aspects.utils
   :members:


Dummy aspects
-------------
Convenient for testing. Shouldn't be used for actual 
transformation of datasets.

Reverser
~~~~~~~~

.. autoclass:: wildnlp.aspects.dummy.reverser.Reverser
   :members:
   :special-members: __call__
   :show-inheritance:

PigLatin
~~~~~~~~

.. autoclass:: wildnlp.aspects.dummy.piglatin.PigLatin
   :members:
   :special-members: __call__
   :show-inheritance: