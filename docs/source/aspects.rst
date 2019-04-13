Aspects
=======
Functions that can be applied to sentences to corrupt them in a controled way.
Corrupted sentences can be then used to test NLP models' robustness.

Base class
----------
.. autoclass:: wildnlp.aspects.base.Aspect
   :members:
   :special-members: __call__
   :private-members:

Utility functions
-----------------

.. automodule:: wildnlp.aspects.utils
   :members:

AddSubString
------------

.. autoclass:: wildnlp.aspects.add_sub_string.AddSubString
   :members:
   :special-members: __init__
   :show-inheritance:

Articles
--------

.. autoclass:: wildnlp.aspects.articles.Articles
   :members:
   :special-members: __init__
   :show-inheritance:

ChangeChar
----------

.. autoclass:: wildnlp.aspects.change_char.ChangeChar
   :members:
   :special-members: __init__
   :show-inheritance:

Characters removal
------------------

.. autoclass:: wildnlp.aspects.remove_char.RemoveChar
   :members:
   :special-members: __init__
   :show-inheritance:

Characters swapping
-------------------

.. autoclass:: wildnlp.aspects.swap.Swap
   :members:
   :special-members: __init__
   :show-inheritance:

Digits2Words
------------

.. autoclass:: wildnlp.aspects.digits2words.Digits2Words
   :members:
   :special-members: __init__
   :show-inheritance:

Misspelling
-----------

.. autoclass:: wildnlp.aspects.misspelling.Misspelling
   :members:
   :special-members: __init__
   :show-inheritance:

Punctuation
-----------

.. autoclass:: wildnlp.aspects.punctuation.Punctuation
   :members:
   :special-members: __init__
   :show-inheritance:

QWERTY
------

.. autoclass:: wildnlp.aspects.qwerty.QWERTY
   :members:
   :special-members: __init__
   :show-inheritance:

Sentiment words masking
-----------------------

.. autoclass:: wildnlp.aspects.sentiment_masking.SentimentMasking
   :members:
   :special-members: __init__
   :show-inheritance:

WhiteSpaces
-----------------------

.. autoclass:: wildnlp.aspects.white_spaces.WhiteSpaces
   :members:
   :special-members: __init__
   :show-inheritance: