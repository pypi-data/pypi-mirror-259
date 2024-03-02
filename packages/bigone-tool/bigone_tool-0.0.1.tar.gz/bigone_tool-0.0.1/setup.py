import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bigone_tool", # Replace with your own username
    version="0.0.1",
    author="lilasxie",
    author_email='thanklilas@163.com',
    maintainer="lilasxie",
    maintainer_email="thanklilas@163.com",
    url = "https://github.com/lilasxie/bigone_tool",
    description="An python3 library for bigone commonly used function",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
