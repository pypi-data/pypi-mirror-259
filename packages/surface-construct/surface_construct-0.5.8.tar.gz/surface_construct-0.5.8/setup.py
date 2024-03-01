from setuptools import setup

install_requires = [
    'ase',
    'networkx',
    'numpy',
    'spglib',
    'pandas',
    'tqdm',
    'matplotlib',
    'scipy',
    'scikit-learn',
]

setup(
    name='surface_construct',
    version='0.5.8',
    packages=['surface_construct'],
    url='https://gitee.com/pjren/surface_construct/',
    license='GPL',
    author='ren',
    author_email='0403114076@163.com',
    description='Surface termination construction especially for complex model, such as oxides or carbides.',
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
)
