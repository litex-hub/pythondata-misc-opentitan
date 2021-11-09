import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8635"
version_tuple = (0, 0, 8635)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8635")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8523"
data_version_tuple = (0, 0, 8523)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8523")
except ImportError:
    pass
data_git_hash = "882cce06a528974ce72e6c893f726be2febed0aa"
data_git_describe = "v0.0-8523-g882cce06a"
data_git_msg = """\
commit 882cce06a528974ce72e6c893f726be2febed0aa
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Nov 5 06:59:29 2021 +0000

    [sw/testing] Fix comment typos in `check.h`.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
