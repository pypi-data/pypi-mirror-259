from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name="de-logging",
    version="0.0.1",
    author="Alex Johnson",
    author_email="alex@plotly.com",
    url="https://plotly.com/dash/",
    packages=["de_logging"],
    license="Commercial",
    description="A public stub for de-logging by Plotly",
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Dash",
    ],
)
