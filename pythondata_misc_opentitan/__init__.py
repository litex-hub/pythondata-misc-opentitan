import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8431"
version_tuple = (0, 0, 8431)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8431")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8319"
data_version_tuple = (0, 0, 8319)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8319")
except ImportError:
    pass
data_git_hash = "59b043ec86407b8d6d9499cb1a2d1695f6601d59"
data_git_describe = "v0.0-8319-g59b043ec8"
data_git_msg = """\
commit 59b043ec86407b8d6d9499cb1a2d1695f6601d59
Author: alex sapozhnikov <alex.sapozhnikov@wdc.com>
Date:   Wed Oct 6 21:21:42 2021 -0700

    [pattgen/dv] Improve stimulus to achieve near full functional coverage
    
    Signed-off-by: alex sapozhnikov <alex.sapozhnikov@wdc.com>

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
