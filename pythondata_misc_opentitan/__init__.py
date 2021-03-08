import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5279"
version_tuple = (0, 0, 5279)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5279")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5184"
data_version_tuple = (0, 0, 5184)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5184")
except ImportError:
    pass
data_git_hash = "2a1589419e8fd8c80f21939b810698295f73d05c"
data_git_describe = "v0.0-5184-g2a1589419"
data_git_msg = """\
commit 2a1589419e8fd8c80f21939b810698295f73d05c
Author: Felix Miller <felix.miller@gi-de.com>
Date:   Sun Mar 7 18:05:39 2021 +0100

    [otbn] add P-384 curve point addition
    
    Adds routine for P-384 point addition in projective space plus
    simple standalone test.
    
    Signed-off-by: Felix Miller <felix.miller@gi-de.com>

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
