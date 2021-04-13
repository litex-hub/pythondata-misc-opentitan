import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5840"
version_tuple = (0, 0, 5840)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5840")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5745"
data_version_tuple = (0, 0, 5745)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5745")
except ImportError:
    pass
data_git_hash = "d0936b2abea12fac6951252dbc86a167c1cc0ec5"
data_git_describe = "v0.0-5745-gd0936b2ab"
data_git_msg = """\
commit d0936b2abea12fac6951252dbc86a167c1cc0ec5
Author: Michael Schaffner <msf@opentitan.org>
Date:   Mon Apr 12 16:01:45 2021 -0700

    [otp_ctrl] Align lock bits in otp_ctrl Hjson to use rw0c
    
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
