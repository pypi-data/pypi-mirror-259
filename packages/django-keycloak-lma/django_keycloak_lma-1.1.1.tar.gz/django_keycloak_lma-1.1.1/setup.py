from setuptools import setup, find_packages

setup(name='django_keycloak_lma',
      version='1.1.1',
      description='Modified version of the package django_keycloak (0.1.1)',
      long_description='Available features:'
                       '- basic auth with token request (KeycloakPasswordAuthentication)'
                       '- bearer token auth (KeycloakTokenAuthentication)',
      author='Vyacheslav Konovalov',
      packages=find_packages(),
      install_requires=[
            'djangorestframework',
            'python-keycloak-client-pkg',
      ],
      include_package_data=True,
      zip_safe=False)
