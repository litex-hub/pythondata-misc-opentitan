import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10925"
version_tuple = (0, 0, 10925)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10925")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10799"
data_version_tuple = (0, 0, 10799)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10799")
except ImportError:
    pass
data_git_hash = "121ea53a3955779cc46a66a149ce870e7f8b6c15"
data_git_describe = "v0.0-10799-g121ea53a3"
data_git_msg = """\
commit 121ea53a3955779cc46a66a149ce870e7f8b6c15
Author: Michael Tempelmeier <michael.tempelmeier@gi-de.com>
Date:   Wed Feb 16 17:00:51 2022 +0100

    [kmac] Added errorcode for fatal-fault #10804
    
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
