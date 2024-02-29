from setuptools import setup

setup(name='praetor2',
      version='1.2',
      python_requires='>=2.7',
      description='Automatic Generation of Provenance from Python Scripts',
      url='https://gitlab.mpcdf.mpg.de/PRAETOR/prov-PRAETOR_public/',
      author='Michael Johnson',
      author_email='michael.johnson0100@gmail.com',
      license='MIT',
      packages=['praetor2'],
      install_requires=['codegen','memory_profiler','pymongo','rdflib','pandas'],
      scripts=['bin/praetor_run.py','bin/add_quality.py'],
      zip_safe=False)

