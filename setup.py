from setuptools import setup


if __name__ == "__main__":
    setup(
        name="speedoc",
        description="sphinx meets pydoc.",
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
        entry_points={"console_scripts": ["speedoc = _speedoc:main"]},
        install_requires=["sphinx>=1.5"],  # sphinx-doc/sphinx#1911.
    )
