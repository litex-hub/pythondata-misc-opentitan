import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9799"
version_tuple = (0, 0, 9799)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9799")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9677"
data_version_tuple = (0, 0, 9677)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9677")
except ImportError:
    pass
data_git_hash = "56bb04f9a8a806b36f6f67a9c09fa316fada11b7"
data_git_describe = "v0.0-9677-g56bb04f9a"
data_git_msg = """\
commit 56bb04f9a8a806b36f6f67a9c09fa316fada11b7
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Dec 10 13:28:54 2021 -0800

    [doc] Update TC list
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
