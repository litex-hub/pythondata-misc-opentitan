import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10105"
version_tuple = (0, 0, 10105)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10105")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9981"
data_version_tuple = (0, 0, 9981)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9981")
except ImportError:
    pass
data_git_hash = "e87d92e0e4dd66291272e70357dabbe2dfd87ca8"
data_git_describe = "v0.0-9981-ge87d92e0e"
data_git_msg = """\
commit e87d92e0e4dd66291272e70357dabbe2dfd87ca8
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Wed Feb 2 14:01:24 2022 -0800

    [edn/rtl] Add filter to cmd_req_done status
    
    When the hardware interfaces run (boot or auto request modes) the
    cmd_req_done status bit should not be set.
    Only in response to a software command should this status bit be set.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
