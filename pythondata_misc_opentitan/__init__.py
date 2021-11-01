import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8542"
version_tuple = (0, 0, 8542)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8542")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8430"
data_version_tuple = (0, 0, 8430)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8430")
except ImportError:
    pass
data_git_hash = "10eb39442fdaa80e5ff5c46edfb4d9aa7ea9474d"
data_git_describe = "v0.0-8430-g10eb39442"
data_git_msg = """\
commit 10eb39442fdaa80e5ff5c46edfb4d9aa7ea9474d
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue Oct 26 14:28:49 2021 +0100

    [dif] Implement the AES OFB and CFB modes on the DIF API
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
