from setuptools import setup, find_packages

setup(
    name='django-south-admin',
    version='0.0.1',
    description='Django app/project skeleton.',
    long_description = open('README.rst', 'r').read() + open('AUTHORS.rst', 'r').read() + open('CHANGELOG.rst', 'r').read(),
    author='Shaun Sephton',
    author_email='shaun@28lines.com',
    license='BSD',
    url='http://github.com/praekelt/django-south-admin',
    packages = find_packages(),
    dependency_links = [
    ],
    install_requires=[
        'django',
        'django-object-tools',
        'south',
    ],
    tests_require=[
        'django-setuptest',
    ],
    test_suite="setuptest.setuptest.SetupTestSuite",
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    zip_safe=False,
)
