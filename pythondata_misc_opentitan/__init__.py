import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8771"
version_tuple = (0, 0, 8771)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8771")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8659"
data_version_tuple = (0, 0, 8659)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8659")
except ImportError:
    pass
data_git_hash = "eecccf35aa9a8d94bc6acb4ebd876e08bffcdf86"
data_git_describe = "v0.0-8659-geecccf35a"
data_git_msg = """\
commit eecccf35aa9a8d94bc6acb4ebd876e08bffcdf86
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Nov 19 12:01:51 2021 +0000

    Revert "[kmac] Use Empty signal from FIFO"
    
    This reverts commit 0e0c1a99f5a45584017d42bc8cba0aa376745908.
    
    The change appears to have broken the CW310 CI tests
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
