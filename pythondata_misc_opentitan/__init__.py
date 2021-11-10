import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8658"
version_tuple = (0, 0, 8658)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8658")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8546"
data_version_tuple = (0, 0, 8546)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8546")
except ImportError:
    pass
data_git_hash = "f4d5e9a468455e620eef481a3147c9a98216ba91"
data_git_describe = "v0.0-8546-gf4d5e9a46"
data_git_msg = """\
commit f4d5e9a468455e620eef481a3147c9a98216ba91
Author: Timothy Chen <timothytim@google.com>
Date:   Tue Nov 9 13:41:04 2021 -0800

    [top, all] update connects for mubi
    
    - scanmode and flash_bist_enable from ast have been converted to mubi types
    - this commit just does the matching changes on the open source side
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
