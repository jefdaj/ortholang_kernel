from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='ortholang_kernel',
    version='0.1',
    packages=['ortholang_kernel'],
    description='OrthoLang kernel for Jupyter',
    long_description=readme,
    author='Jeffrey David Johnson',
    author_email='jefdaj@berkeley.edu',
    url='https://github.com/jefdaj/ortholang_kernel',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
