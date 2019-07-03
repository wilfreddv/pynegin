from setuptools import setup, find_packages


with open("README.md", "rb") as f:
    long_desc = str(f.read())


PACKAGES = ['pynegin',
            'pynegin.components',
            'pynegin.constants'
           ]


setup(
    name="pynegin",
    version="0.3",
    description="Pure Python Game Engine On Top Of PyGame",
    long_description=long_desc,
    author="Wilfred",
    author_email="wilfred@programmer.net",
    packages=PACKAGES,
    install_requires=["pygame", "Pillow"],
    url="http://wilfred-kun.github.io/pynegin.html",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    project_urls={
        "Documentation": "http://wilfred-kun.github.io/pynegin",
        "Source": "https://github.com/wilfred-kun/pynegin.html"
    }
)
