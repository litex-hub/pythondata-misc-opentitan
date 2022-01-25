import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9762"
version_tuple = (0, 0, 9762)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9762")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9640"
data_version_tuple = (0, 0, 9640)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9640")
except ImportError:
    pass
data_git_hash = "92fa6f8648ac1e60ec98e18657d9925b47fac3b9"
data_git_describe = "v0.0-9640-g92fa6f864"
data_git_msg = """\
commit 92fa6f8648ac1e60ec98e18657d9925b47fac3b9
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Jan 21 14:58:12 2022 -0800

    [dv/otp_ctrl] Update auto-generated UNR file
    
    This PR updates the tool generated UNR file. The main impact is that
    design added a `VendorTest` partition.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
