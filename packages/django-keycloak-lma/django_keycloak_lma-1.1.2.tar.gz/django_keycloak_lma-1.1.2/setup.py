from setuptools import setup, find_packages

setup(name='django_keycloak_lma',
      version='1.1.2',
      description='Modified version of the package django_keycloak (0.1.1)',
      long_description='Available features:\n'
                       '- basic auth with token request (KeycloakPasswordAuthentication)\n'
                       '- bearer token auth (KeycloakTokenAuthentication)\n'
                       'Examples of using features: tests/lma',
      author='Vyacheslav Konovalov',
      packages=find_packages(),
      install_requires=[
            'djangorestframework',
            'python-keycloak-client-pkg',
      ],
      include_package_data=True,
      zip_safe=False)
