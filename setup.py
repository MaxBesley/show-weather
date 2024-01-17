import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()

setuptools.setup(
    name="show-weather",
    version="0.0.1",
    author="Max Besley",
    author_email="besleymax@gmail.com",
    description=("Tells you the weather of any city/town anywhere in the world over the command line."),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaxBesley/show-weather",
    project_urls={
        "Bug Tracker": "https://github.com/MaxBesley/show-weather/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["requests"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "show-weather = show_weather.show_weather:main",
        ]
    }
)
