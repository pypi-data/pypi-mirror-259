import setuptools

setuptools.setup(
    name="RequestParser",
    version="2024.1.0",
    author="dyn.lee",
    author_email="duyenle.201001@gmail.com",
    description="Parse the raw HTTP Request",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=open("requirements.txt").read().split(),
    url="",
    classifiers=[
		"Programming Language :: Python :: 3"
    ],
    keywords=["HTTP Request Parser"],
	packages=["RequestParser"],
)