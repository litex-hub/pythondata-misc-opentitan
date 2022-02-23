import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10481"
version_tuple = (0, 0, 10481)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10481")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10355"
data_version_tuple = (0, 0, 10355)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10355")
except ImportError:
    pass
data_git_hash = "7ad8245637fc54499cd55daba356cda304ee8af5"
data_git_describe = "v0.0-10355-g7ad824563"
data_git_msg = """\
commit 7ad8245637fc54499cd55daba356cda304ee8af5
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Feb 21 18:24:41 2022 -0800

    [dv/kmac] KMAC reaches V2
    
    This PR finishes the checklist for KMAC V2 status.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
