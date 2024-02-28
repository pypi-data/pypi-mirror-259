from setuptools import setup, find_packages, Extension

ext = Extension(
    name='ipdb.ipdb',  # 'mypackage.mymodule'
    sources=['src/ipdb/py-ipdb.c', 'src/ipdb/ipdb.c'],  # list of source files (to compile)
    include_dirs=['src/ipdb'],  # list of directories to search for C/C++ header files (in Unix form for portability)
    extra_link_args=["-ljson-c"],
    py_limited_api=True  # opt-in flag for the usage of Python's limited API <python:c-api/stable>.
)

setup_args = dict(
    name='ipip-ipdb-hp',
    version="0.1.0",
    packages=find_packages(where="src"),  # list
    package_dir={"": "src"},  # mapping
    ext_modules=[ext],  # list
    scripts=[]  # list
)

setup(**setup_args)
