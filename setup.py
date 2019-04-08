from setuptools import setup

setup(
    name="pynegin",
    version="0.1",
    description="Pure Python Game Engine On Top Of PyGame",
    author="Wilfred",
    author_email="_",
    packages=["pynegin"],
    install_requires=["pygame", "Pillow"],
    url="http://wilfred-kun.github.io/pynegin",
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    project_urls={
        "Documentation": "http://wilfred-kun.github.io/pynegin",
        "Source": "https://github.com/wilfred-kun/pynegin"
    }
)
