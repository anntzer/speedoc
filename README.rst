speedoc – sphinx meets pydoc
============================

Turn docstrings into man pages using Sphinx_, and view the result with ``man``.

.. _Sphinx: http://www.sphinx-doc.org

Installation
------------

.. code:: sh

   python -mpip install git+https://github.com/anntzer/speedoc

Usage
-----

.. code:: sh

   speedoc [--opts ...] obj.to.document

Options are passed as is to ``python -msphinx``.  By default, ``sphinx`` is
invoked as

.. code:: sh

   # $tmpdir1, $tmpdir2 are set up by speedoc.
   # -bman: build a man page; -q: quietly; -Dextensions: extensions used.
   python -msphinx \
      $tmpdir1 $tmpdir2 \
      -bman -q \
      -Dextensions=sphinx.ext.autodoc,sphinx.ext.autosummary,sphinx.ext.napoleon

and a minimal ``conf.py`` (``man_pages = [("contents", obj_name, "\n", "",
"3")]``).  To use, e.g., numpydoc_ instead of sphinx.ext.napoleon_, call

.. code:: sh

   speedoc -Dextensions=sphinx.ext.autodoc,sphinx.ext.autosummary,numpydoc \
      obj.to.document

(sphinx.ext.autodoc_ must always be listed, and sphinx.ext.autosummary_
is a dependency of numpydoc_).

.. _numpydoc: https://numpydoc.readthedocs.io
.. _sphinx.ext.autodoc: http://www.sphinx-doc.org/ext/autodoc.html
.. _sphinx.ext.autosummary: http://www.sphinx-doc.org/ext/autosummary.html
.. _sphinx.ext.napoleon: http://www.sphinx-doc.org/ext/napoleon.html

Troubleshooting
---------------

:Q: Docstrings are rendered terribly!
:A: Invalid RST formatting is very common :-(
