from setuptools import setup, Extension

bewcore_yespower_module = Extension('bewcore_yespower',
                            sources = ['yespower-module.c',
                                       'yespower.c',
                                       'yespower-opt.c',
                                       'sha256.c'
                                       ],
                            extra_compile_args=['-O2', '-funroll-loops', '-fomit-frame-pointer'],
                            include_dirs=['.'])

setup (name = 'bewcore_yespower',
       version = '1.0.1',
       author_email = 'mraksoll4@gmail.com',
       author = 'mraksoll',
       url = 'https://github.com/bewcore-project/bewcore_yespower_python3',
       description = 'Bindings for yespower-1.0.1 proof of work used by bewcore',
       ext_modules = [bewcore_yespower_module])
