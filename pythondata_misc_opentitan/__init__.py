import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10601"
version_tuple = (0, 0, 10601)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10601")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10475"
data_version_tuple = (0, 0, 10475)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10475")
except ImportError:
    pass
data_git_hash = "536092a26c5f5dc7f24a87c48d4849c5a2eb972d"
data_git_describe = "v0.0-10475-g536092a26"
data_git_msg = """\
commit 536092a26c5f5dc7f24a87c48d4849c5a2eb972d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Feb 28 12:06:11 2022 -0800

    [fpv/csr] Support rw0c
    
    This PR supports adding assertions for RW0C regs followed the
    implementation of PR #11122
    
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
