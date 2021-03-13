import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5373"
version_tuple = (0, 0, 5373)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5373")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5278"
data_version_tuple = (0, 0, 5278)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5278")
except ImportError:
    pass
data_git_hash = "9bb75e906b09e887cacb0450d17d103e19e17afc"
data_git_describe = "v0.0-5278-g9bb75e906"
data_git_msg = """\
commit 9bb75e906b09e887cacb0450d17d103e19e17afc
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Mar 12 15:13:31 2021 -0800

    [ibex] Hook up ram_cfg to Ibex
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
