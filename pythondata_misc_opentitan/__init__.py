import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14577"
version_tuple = (0, 0, 14577)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14577")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14435"
data_version_tuple = (0, 0, 14435)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14435")
except ImportError:
    pass
data_git_hash = "883c2711350a72ff8172cfe01b0b07c903d61b25"
data_git_describe = "v0.0-14435-g883c271135"
data_git_msg = """\
commit 883c2711350a72ff8172cfe01b0b07c903d61b25
Author: Weicai Yang <weicai@google.com>
Date:   Tue Oct 4 15:05:56 2022 -0700

    [spi_device/dv] Enable testing unaligned address when read TPM HW regs
    
    1. Enabled testing unaligned address when read TPM HW regs
    2. updated scb to support to drop HW reg write when host writes invalid locality
    
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
