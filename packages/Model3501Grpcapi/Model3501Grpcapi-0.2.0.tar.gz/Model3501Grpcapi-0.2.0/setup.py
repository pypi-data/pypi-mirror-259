from setuptools import setup, find_packages
from setuptools.command.build_py import build_py
from setuptools.command.install import install
import subprocess

# Custom build command to compile protobuf files
class CustomBuildPy(build_py):
    def run(self):
        # Compile protobuf files
        subprocess.call(['protoc', '--python_out=./src', 'model3501.proto'])
        # Run default build command
        build_py.run(self)

# Custom install command to compile protobuf files before installation
class CustomInstall(install):
    def run(self):
        # Compile protobuf files
        packages=find_packages('src'),

        # Run default install command
        install.run(self)

setup(
    name='Model3501Grpcapi',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'grpcio',
        # Add any other dependencies here
    ],
    package_data={
        '': ['*.proto'],  # Include .proto files
    },
    entry_points={
        'console_scripts': [
            'model3501-server = src.server:main',  # Define entry point for server script
            'model3501-client = src.client:main',  # Define entry point for client script
        ],
    },
    # Metadata
    author='vinay',
    author_email='vinayn@mcci.com.com',
    description='Description of your package',
    url='https://github.com/vinaynmcci/Model3501Grpcapi',
    # Use custom build and install commands
    cmdclass={
        'build_py': CustomBuildPy,
        'install': CustomInstall,
    }
)
