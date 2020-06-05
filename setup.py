from setuptools import setup

setup(name="Qt.py-stubs",
      version="0.0.1",
      description="PySide2 stubs for Qt.py IDE autocomplete or intellisense",
      license='MIT',
      author="Matias Codesal",
      author_email="matias.codesal@gmail.com",
      url='https://github.com/matiascodesal/Qt.py-stubs',
      packages=['Qt'],
      package_data={
            'Qt': ['*.pyi']
      },
      install_requires=[
            'Qt.py'
      ]
)