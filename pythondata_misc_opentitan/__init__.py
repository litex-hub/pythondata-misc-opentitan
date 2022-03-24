import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11060"
version_tuple = (0, 0, 11060)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11060")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10934"
data_version_tuple = (0, 0, 10934)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10934")
except ImportError:
    pass
data_git_hash = "5fac8e3ce4f6cc4d4452c2bfb768b1d573a8dc32"
data_git_describe = "v0.0-10934-g5fac8e3ce"
data_git_msg = """\
commit 5fac8e3ce4f6cc4d4452c2bfb768b1d573a8dc32
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Wed Mar 23 11:03:17 2022 -0700

    [spi_device] Waiving CDC violations through prim_flop_2sync
    
    Adding W_CNTL waivers that are passing through prim_flop_2sync.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
