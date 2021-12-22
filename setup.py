from distutils.core import setup, Extension

digibyte_scrypt_module = Extension('digibyte_scrypt',
                               sources = ['digibyte_scrypt/scryptmodule.c',
                                          'digibyte_scrypt/scrypt.c'],
                               include_dirs=['./digibyte_scrypt/'])

setup (
    name = 'digibyte_scrypt',
    version = '1.0.0',
    description = 'Bindings for scrypt proof of work used by DigiByte',
    classifiers=[
        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    ext_modules = [digibyte_scrypt_module]
)
