from setuptools import setup

with open('requirements.txt') as requirements_file:
    required = requirements_file.read().splitlines()

setup(
    name='sshmenu',
    version='0.1.0',
    license='MIT',
    description='Command line SSH menu and helper utility',
    long_description=open('README.rst').read(),
    author='Skiy Chan',
    author_email='skiychan@outlook.com',
    url='https://github.com/skiy/sshmenu',
    packages=['sshmenu'],
    install_requires=required,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        'console_scripts': ['sshmenu=sshmenu.sshmenu:main']
    }
)
