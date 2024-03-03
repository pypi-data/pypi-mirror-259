import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="uav-hud",
    version="0.0.2",
    author="Nurullah Eren Acar",
    author_email="n.erenacar13@gmail.com",
    description="A frame wrapper project that adds hud for UAVs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/0EA/uav-hud",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)