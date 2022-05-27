import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12394"
version_tuple = (0, 0, 12394)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12394")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12254"
data_version_tuple = (0, 0, 12254)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12254")
except ImportError:
    pass
data_git_hash = "26b2cabc4da62c4b675149910d8db160a4ecad82"
data_git_describe = "v0.0-12254-g26b2cabc4"
data_git_msg = """\
commit 26b2cabc4da62c4b675149910d8db160a4ecad82
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri May 27 10:44:45 2022 -0700

    [docs] remove newline in closed-source test hooks docs
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post140"
tool_version_tuple = (0, 0, 140)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post140")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
