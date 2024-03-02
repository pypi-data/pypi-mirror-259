from setuptools import setup
# from setuptools.command.install import install as _install
# from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
import sys

__version__ = "1.26.2"

# class install(_install):
#     def finalize_options(self):
#         super().finalize_options()
#         if not self.distribution.install_requires:
#             self.distribution.install_requires = list()

#         self.distribution.install_requires.append(
#             f"numpy @ https://dekhtiarjonathan.github.io/pipserver/numpy/numpy-{__version__}-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
#         )

# class bdist_wheel(_bdist_wheel):
#     def finalize_options(self):
#         super().finalize_options()
#         if not self.distribution.install_requires:
#             self.distribution.install_requires = list()

#         self.distribution.install_requires.append(
#             f"numpy @ https://dekhtiarjonathan.github.io/pipserver/numpy/numpy-{__version__}-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
#         )


# cmdclass = {
#     "install": install,
#     "bdist_wheel": bdist_wheel
# }

print(sys.argv)


setup(
    name='jd_yolo',   # PyPI
    version=__version__,
    # cmdclass=cmdclass
    install_requires=None if "sdist" in sys.argv else [
        f"numpy @ https://dekhtiarjonathan.github.io/pipserver/numpy/numpy-{__version__}-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl"
    ]
)
