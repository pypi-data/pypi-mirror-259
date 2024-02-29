from setuptools import setup, find_packages

setup(
    name='Model3501Grpcapi',
    version='0.1.0',
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
)
