import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DFRobot_GP8403",
    keywords = 'Raspberry Pi, Raspi, Python, GPIO, GP8403, DAC',
    version="0.1.1",
    author="Joel Klein",
    description="This package is a fork of the DFRobot GP8403 package, modified for python3 and packaged for pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joe2824/DFRobot_GP8403/",
    project_urls={
        "Bug Tracker": "https://github.com/joe2824/DFRobot_GP8403/issues",
        "Github": "https://github.com/joe2824/DFRobot_GP8403/",
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: POSIX :: Linux",
    ],
    packages=['DFRobot'],
    python_requires=">=3",
    install_requires=[
          'smbus2'
      ]
)
