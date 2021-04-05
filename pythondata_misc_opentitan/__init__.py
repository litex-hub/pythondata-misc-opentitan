import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5714"
version_tuple = (0, 0, 5714)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5714")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5619"
data_version_tuple = (0, 0, 5619)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5619")
except ImportError:
    pass
data_git_hash = "551695c501766bcc10a64fff1ba714720e62e349"
data_git_describe = "v0.0-5619-g551695c50"
data_git_msg = """\
commit 551695c501766bcc10a64fff1ba714720e62e349
Author: Jake Ke <jackieke724@hotmail.com>
Date:   Fri Jan 22 14:22:38 2021 +0800

    [util/simplespi] PyFtdi updated, remove '.tobytes()' for spi read
    
    Signed-off-by: Jake Ke <jackieke724@hotmail.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
