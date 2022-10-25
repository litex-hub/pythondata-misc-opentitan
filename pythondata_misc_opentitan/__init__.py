import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14945"
version_tuple = (0, 0, 14945)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14945")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14803"
data_version_tuple = (0, 0, 14803)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14803")
except ImportError:
    pass
data_git_hash = "e01285f81810f08fa1c41988cff9ac75d901d7ea"
data_git_describe = "v0.0-14803-ge01285f818"
data_git_msg = """\
commit e01285f81810f08fa1c41988cff9ac75d901d7ea
Author: Weicai Yang <weicai@google.com>
Date:   Tue Oct 25 12:24:27 2022 -0700

    [spi_device/dv] Add test - spi_device_flash_and_tpm_min_idle
    
    It inherits from spi_device_flash_and_tpm_vseq and configure the min idle period btw 2 SPI items.
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
