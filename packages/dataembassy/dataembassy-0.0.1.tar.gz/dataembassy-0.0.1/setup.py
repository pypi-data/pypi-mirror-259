from setuptools import setup
from setuptools.command.install import install


class AbortInstall(install):
    def run(self):
        raise SystemExit(
            "You're trying to install dataembassy from pypi, "
            "however, it can be installed only from a private repository. "
            "Please read the installation docs and contact your Anonos "
            "representative in case of any issues or questions."
        )


setup(
    cmdclass={
        "install": AbortInstall,
    },
)
