import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15137"
version_tuple = (0, 0, 15137)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15137")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14995"
data_version_tuple = (0, 0, 14995)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14995")
except ImportError:
    pass
data_git_hash = "db5905ee18fd9573a705d6802424433f660bc0cb"
data_git_describe = "v0.0-14995-gdb5905ee18"
data_git_msg = """\
commit db5905ee18fd9573a705d6802424433f660bc0cb
Author: Michael Schaffner <msf@google.com>
Date:   Tue Nov 1 19:23:06 2022 -0700

    [doc] Minor tweaks to test triage issue template
    
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
