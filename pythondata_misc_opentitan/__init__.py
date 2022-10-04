import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14549"
version_tuple = (0, 0, 14549)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14549")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14407"
data_version_tuple = (0, 0, 14407)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14407")
except ImportError:
    pass
data_git_hash = "2512ca0da80635a4677c522b1f8b8b8d5bc23789"
data_git_describe = "v0.0-14407-g2512ca0da8"
data_git_msg = """\
commit 2512ca0da80635a4677c522b1f8b8b8d5bc23789
Author: Weicai Yang <weicai@google.com>
Date:   Mon Oct 3 17:00:07 2022 -0700

    [spi_device/dv] Add tpm_read_hw_reg test and update scb to check HW regs
    
    1. Create a test that has both SW and host access the HW regs to test #15134
    2. Consolidate tpm init tasks
    3. Update scb to allow SPI host to read back either the new value or the old one.
    
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
