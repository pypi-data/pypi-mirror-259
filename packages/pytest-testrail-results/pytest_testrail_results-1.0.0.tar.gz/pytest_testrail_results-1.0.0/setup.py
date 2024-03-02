from setuptools import setup


def read_file(fname):
    with open(fname) as f:
        return f.read()


setup(
    name='pytest_testrail_results',
    description='pytest plugin for creating TestRail runs and adding results',
    long_description=read_file('README.rst'),
    version='1.0.0',
    author='Oleg_Miroshnychenko',
    author_email='miroshnychenko@dnt-lab.com',
    packages=[
        'pytest_testrail_results',
    ],
    package_dir={'': 'src'},
    install_requires=[
        'pytest>=3.8',
        'requests>=2.30.0',
    ],
    include_package_data=True,
    entry_points={'pytest11': ['pytest-testrail = pytest_testrail_results.conftest']},
)