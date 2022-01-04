import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9310"
version_tuple = (0, 0, 9310)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9310")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9193"
data_version_tuple = (0, 0, 9193)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9193")
except ImportError:
    pass
data_git_hash = "331f25cb0c780dbf382bd601b8a5b7ac90c21f98"
data_git_describe = "v0.0-9193-g331f25cb0"
data_git_msg = """\
commit 331f25cb0c780dbf382bd601b8a5b7ac90c21f98
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Dec 24 07:17:59 2021 -0800

    [sysrst_ctrl] Update Hjson
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
