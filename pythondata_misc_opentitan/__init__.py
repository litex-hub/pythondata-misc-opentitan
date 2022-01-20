import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9654"
version_tuple = (0, 0, 9654)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9654")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9532"
data_version_tuple = (0, 0, 9532)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9532")
except ImportError:
    pass
data_git_hash = "bda359224882cd1740b752999b1e4e2ec4edb123"
data_git_describe = "v0.0-9532-gbda359224"
data_git_msg = """\
commit bda359224882cd1740b752999b1e4e2ec4edb123
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Tue Jan 18 08:25:23 2022 -0800

    [entropy_src/rtl] create a pulse for alert signal
    
    Verification works best when the main fsm alert signal is a pulse.
    Fixes #10134.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
