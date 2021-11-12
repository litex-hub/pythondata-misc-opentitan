import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8707"
version_tuple = (0, 0, 8707)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8707")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8595"
data_version_tuple = (0, 0, 8595)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8595")
except ImportError:
    pass
data_git_hash = "7f2bdc9f34f693e906379a073cf1fe5f5d349729"
data_git_describe = "v0.0-8595-g7f2bdc9f3"
data_git_msg = """\
commit 7f2bdc9f34f693e906379a073cf1fe5f5d349729
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Sat Nov 6 08:22:24 2021 -0700

    [entropy_src/rtl] health test counters hardening
    
    There are a number of critical health test counters that are to be replaced with a hardened version.
    Errors detected by the prim_count block will forward to fatal_err without gating.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
