import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10747"
version_tuple = (0, 0, 10747)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10747")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10621"
data_version_tuple = (0, 0, 10621)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10621")
except ImportError:
    pass
data_git_hash = "54b949255a8c463ea365126d90c39cd26c462638"
data_git_describe = "v0.0-10621-g54b949255"
data_git_msg = """\
commit 54b949255a8c463ea365126d90c39cd26c462638
Author: Michael Tempelmeier <michael.tempelmeier@gi-de.com>
Date:   Mon Feb 28 16:36:53 2022 +0100

    [kmac] changed hash-threshold reg to shadow reg
    
    Signed-off-by: Michael Tempelmeier <michael.tempelmeier@gi-de.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
