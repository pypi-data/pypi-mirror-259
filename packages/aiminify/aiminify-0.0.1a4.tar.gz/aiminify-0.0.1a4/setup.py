
from setuptools import setup
from setuptools.command.install import install

class CustomInstallCommand(install):

    def run(self):
        raise Exception("This package should not be installed. Contact support@aiminify.com for further information.")


setup(
    name='aiminify',
    version='0.0.1a4',
    description='This package should not be installed. Contact support@aiminify.com for further information.',
    author='aiminify',
    author_email='support@aiminify.com',
    url='',
    cmdclass={
        'install': CustomInstallCommand,
    }
) 

