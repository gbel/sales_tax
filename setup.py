from setuptools import setup, find_packages


setup(name='sales_tax', version='0.0.1', author='Gabe De Oliveira',
      description='Simple Products Receipt Generator',
      packages=find_packages(exclude=['tests']),
      scripts=['sales.py',],
      include_package_data=True,
      tests_require=['nose>=1.3.0'],
      test_suite='nose.collector',
     )
