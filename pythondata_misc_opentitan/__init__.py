import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14981"
version_tuple = (0, 0, 14981)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14981")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14839"
data_version_tuple = (0, 0, 14839)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14839")
except ImportError:
    pass
data_git_hash = "cb9bee67989b2c0ef31d47936ac9501c9e2b798f"
data_git_describe = "v0.0-14839-gcb9bee6798"
data_git_msg = """\
commit cb9bee67989b2c0ef31d47936ac9501c9e2b798f
Author: Michael Schaffner <msf@google.com>
Date:   Tue Oct 25 17:19:50 2022 -0700

    [rv_dm] Add generated registers to docs
    
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
