from setuptools import setup

setup(
    author='Andrew Udvare',
    author_email='audvare@gmail.com',
    description=('Quickly track via SMS several USPS (and some international) '
                 'tracking numbers via the command line.'),
    entry_points={'console_scripts': [
        'usps-track = usps_track:main',
    ]},
    install_requires=['aiohttp>=3.7.2', 'argcomplete>=1.10.3'],
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    name='usps-track',
    py_modules=['usps_track'],
    url='https://github.com/Tatsh/usps-track',
    keywords=['cli', 'mail', 'shipping', 'sms', 'tracking', 'usps', 'utility'],
    version='v0.0.1',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Typing :: Typed',
    ])
