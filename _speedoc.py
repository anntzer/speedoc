"""speedoc - sphinx meets pydoc.
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import builtins
from collections.abc import Callable
from tempfile import TemporaryDirectory
import importlib
from pathlib import Path
import subprocess
import sys
import types


_templates = {
    "module": """\
.. automodule:: {obj}
   :members:
   :special-members: __init__
   :undoc-members:
""",
    "exception": """\
.. currentmodule:: {mod}

.. autoexception:: {obj}
   :members:
   :special-members: __init__
   :undoc-members:
""",
    "class": """\
.. currentmodule:: {mod}

.. autoclass:: {obj}
   :members:
   :special-members: __init__
   :undoc-members:
""",
    "function": """\
.. currentmodule:: {mod}

.. autofunction:: {obj}
""",
    "data": """\
.. currentmodule:: {mod}

.. autodata:: {obj}
""",
}


def main(argv=None):
    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        epilog="""\
Unknown flags are passed to `python -msphinx`.  For example, numpydoc rendering
can be obtained with

    %(prog)s -Dextensions=sphinx.ext.autodoc,sphinx.ext.autosummary,numpydoc ...
""")
    parser.add_argument("obj", help="object to document")
    args, rest = parser.parse_known_args(argv)
    if not all(opt.startswith("-") for opt in rest):
        parser.error("only one object can be documented at a time")

    parts = args.obj.split(".")
    mod = obj = builtins
    try:
        for i in range(len(parts)):
            mod = obj = importlib.import_module(".".join(parts[:i + 1]))
    except ImportError:
        for j in range(i, len(parts)):
            obj = getattr(obj, parts[j])

    template = _templates[
        "module" if isinstance(obj, types.ModuleType)
        else "exception"
            if isinstance(obj, type) and issubclass(obj, Exception)
        else "class" if isinstance(obj, type)
        else "function" if isinstance(obj, Callable)
        else "data"  # no support for automethod, autoattribute.
    ]
    with TemporaryDirectory() as tmpdir:
        Path(tmpdir, "conf.py").write_text(r"""\
# No description, no authors, section 3 ("library calls").
man_pages = [("contents", "{}", "\n", "", "3")]
""".format(args.obj))
        extensions = ["sphinx.ext.autodoc",
                      "sphinx.ext.autosummary",
                      "sphinx.ext.napoleon"]
        Path(tmpdir, "contents.rst").write_text(
            template.format(mod=mod.__name__, obj=args.obj))
        subprocess.run(
            [sys.executable, "-msphinx", ".", "build", "-bman", "-q",
             "-Dextensions=" + ",".join(extensions)] + rest,
            cwd=tmpdir, check=True)
        subprocess.run(["man", "build/{}.3".format(args.obj)], cwd=tmpdir)


if __name__ == "__main__":
    main()