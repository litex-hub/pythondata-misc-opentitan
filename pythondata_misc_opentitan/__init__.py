import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5172"
version_tuple = (0, 0, 5172)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5172")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5081"
data_version_tuple = (0, 0, 5081)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5081")
except ImportError:
    pass
data_git_hash = "50a83bedd4d6e3af8ef3c3696cf12fdbce53aaad"
data_git_describe = "v0.0-5081-g50a83bedd"
data_git_msg = """\
commit 50a83bedd4d6e3af8ef3c3696cf12fdbce53aaad
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Mon Feb 22 10:44:19 2021 -0800

    [csrng/rtl] internal state read timing improvements
    
    Re-structed the read flow for the internal state array.
    Added parameter to prim_fifo_sync to remove output mux.
    Added simple flops to break up configuration paths.
    Added fifo output mux back for genbits to prevent assertion.
    Cleaned up format for hjson file.
    Updated internal state rtl based on feedback.
    Fixed hjson register wording.
    Added comment for FIFO parameter use.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
