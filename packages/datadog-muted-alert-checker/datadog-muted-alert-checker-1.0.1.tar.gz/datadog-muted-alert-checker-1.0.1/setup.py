from setuptools import setup


setup(
    name="datadog-muted-alert-checker",
    version="1.0.1",
    license="MIT",
    url="https://github.com/zackzonexx/datadog-muted-alert-checker.git",
    author="Zackzonexx",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    author_email="zackzonexx@gmail.com",
    packages=["package"],
    keywords="Datadog Muted Alert Checker",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Natural Language :: English",
    ],
    install_requires=[
        "datadog",
        "opsgenie-sdk",
        "requests",
        "urllib3",
        "google-auth",
        "google-auth-httplib2",
        "google-api-python-client",
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "datadog-checker=package.main:main",
        ],
    },
)
