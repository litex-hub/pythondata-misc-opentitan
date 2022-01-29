import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9888"
version_tuple = (0, 0, 9888)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9888")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9764"
data_version_tuple = (0, 0, 9764)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9764")
except ImportError:
    pass
data_git_hash = "b8a1093b1de25ff7f84c6b9dc58bbc384815aeaa"
data_git_describe = "v0.0-9764-gb8a1093b1"
data_git_msg = """\
commit b8a1093b1de25ff7f84c6b9dc58bbc384815aeaa
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Jan 27 20:47:28 2022 -0800

    [keymgr] Convert configuration to shadow register
    
    - split start from configuration since shadow registers do now support hrw
    - this is part of keymgr d2s likely review items
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
