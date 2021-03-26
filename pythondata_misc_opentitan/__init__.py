import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5603"
version_tuple = (0, 0, 5603)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5603")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5508"
data_version_tuple = (0, 0, 5508)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5508")
except ImportError:
    pass
data_git_hash = "26215746ec72774c540e4e8076f29e3d1a918eb1"
data_git_describe = "v0.0-5508-g26215746e"
data_git_msg = """\
commit 26215746ec72774c540e4e8076f29e3d1a918eb1
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Wed Mar 17 16:47:09 2021 -0700

    [entropy_src/rtl] sha3 block added as conditioner
    
    Replacing the placeholder FIFO with the kmac sha3 module.
    Updated documentation for window going from 1024 to 2048 samples.
    Update the main state machine will new flow.
    Uniquified the local parameters related to the sha3 block.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
