import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5495"
version_tuple = (0, 0, 5495)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5495")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5400"
data_version_tuple = (0, 0, 5400)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5400")
except ImportError:
    pass
data_git_hash = "fc82225ab99a6e50ce2e9131d564e9a11ea82075"
data_git_describe = "v0.0-5400-gfc82225ab"
data_git_msg = """\
commit fc82225ab99a6e50ce2e9131d564e9a11ea82075
Author: Chris Frantz <cfrantz@google.com>
Date:   Thu Mar 18 16:17:12 2021 -0700

    Eliminate `#pragma once` in favor of include guards
    
    The Google C/C++ Style Guide (referenced from the OpenTitan C/C++ guide)
    requires #define guards in header files.
    
    https://google.github.io/styleguide/cppguide.html#The__define_Guard
    Signed-off-by: Chris Frantz <cfrantz@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
