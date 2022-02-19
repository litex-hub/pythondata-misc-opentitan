import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10449"
version_tuple = (0, 0, 10449)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10449")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10323"
data_version_tuple = (0, 0, 10323)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10323")
except ImportError:
    pass
data_git_hash = "a5566a4de46aa0e951bd6e1e1658b13354f7b6bd"
data_git_describe = "v0.0-10323-ga5566a4de"
data_git_msg = """\
commit a5566a4de46aa0e951bd6e1e1658b13354f7b6bd
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Feb 16 14:54:08 2022 -0800

    [reggen] Minor cm check fix
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
