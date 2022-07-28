import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13319"
version_tuple = (0, 0, 13319)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13319")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13177"
data_version_tuple = (0, 0, 13177)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13177")
except ImportError:
    pass
data_git_hash = "12e8112f85267dd2ee34f0d7d596a0ade839aa7e"
data_git_describe = "v0.0-13177-g12e8112f85"
data_git_msg = """\
commit 12e8112f85267dd2ee34f0d7d596a0ade839aa7e
Author: Alexander Williams <awill@google.com>
Date:   Tue Jul 19 17:17:25 2022 -0700

    [doc] Show how to use JTAG with the CW310
    
    Add some instructions for connecting the debugger and setting the TAP
    straps.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
