from setuptools import setup


setup(
    name="speedoc",
    description="sphinx meets pydoc.",
    long_description=open("README.rst", encoding="utf-8").read(),
    url="https://github.com/anntzer/speedoc",
    author="Antony Lee",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Topic :: Documentation",
    ],
    py_modules=["_speedoc"],
    package_dir={"": "lib"},
    python_requires=">=3.5",
    setup_requires=["setuptools_scm"],
    use_scm_version=lambda: {  # xref pypi2pkgbuild.py
        "version_scheme": "post-release",
        "local_scheme": "node-and-date",
    },
    install_requires=["sphinx>=1.7"],  # sphinx-doc/sphinx#4233.
    entry_points={"console_scripts": ["speedoc = _speedoc:main"]},
)
