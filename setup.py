from setuptools import setup, find_packages

setup(
    name = 'pso',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        "ipython",
        "numpy",
        "matplotlib",
        "mako",
        "pyopencl",
    ],
    url = 'http://eardley.xyz',
    author = 'Steven Eardley',
    author_email = 'steve@eardley.xyz',
    description = 'Particle swarm optimisation with OpenCL',
    license = 'Copyheart',
    classifiers = [
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Copyheart',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)

