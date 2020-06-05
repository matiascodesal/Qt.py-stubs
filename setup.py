import os
from setuptools.command.install import install
from setuptools import setup, find_packages


class PostLinkInstallCommand(install):
      def run(self):
            install.run(self)
            qt_py_module = os.path.join(self.install_libbase, "Qt.py")
            qt_py_pkg = os.path.join(self.install_libbase, "Qt", "__init__.py")
            os.remove(qt_py_pkg)
            os.link(qt_py_module, qt_py_pkg)

setup(name="Qt.py-stubs",
      version="0.0.1",
      description="PySide2 stubs for Qt.py IDE autocomplete or intellisense",
      license='MIT',
      author="Matias Codesal",
      author_email="matias.codesal@gmail.com",
      url='https://github.com/matiascodesal/Qt.py-stubs',
      packages=find_packages(),
      package_data={
            '': ['*.pyi']
      },
      install_requires=[
            'Qt.py'
      ],
      cmdclass={
            'install': PostLinkInstallCommand,
      }
)