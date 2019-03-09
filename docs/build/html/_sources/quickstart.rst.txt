Quick Start Guide
=================
5 minutes is enough to start using the module!

Installation
------------
::

  pip install wild-nlp

Loading a dataset
-----------------
.. code-block:: python
  :linenos:

  from wildnlp.datasets import SampleDataset

  dataset = SampleDataset()
  dataset.load()

Corrupting a text
-----------------
.. code-block:: python
  :linenos:

  from wildnlp.aspects import Reverser
  modified = dataset.apply(Reverser())

Full example with multiple corruptors
-------------------------------------

The code
~~~~~~~~
.. code-block:: python
  :linenos:

  from wildnlp.aspects import Reverser, PigLatin
  from wildnlp.aspects.utils import compose
  from wildnlp.datasets import SampleDataset

  # Create a dataset object and load the dataset
  dataset = SampleDataset()
  dataset.load()

  # Crate a composed corruptor function.
  # Functions will be applied in the same order they appear.
  composed = compose(Reverser(), PigLatin())

  # Apply the function to the dataset
  modified = dataset.apply(composed)

The dataset's contents
~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python
  
  ["Manning is a leader in applying Deep Learning "
   "to Natural Language Processing",
   "Manning has coauthored leading textbooks on statistical "
   "approaches to Natural Language Processing"]

After applying the aspects
~~~~~~~~~~~~~~~~~~~~~~~~~~
>>> print(modified)
['ninnamgay isay aay edaelray inay niylppagay eedpay ninraelgay toay arutanlay gaugnaleay nissecorpgay', 'ninnamgay ahsay erohtuaocday nidaelgay koobtxetsay onay acitsitatslay ehcaorppasay toay arutanlay gaugnaleay nissecorpgay']

