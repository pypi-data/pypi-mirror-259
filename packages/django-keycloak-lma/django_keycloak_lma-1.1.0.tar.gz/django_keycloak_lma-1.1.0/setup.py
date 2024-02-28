from setuptools import setup, find_packages

setup(name='django_keycloak_lma',
      version='1.1.0',
      description='Modified version of the package django_keycloak (0.1.1)',
      long_description='Modified version of the package django_keycloak (0.1.1)',
      author='Vyacheslav Konovalov',
      packages=find_packages(),
      install_requires=[
            'djangorestframework',
            'python-keycloak-client-pkg',
      ],
      include_package_data=True,
      zip_safe=False)
