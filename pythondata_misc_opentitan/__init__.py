import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5299"
version_tuple = (0, 0, 5299)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5299")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5204"
data_version_tuple = (0, 0, 5204)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5204")
except ImportError:
    pass
data_git_hash = "e09bafcfdc3bd8af53efc8c235c25919344231bd"
data_git_describe = "v0.0-5204-ge09bafcfd"
data_git_msg = """\
commit e09bafcfdc3bd8af53efc8c235c25919344231bd
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Mon Mar 8 21:56:25 2021 -0800

    [sram_ctrl dv doc] Update DV doc
    
    Update terminology (testplan -> DV plan, DV plan -> DV document).
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
