import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9006"
version_tuple = (0, 0, 9006)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9006")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8894"
data_version_tuple = (0, 0, 8894)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8894")
except ImportError:
    pass
data_git_hash = "f6eebeee722ce608ad4500f8b13239c4c849235e"
data_git_describe = "v0.0-8894-gf6eebeee7"
data_git_msg = """\
commit f6eebeee722ce608ad4500f8b13239c4c849235e
Author: Weicai Yang <weicai@google.com>
Date:   Thu Dec 2 15:36:44 2021 -0800

    [sram/dv] Fix access_during_key_req
    
    1. updated seq and scb to avoid timing precise check
    2. moved mem_init to scb
    3. disabled intg check if we only request key update without init
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
