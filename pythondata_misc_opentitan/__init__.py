import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12736"
version_tuple = (0, 0, 12736)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12736")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12594"
data_version_tuple = (0, 0, 12594)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12594")
except ImportError:
    pass
data_git_hash = "bfb3da321b49a2f3d9271053e7d2e0d05f662503"
data_git_describe = "v0.0-12594-gbfb3da321"
data_git_msg = """\
commit bfb3da321b49a2f3d9271053e7d2e0d05f662503
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Jun 9 10:07:18 2022 -0700

    feat(ci): Skip FPGA/ OTBN tests for CDC
    
    This commit let CI skip FPGA, verilator, OTBN tests for CDC only
    changes.
    
    The cdconlychange log has been checked after
    https://github.com/lowRISC/opentitan/pull/13117 has been merged.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
