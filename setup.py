from setuptools import setup, find_packages

setup_args=dict(
  name='python-yocto',
  packages=find_packages(),
)
setup(**setup_args)
