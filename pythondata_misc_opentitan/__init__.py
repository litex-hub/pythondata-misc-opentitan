import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14608"
version_tuple = (0, 0, 14608)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14608")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14466"
data_version_tuple = (0, 0, 14466)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14466")
except ImportError:
    pass
data_git_hash = "10daa25ec9d8bebe6d86b6b20694cad1c2a40448"
data_git_describe = "v0.0-14466-g10daa25ec9"
data_git_msg = """\
commit 10daa25ec9d8bebe6d86b6b20694cad1c2a40448
Author: Michael Schaffner <msf@google.com>
Date:   Wed Oct 5 16:59:35 2022 -0700

    [prim_mubi] Fix sampling issue in MUBI sync assertions
    
    Fix #15234
    
    Signed-off-by: Michael Schaffner <msf@google.com>

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
