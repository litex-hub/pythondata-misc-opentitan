import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11039"
version_tuple = (0, 0, 11039)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11039")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10913"
data_version_tuple = (0, 0, 10913)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10913")
except ImportError:
    pass
data_git_hash = "9634d8b81076f5746485bdf874d175ee824617dc"
data_git_describe = "v0.0-10913-g9634d8b81"
data_git_msg = """\
commit 9634d8b81076f5746485bdf874d175ee824617dc
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Mar 22 13:55:50 2022 -0700

    [lc_ctrl/dv] Update DIF to account for hardware revision CSR
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
