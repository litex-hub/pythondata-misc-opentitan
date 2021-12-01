import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8940"
version_tuple = (0, 0, 8940)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8940")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8828"
data_version_tuple = (0, 0, 8828)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8828")
except ImportError:
    pass
data_git_hash = "0fd56dd5658005d576a0440a268de6028818244e"
data_git_describe = "v0.0-8828-g0fd56dd56"
data_git_msg = """\
commit 0fd56dd5658005d576a0440a268de6028818244e
Author: Michael Schaffner <msf@google.com>
Date:   Tue Nov 30 12:54:12 2021 -0800

    [lc_ctrl] Correct invalid state error indication
    
    Fixes #9431
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
