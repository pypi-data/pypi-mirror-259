import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="gcpds-docs",
    version='0.5',
    packages=["gcpds", "gcpds.docs"],
    author="Yeison Cardona",
    author_email="yencardonaal@unal.edu.co",
    maintainer="Yeison Cardona",
    maintainer_email="yencardonaal@unal.edu.co",
    download_url='',
    install_requires=[
        'ipywidgets',
        'ipython_secrets',
    ],
    scripts=[
    ],
    include_package_data=True,
    license='Simplified BSD License',
    description="",
    zip_safe=False,
    long_description=README,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',

    # https://pypi.org/classifiers/
    classifiers=[
    ],
)

