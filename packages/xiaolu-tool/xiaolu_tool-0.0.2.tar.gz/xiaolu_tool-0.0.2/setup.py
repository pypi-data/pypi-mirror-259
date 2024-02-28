import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiaolu_tool",
    version="0.0.2",
    author="xiaolu-developer",
    author_email="liuyueqingyun@gmail.com",
    description="A tool for xiaolu data server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject"   内部项目不需要加url,
    packages=setuptools.find_packages(where="src/xiaolu_common"),
    package_dir={"": "src/xiaolu_common"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
