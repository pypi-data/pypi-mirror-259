from setuptools import setup, find_packages

setup(
    name='qham',
    version='1.0.0',
    author='Kaushik Chintam',
    author_email='kaushikam12@gmail.com',
    description='A package for simulating quantum Hamiltonians.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yourpackagename',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.1',
        'qiskit>=0.7.0',
        'torch>=1.7.0',
        'scipy>=1.4.1',
        'matplotlib>=3.1.3',
        'pytest>=5.3.5',

    ],
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
    )
