import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8652"
version_tuple = (0, 0, 8652)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8652")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8540"
data_version_tuple = (0, 0, 8540)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8540")
except ImportError:
    pass
data_git_hash = "6e61902d4be9ab56295112b411c4fe91a316b102"
data_git_describe = "v0.0-8540-g6e61902d4"
data_git_msg = """\
commit 6e61902d4be9ab56295112b411c4fe91a316b102
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Nov 8 16:42:52 2021 -0800

    [prim] Add time-out functionality to prim_clock_meas
    
    prim_clock_meas can now also detect if a clock has stopped.
    
    This is done for 2 reasons:
    
    1. clkmgr needs to have both clock presence and accuracy detection.
       The former was missed in a previous PR.
    
    2. The same module will be re-used for #8658, which needs a time-out
       mechanism.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
