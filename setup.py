# :----------------------------------------------------------------------- INFO
# :[Snake-Vault-Flask/setup.py]
# :author        : fantomH
# :created       : 2024-08-16 17:25:00 UTC
# :updated       : 2024-08-16 17:25:04 UTC
# :description   : Setup script for Snake-Vault-Flask.

from setuptools import (
    setup,
    find_packages
)

setup(
    name='Snake-Vault-Flask',
    version='1.0.0',
    author="Pascal Malouin",
    author_email="pascal.malouin@gmail.com",
    description="Miscellaneous Flask utils.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fantomH/Snake-Vault-Flask/",
    
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
    ]
)
