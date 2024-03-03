from setuptools import setup, find_packages

VERSION = '0.0.7' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'This is a test package'

setup(
       # the name must match the folder name 'verysimplemodule'
        name="nikitosPackage1", 
        version=VERSION,
        author="Nikita Romm",
        author_email="nikitaromm@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        entry_points={
            'console_scripts': [
                'nikitosCommand = nikitosPackage.hello_module:main',
            ],
        },
        keywords=['python', 'first package'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)