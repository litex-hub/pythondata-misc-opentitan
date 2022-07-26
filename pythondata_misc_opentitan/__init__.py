import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13265"
version_tuple = (0, 0, 13265)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13265")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13123"
data_version_tuple = (0, 0, 13123)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13123")
except ImportError:
    pass
data_git_hash = "9595dea00edadf0c90c1b93d8ecfb1e42ffd930e"
data_git_describe = "v0.0-13123-g9595dea00e"
data_git_msg = """\
commit 9595dea00edadf0c90c1b93d8ecfb1e42ffd930e
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Mon Jul 25 12:11:04 2022 -0700

    [entropy_src/rtl] add recov alert for FW_OV_WR error
    
    A recoverable alert has been added in the case where the packer FIFO
    has been written but was full at the time.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
