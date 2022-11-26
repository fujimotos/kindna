=======================================
kinDNA -- Find similar DNA combinations
=======================================

A Python script that solves the following bio computing problem::

    Given a set containing N>>1e4 DNA sequences of length L,
    find all pairs that are at Levenshtein distance 1

Basic Usage
-----------

First install polyleven::

    $ pip install -r requirements.txt

Now you can run kindna.py as follows::

    $ python3 kindna.py < dna10k.txt

Notes
-----

* The brute-force solution for the problem requires :math:`O(N^2)`,
  since it needs to check :math:`N(N-1)/2` DNA pairs.

* This script uses a FastSS index [1]_ to improve the complexity.

.. [1]  T. Bocek, E. Hunt, and B. Stiller. Fast Similarity Search in Large
        Dictionaries. Technical Report ifi-2007.02, Department of Informatics,
        University of Zurich, April 2007. http://fastss.csg.uzh.
