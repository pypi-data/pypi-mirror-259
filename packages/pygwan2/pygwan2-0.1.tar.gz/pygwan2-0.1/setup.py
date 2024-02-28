from setuptools import setup, find_packages

setup(
    name="pygwan2",
    version="0.1",
    packages=find_packages(),
    description="since i lost the original package, i am trying to create a new one.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Tarmica Sean Chiwara",
    author_email="tarimicac+pypi@gmail.com",
    license="MIT",
    url="https://github.com/lordskyzw/pygwan2",
    install_requires=[
        "requests>=2.25.0",
        "colorama>=0.4.3",
        "requests_toolbelt>=0.9.1"
    ],
)
