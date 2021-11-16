import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8735"
version_tuple = (0, 0, 8735)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8735")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8623"
data_version_tuple = (0, 0, 8623)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8623")
except ImportError:
    pass
data_git_hash = "7e5b0deb1c24089adeed5396eca473f60449d45c"
data_git_describe = "v0.0-8623-g7e5b0deb1"
data_git_msg = """\
commit 7e5b0deb1c24089adeed5396eca473f60449d45c
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Nov 16 10:19:32 2021 -0800

    [doc] Minor dev stages cleanup
    
    Signed-off-by: Michael Schaffner <msf@opentitan.org>

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
