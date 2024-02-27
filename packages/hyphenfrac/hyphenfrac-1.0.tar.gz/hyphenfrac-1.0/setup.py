from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    description = f.read()

setup(
    name="hyphenfrac",
    author="xyzpw",
    maintainer="xyzpw",
    version="1.0",
    classifiers=[
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
    ],
    url="https://github.com/xyzpw/hyphenfrac/",
    description="Uses a hyphen-minus character to visualize a fraction.",
    long_description=description,
    long_description_content_type="text/markdown",
)
