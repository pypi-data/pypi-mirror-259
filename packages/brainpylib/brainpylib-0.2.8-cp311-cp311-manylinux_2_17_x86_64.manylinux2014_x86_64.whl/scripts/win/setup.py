# -*- coding: utf-8 -*-


try:
    from distutils import sysconfig
except ModuleNotFoundError:
    import sysconfig
import glob
import io
import os
import re
import subprocess
import sys

from setuptools import setup, find_namespace_packages
from setuptools.command.build_ext import build_ext

try:
  import pybind11
except ModuleNotFoundError:
  raise ModuleNotFoundError('Please install pybind11 before compiling brainpylib! '
                            '\n'
                            '> pip install pybind11')
from pybind11.setup_helpers import Pybind11Extension
try:
    import taichi as ti
    if ti.__version__ < (1, 7, 0):
        raise ModuleNotFoundError
except ModuleNotFoundError:
    taichi_installed = 'taichi' in globals()
    error_message = ('Please update taichi to 1.7.0 or above!' if taichi_installed else 
                     'Please install taichi before compiling brainpylib!')
    error_message += '\n> pip install -i https://pypi.taichi.graphics/simple/ taichi-nightly'
    raise ModuleNotFoundError(error_message)


# set taichi environments
taichi_path = ti.__path__[0]
taichi_c_api_install_dir = os.path.join(taichi_path, '_lib', 'c_api')
taichi_lib_dir = os.path.join(taichi_path, '_lib', 'runtime')

os.environ.update({
    'TAICHI_C_API_INSTALL_DIR': taichi_c_api_install_dir,
    'TI_LIB_DIR': taichi_lib_dir
})

build_ext.get_export_symbols = lambda *args: []

# version control
HERE = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(HERE, 'brainpylib', '__init__.py'), 'r') as f:
  init_py = f.read()
  __version__ = re.search('__version__ = "(.*)"', init_py).groups()[0]

# extension modules
if sys.platform == 'darwin':  # mac
  ext_modules = [
    Pybind11Extension("brainpylib/cpu_ops",
                      sources=glob.glob("lib/cpu_*.cc") + glob.glob("lib/cpu_*.cpp"),
                      cxx_std=11,
                      extra_link_args=["-rpath", re.sub('/lib/.*', '/lib', sys.path[1])],
                      define_macros=[('VERSION_INFO', __version__)]),
  ]
else:
  ext_modules = [
    Pybind11Extension("brainpylib/cpu_ops",
                      sources=glob.glob("lib/cpu_*.cc") + glob.glob("lib/cpu_*.cpp"),
                      cxx_std=11,
                      define_macros=[('VERSION_INFO', __version__)]),
  ]


# obtain long description from README
here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), 'r', encoding='utf-8') as f:
  README = f.read()


os.environ['pybind11_DIR'] = pybind11.get_cmake_dir()


class CMakeBuildExt(build_ext):
    def build_extensions(self):
        # First: configure CMake build
        import platform
        import sys
        import distutils.sysconfig

        import pybind11

        # Work out the relevant Python paths to pass to CMake, adapted from the
        # PyTorch build system
        if platform.system() == "Windows":
            cmake_python_library = "{}/libs/python{}.lib".format(
                distutils.sysconfig.get_config_var("prefix"),
                distutils.sysconfig.get_config_var("VERSION"),
            )
            if not os.path.exists(cmake_python_library):
                cmake_python_library = "{}/libs/python{}.lib".format(
                    sys.base_prefix,
                    distutils.sysconfig.get_config_var("VERSION"),
                )
        else:
            cmake_python_library = "{}/{}".format(
                distutils.sysconfig.get_config_var("LIBDIR"),
                distutils.sysconfig.get_config_var("INSTSONAME"),
            )
        cmake_python_include_dir = distutils.sysconfig.get_python_inc()

        install_dir = os.path.abspath(os.path.dirname(self.get_ext_fullpath("dummy")))
        os.makedirs(install_dir, exist_ok=True)
        cmake_args = [
            # "-DPYTHON_LIBRARY={}".format(os.path.join(sysconfig.get_config_var('LIBDIR'))),
            "-DPYTHON_INCLUDE_DIRS={}".format(sysconfig.get_python_inc()),
            "-DPYTHON_INCLUDE_DIR={}".format(sysconfig.get_python_inc()),
            "-DCMAKE_INSTALL_PREFIX={}".format(install_dir),
            "-DPython_EXECUTABLE={}".format(sys.executable),
            "-DPython_LIBRARIES={}".format(cmake_python_library),
            "-DPython_INCLUDE_DIRS={}".format(cmake_python_include_dir),
            "-DCMAKE_BUILD_TYPE={}".format("Debug" if self.debug else "Release"),
            "-DCMAKE_PREFIX_PATH={}".format(os.path.dirname(pybind11.get_cmake_dir())),
        ]
        if os.environ.get("BRAINPY_CUDA", "no").lower() == "yes":
            cmake_args.append("-BRAINPY_CUDA=yes")

        os.makedirs(self.build_temp, exist_ok=True)

        subprocess.check_call(["cmake"] + cmake_args + [HERE], cwd=self.build_temp)

        # Build all the extensions
        super().build_extensions()
        # Finally run install
        subprocess.check_call(["cmake", "--build", ".", "--target", "install", "-j24"], cwd=self.build_temp)

    def build_extension(self, ext):
        subprocess.check_call(["cmake", "--build", ".", "--target", "cpu_ops", "-j24"], cwd=self.build_temp)


# build
setup(
  name='brainpylib',
  version=__version__,
  description='C++/CUDA Library for BrainPy',
  long_description=README,
  long_description_content_type="text/markdown",
  author='BrainPy team',
  author_email='chao.brain@qq.com',
  packages=find_namespace_packages(exclude=['lib*', 'docs*', 'tests*', 'win_dll*', 'out*']),
  include_package_data=True,
  install_requires=[],
  extras_require={"test": "pytest"},
  python_requires='>=3.8,<3.12',
  url='https://github.com/brainpy/BrainPy',
  ext_modules=ext_modules,
  cmdclass={"build_ext": CMakeBuildExt},
  license='GPL-3.0 license',
  keywords=('event-driven computation, '
            'sparse computation, '
            'brainpy'),
  classifiers=[
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: Apache Software License',
    'Topic :: Scientific/Engineering :: Bio-Informatics',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Software Development :: Libraries',
  ],
)
