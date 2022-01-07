import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9383"
version_tuple = (0, 0, 9383)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9383")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9266"
data_version_tuple = (0, 0, 9266)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9266")
except ImportError:
    pass
data_git_hash = "a41c0a57568f1dc8263a4ecc3913f190750959f5"
data_git_describe = "v0.0-9266-ga41c0a575"
data_git_msg = """\
commit a41c0a57568f1dc8263a4ecc3913f190750959f5
Author: Michael Schaffner <msf@opentitan.org>
Date:   Wed Jan 5 04:37:04 2022 -0800

    [prim_filter_cnt] Make threshold runtime programmable
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
