from setuptools import find_packages, setup

setup(
    name="prjpath",
    version="1.0.1",
    py_modules=['prjpath'],
    description='A library designed to help you easily locate the path of your project',
    long_description='project_path is a Python library designed to help you easily locate the path of your project by searching for specific files in the current directory and its parent directories.',
    url='https://github.com/alfredo000008/project_path',
    author='Alfredo Gallegos',
    author_email='alfredogasa1996@gmail.com',

    license='MIT',

    # See https://PyPI.python.org/PyPI?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],

    keywords='path',
    packages=find_packages(),
    install_requires=['inspect', 'os', 'sys'] 
)