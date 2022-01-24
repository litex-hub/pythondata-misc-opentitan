import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9719"
version_tuple = (0, 0, 9719)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9719")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9597"
data_version_tuple = (0, 0, 9597)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9597")
except ImportError:
    pass
data_git_hash = "e5aa269c0215cb762ac537ea711b2e6318271448"
data_git_describe = "v0.0-9597-ge5aa269c0"
data_git_msg = """\
commit e5aa269c0215cb762ac537ea711b2e6318271448
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Jan 24 15:27:02 2022 +0000

    Revert "[flash_ctrl] D2 preparation steps"
    
    This reverts commit f166105, which has broken the CW305 build because
    Vivado (wrongly?) infers a combo loop on the sparse FSM.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
