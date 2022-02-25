import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10537"
version_tuple = (0, 0, 10537)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10537")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10411"
data_version_tuple = (0, 0, 10411)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10411")
except ImportError:
    pass
data_git_hash = "2ee2bec3c70e4cbbab00084313fe5c02972f3c0a"
data_git_describe = "v0.0-10411-g2ee2bec3c"
data_git_msg = """\
commit 2ee2bec3c70e4cbbab00084313fe5c02972f3c0a
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Feb 24 17:53:39 2022 -0800

    [dv/rstmgr] Fix incorrect SVA for cascading resets
    
    The previous assertion for a falling parent reset was just wrong,
    and was never attempted, causing low assertion coverage.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
