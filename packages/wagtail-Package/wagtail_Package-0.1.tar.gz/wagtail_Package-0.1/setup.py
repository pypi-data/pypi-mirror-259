from setuptools import setup,find_packages

with open("README.md","r") as f:
    description=f.read()
    
    
setup(
    name='wagtail_Package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Wagtail==5.2.3',
        # Other dependencies go here
    ],
    classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',

author='auth',
author_email='bipuldawadi14@email.com',
license='MIT',
zip_safe=False)
