from cx_Freeze import setup, Executable

executables = [Executable('virus.py')]

setup(name='ДЗ->История',
      version='0.0.1',
      description='История',
      executables=executables,
      install_requires=['kivy'])


