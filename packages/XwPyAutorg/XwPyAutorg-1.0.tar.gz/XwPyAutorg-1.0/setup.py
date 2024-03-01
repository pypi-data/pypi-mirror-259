from distutils.core import  setup
import setuptools
packages = ['XwPyAutorg']# 唯一的包名，自己取名
setup(name='XwPyAutorg',
	version='1.0',
	author='xiaowang',
    description="...[非常NB]反正",
    author_email='wzxddzyj1@outlook.com',
    packages=packages, 
    package_dir={'requests': 'requests'},)
