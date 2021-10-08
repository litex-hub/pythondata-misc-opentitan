import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8183"
version_tuple = (0, 0, 8183)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8183")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8071"
data_version_tuple = (0, 0, 8071)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8071")
except ImportError:
    pass
data_git_hash = "9e78b5edd198756bb6b55369b843ed7553a8bd1d"
data_git_describe = "v0.0-8071-g9e78b5edd"
data_git_msg = """\
commit 9e78b5edd198756bb6b55369b843ed7553a8bd1d
Author: Udi Jonnalagadda <udij@google.com>
Date:   Tue Aug 17 20:01:56 2021 -0700

    [dv/cdc] CDC simulation model
    
    This PR adds an initial draft of a CDC simulation model.
    
    This module should be instantiated inside of CDC synchronization
    primitives, and is used to inject random data delays into the
    synchronizers to more accurately model real CDC delays.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
