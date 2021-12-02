import pathlib
import setuptools


here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setuptools.setup(
    name="boptest_gym",
    version="0.1.0",
    packages= ["boptest_gym"],
    python_requires=">=3.6",
    install_requires=["pandas","numpy", "matplotlib", "gym", "scipy", "requests"]
)