from setuptools import setup, find_packages


setup(name='receipt_generator', version='0.0.1', author='Gabe De Oliveira',
      description='Simple Products Receipt Generator',
      packages=find_packages(exclude=['tests']),
      scripts=['receipt_generator.py',],
      include_package_data=True,
      tests_require=['nose>=1.3.0'],
      test_suite='nose.collector',
     )
