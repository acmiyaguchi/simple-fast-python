from distutils.core import setup

setup(
    name="simple-python",
    version="1.0",
    description="An implementation of the SiMPle algorithm",
    author="Anthony Miyaguchi",
    author_email="acmiyaguchi@gmail.com",
    url="https://github.com/acmiyaguchi/simple-python",
    packages=["simple"],
    install_requires=[
        "numpy",
    ],
)
