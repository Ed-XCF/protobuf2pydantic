import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    install_requires = fh.read().splitlines()

with open("version", "r") as fh:
    version = fh.read()

setuptools.setup(
    name="protobuf2pydantic",
    version=version,
    author="Ed__xu__Ed",
    author_email="m.tofu@qq.com",
    description="Generate a file which include pydantic models by protobuf.pb2 file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ed-XCF/protobuf2pydantic",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=install_requires,
    entry_points={"console_scripts": ["pb2py = protobuf2pydantic.main:app"]}
)
