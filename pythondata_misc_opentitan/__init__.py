import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12796"
version_tuple = (0, 0, 12796)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12796")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12654"
data_version_tuple = (0, 0, 12654)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12654")
except ImportError:
    pass
data_git_hash = "776116b731f21d922195187233be5c02db7b238c"
data_git_describe = "v0.0-12654-g776116b731"
data_git_msg = """\
commit 776116b731f21d922195187233be5c02db7b238c
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jun 22 20:55:46 2022 -0700

    [top/autogen] Add missing autogen file
    
    - an autogen update was missed, possibly due to PR's crossing.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
