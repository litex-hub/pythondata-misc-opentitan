import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14955"
version_tuple = (0, 0, 14955)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14955")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14813"
data_version_tuple = (0, 0, 14813)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14813")
except ImportError:
    pass
data_git_hash = "d83c59f074cc4081ef362d525cf21bb4f2ac3b5b"
data_git_describe = "v0.0-14813-gd83c59f074"
data_git_msg = """\
commit d83c59f074cc4081ef362d525cf21bb4f2ac3b5b
Author: Michael Schaffner <msf@google.com>
Date:   Tue Oct 25 16:51:23 2022 -0700

    [mubi/lc] Add comment regarding mubi encoding changes
    
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
