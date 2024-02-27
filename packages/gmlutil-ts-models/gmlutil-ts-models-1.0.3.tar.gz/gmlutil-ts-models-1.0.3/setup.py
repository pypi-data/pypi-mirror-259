from setuptools import setup

setup(
    name='gmlutil-ts-models',
    version='1.0.3',    
    description='General Machine Learning Utility Package for Timeseries Models',
    url='https://github.com/Phillip1982/gmlutil_ts_models',
    author='Phillip Kim',
    author_email='phillip.kim@ejgallo.com',
    license='BSD 2-clause', ## Change this
    packages=['gmlutil_ts_models'],
    install_requires=[ # package>=0.2,<0.3
		# 'numpy>=1.19.5,<1.23.0',
		'pandas>=1.3.5,<1.4.3',
        'statsmodels>=0.12.2',
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
