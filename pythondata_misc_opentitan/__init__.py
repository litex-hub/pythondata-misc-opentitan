import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5335"
version_tuple = (0, 0, 5335)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5335")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5240"
data_version_tuple = (0, 0, 5240)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5240")
except ImportError:
    pass
data_git_hash = "bd440d25bc428f82bd2c65f57341587408623d94"
data_git_describe = "v0.0-5240-gbd440d25b"
data_git_msg = """\
commit bd440d25bc428f82bd2c65f57341587408623d94
Author: Michael Schaffner <msf@opentitan.org>
Date:   Fri Mar 5 17:51:01 2021 -0800

    [jtag_mux] Delete JTAG mux module
    
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
