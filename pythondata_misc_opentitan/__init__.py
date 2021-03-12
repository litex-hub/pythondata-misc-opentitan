import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5363"
version_tuple = (0, 0, 5363)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5363")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5268"
data_version_tuple = (0, 0, 5268)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5268")
except ImportError:
    pass
data_git_hash = "73b67d7b026f2cb2cb5e2392f7f2c15f70fca3a6"
data_git_describe = "v0.0-5268-g73b67d7b0"
data_git_msg = """\
commit 73b67d7b026f2cb2cb5e2392f7f2c15f70fca3a6
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Thu Mar 4 02:18:24 2021 -0800

    [aes/cov] added refine file to aes
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
