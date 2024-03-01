import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "aws_analytics_reference_architecture",
    "version": "2.12.13",
    "description": "aws-analytics-reference-architecture",
    "license": "MIT-0",
    "url": "https://aws-samples.github.io/aws-analytics-reference-architecture/",
    "long_description_content_type": "text/markdown",
    "author": "Amazon Web Services",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/aws-samples/aws-analytics-reference-architecture.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "aws_analytics_reference_architecture",
        "aws_analytics_reference_architecture._jsii"
    ],
    "package_data": {
        "aws_analytics_reference_architecture._jsii": [
            "aws-analytics-reference-architecture@2.12.13.jsii.tgz"
        ],
        "aws_analytics_reference_architecture": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib==2.130.0",
        "aws-cdk.aws-glue-alpha==2.130.0.a0",
        "aws-cdk.aws-redshift-alpha==2.130.0.a0",
        "constructs>=10.3.0, <11.0.0",
        "jsii>=1.94.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
