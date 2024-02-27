# -*- coding: UTF-8 -*-

import setuptools

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="fyang_utils",
    version="0.0.1.3",
    description=long_description,
    long_description_content_type="text/markdown",
    author="fyang",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'loguru',
        'configparser==5.0.2',
        'pymongo==3.12.0',
        'PyMySQL==1.0.2',
        'DateTime==4.3',
        'redis==3.5.3',
        'DBUtils==1.3',
        'clickhouse_driver==0.2.2',
        'APScheduler==3.8.0',
        'oss2==2.15.0',
        'kafka-python==2.0.2',
        'xhtml2pdf==0.2.5',
        'Jinja2==2.11.3',
        'odps==3.5.1',
        'openpyxl==3.0.9',
        'netifaces==0.11.0',
        'nacos-sdk-python==0.1.6'
    ],
    python_requires=">=3.6",
    zip_safe=True,

)
# import setuptools
#
#
#
# setuptools.setup(
#     name="example-pkg-YOUR-USERNAME-HERE",
#     version="0.0.1",
#     author="Example Author",
#     author_email="author@example.com",
#     description="A small example package",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/pypa/sampleproject",
#     project_urls={
#         "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
#     },
#     classifiers=[
#         "Programming Language :: Python :: 3",
#         "License :: OSI Approved :: MIT License",
#         "Operating System :: OS Independent",
#     ],
#     package_dir={"": "src"},
#     packages=setuptools.find_packages(where="src"),
#
# )
