import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8439"
version_tuple = (0, 0, 8439)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8439")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8327"
data_version_tuple = (0, 0, 8327)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8327")
except ImportError:
    pass
data_git_hash = "71bf7aad9531669f0cfafc923938775ae34d0562"
data_git_describe = "v0.0-8327-g71bf7aad9"
data_git_msg = """\
commit 71bf7aad9531669f0cfafc923938775ae34d0562
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Oct 22 06:40:20 2021 -0700

    [entropy_src/rtl] lint cleanup after mubi updates
    
    Removed unneeded signals after MuBi updates were made.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
