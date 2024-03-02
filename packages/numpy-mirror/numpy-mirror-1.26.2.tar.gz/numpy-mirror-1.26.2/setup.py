from setuptools import setup
import sys

__version__ = "1.26.2"


if __name__ == "__main__":

    setup(
        name='numpy-mirror',
        version=__version__,
    #     install_requires=[
    #         f"numpy @ https://dekhtiarjonathan.github.io/pipserver/numpy/numpy-{__version__}-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
    #     ]
    # )

        install_requires=None if "sdist" in sys.argv else [
            f"numpy_bin @ https://dekhtiarjonathan.github.io/pipserver/numpy/numpy-{__version__}-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
        ]
    )
