import os
import tempfile

from setuptools import setup
from urllib.request import urlopen
import shutil

from wheel.bdist_wheel import bdist_wheel as _bdist_wheel

__version__ = "2.7.2"

__bin_wheel_host__ = "http://sqrl.nvidia.com/nvdl/usr/jdekhtiar/pipserver/"
__bin_wheel_filename__ = f"dummy_nccl-{__version__}-py3-none-manylinux1_x86_64.whl"


class bdist_wheel(_bdist_wheel):
    def run(self):

        with tempfile.TemporaryDirectory() as temp_dir:

            whl_target = temp_dir + "/" + __bin_wheel_filename__
            print(f"{whl_target=}")

            remotefile = urlopen(__bin_wheel_host__ + __bin_wheel_filename__)
            with open(whl_target, 'wb') as f:
                f.write(remotefile.read())

            if not os.path.exists(self.dist_dir):
                os.makedirs(self.dist_dir)

            shutil.copy(
                src=whl_target,
                dst=os.path.join(self.dist_dir, __bin_wheel_filename__)
            )


__cmdclass__ = {
    "bdist_wheel": bdist_wheel
}


setup(
    name='dummy-nccl',
    version=__version__,
    cmdclass=__cmdclass__,
    # Necessary to avoid problems - do not remove.
    install_requires=[
        "wheel",
        "setuptools"
    ]
)
