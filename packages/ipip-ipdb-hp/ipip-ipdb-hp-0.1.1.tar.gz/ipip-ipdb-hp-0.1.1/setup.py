from setuptools import setup, find_packages, Extension

ext = Extension(
    name='ipdb.ipdb',  # 'mypackage.mymodule'
    sources=['src/ipdb/py-ipdb.c', 'src/ipdb/ipdb.c'],  # list of source files (to compile)
    include_dirs=['src/ipdb'],  # list of directories to search for C/C++ header files (in Unix form for portability)
    extra_link_args=["-ljson-c"],
    py_limited_api=True  # opt-in flag for the usage of Python's limited API <python:c-api/stable>.
)

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup_args = dict(
    name='ipip-ipdb-hp',
    version="0.1.1",
    author="MagicBear",
    author_email="magicbearmo@gmail.com",
    description="IPIP.net non-officially supported IP database ipdb format parsing library",
    long_description=long_description,
    long_description_content_type='text/markdown',
    requires_python=">=3.7",
    keywords=["ipdb", "ipip"],
    license="Apache-2.0",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(where="src"),  # list
    package_dir={"": "src"},  # mapping
    ext_modules=[ext],  # list
    url='https://github.com/magicbear/ipip-ipdb-hp',
    scripts=[]  # list
)

setup(**setup_args)
