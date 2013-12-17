import setuptools

packages = [
    'cube2demo',
]

setuptools.setup(
    name="pycube2demo",
    version="0.1",
    packages=packages,
    package_dir={'' : 'src'},
    install_requires=['pycube2common', 'pycube2protocol'],
    author="Chasm",
    author_email="fd.chasm@gmail.com",
    url="https://github.com/fdChasm/cube2demo",
    license="MIT",
    description="Python library for reading and writing Cube 2 demos.",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English"
    ],
)
