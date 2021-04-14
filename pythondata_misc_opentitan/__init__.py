import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5859"
version_tuple = (0, 0, 5859)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5859")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5764"
data_version_tuple = (0, 0, 5764)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5764")
except ImportError:
    pass
data_git_hash = "9312b9e529636114dc33dbd2937b489fe338af98"
data_git_describe = "v0.0-5764-g9312b9e52"
data_git_msg = """\
commit 9312b9e529636114dc33dbd2937b489fe338af98
Author: Michael Schaffner <msf@opentitan.org>
Date:   Tue Apr 13 17:51:01 2021 -0700

    [lint/docs] Update ascentlint dvsim command in readme
    
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
