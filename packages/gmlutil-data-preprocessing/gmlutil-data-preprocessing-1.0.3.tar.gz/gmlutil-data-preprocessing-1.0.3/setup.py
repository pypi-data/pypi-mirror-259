from setuptools import setup

setup(
    name='gmlutil-data-preprocessing',
    version='1.0.3',    
    description='General Machine Learning Utility Package for Data Preprocessing',
    url='https://github.com/Phillip1982/gmlutil_data_preprocessing',
    author='Phillip Kim',
    author_email='phillip.kim@ejgallo.com',
    license='BSD 2-clause', ## Change this
    packages=['gmlutil_data_preprocessing'],
    install_requires=[
		'numpy>=1.19.5,<1.23.0',
		'pandas>=1.3.5,<1.4.3'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
		'Operating System :: MacOS',
		'Operating System :: Microsoft :: Windows :: Windows XP',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
