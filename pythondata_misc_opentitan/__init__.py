import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8801"
version_tuple = (0, 0, 8801)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8801")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8689"
data_version_tuple = (0, 0, 8689)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8689")
except ImportError:
    pass
data_git_hash = "485d3e87fbd9389ab9e5e68ec9fe63e84090f6f6"
data_git_describe = "v0.0-8689-g485d3e87f"
data_git_msg = """\
commit 485d3e87fbd9389ab9e5e68ec9fe63e84090f6f6
Author: alex sapozhnikov <alex.sapozhnikov@wdc.com>
Date:   Thu Nov 11 12:15:59 2021 -0800

    [pattgen/dv]updated pattgen with action items from v1 review
    
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
