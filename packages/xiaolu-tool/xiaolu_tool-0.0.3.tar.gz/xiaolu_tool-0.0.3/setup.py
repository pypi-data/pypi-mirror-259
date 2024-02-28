import os
import shutil

import setuptools

class CleanCommand(setuptools.Command):
    """Custom clean command to tidy up the project root."""
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')
        # 删除 __pycache__ 目录和 .pyc 文件
        for root, dirs, files in os.walk('.'):
            for dir in dirs:
                if dir == "__pycache__":
                    shutil.rmtree(os.path.join(root, dir))
            for file in files:
                if file.endswith('.pyc'):
                    os.remove(os.path.join(root, file))
        print("Cleaned up.")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiaolu_tool",
    version="0.0.3",
    author="xiaolu-developer",
    author_email="jiaboyu@xiaoluyy.com",
    description="A tool for xiaolu data server",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject"   内部项目不需要加url,
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    cmdclass={"clean": CleanCommand},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)


