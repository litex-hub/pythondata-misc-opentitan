import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14743"
version_tuple = (0, 0, 14743)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14743")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14601"
data_version_tuple = (0, 0, 14601)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14601")
except ImportError:
    pass
data_git_hash = "9775df8858ffbb10fd804eb1ba67e2b498fcd814"
data_git_describe = "v0.0-14601-g9775df8858"
data_git_msg = """\
commit 9775df8858ffbb10fd804eb1ba67e2b498fcd814
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 13 22:54:57 2022 -0700

    [spi_device/dv] Fix wrong path
    
    Fixed for this PR #15496
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
