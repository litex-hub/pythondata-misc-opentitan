import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12662"
version_tuple = (0, 0, 12662)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12662")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12520"
data_version_tuple = (0, 0, 12520)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12520")
except ImportError:
    pass
data_git_hash = "022b181f4b5b4e0d771b5c6baef29df76d3f7063"
data_git_describe = "v0.0-12520-g022b181f4"
data_git_msg = """\
commit 022b181f4b5b4e0d771b5c6baef29df76d3f7063
Author: Alphan Ulusoy <alphan@google.com>
Date:   Mon Jun 13 10:49:20 2022 -0400

    [util] Edit chip_info format to look better with LOG_INFO()
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
