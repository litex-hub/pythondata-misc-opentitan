import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9390"
version_tuple = (0, 0, 9390)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9390")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9273"
data_version_tuple = (0, 0, 9273)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9273")
except ImportError:
    pass
data_git_hash = "fbb37b1a04097143cfa7b0c26477e5b9b4884327"
data_git_describe = "v0.0-9273-gfbb37b1a0"
data_git_msg = """\
commit fbb37b1a04097143cfa7b0c26477e5b9b4884327
Author: Weicai Yang <weicai@google.com>
Date:   Thu Jan 6 14:04:30 2022 -0800

    [sram/dv] Update DV doc
    
    Update the memory scb checkings
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
