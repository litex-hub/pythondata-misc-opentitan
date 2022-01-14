import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9541"
version_tuple = (0, 0, 9541)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9541")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9419"
data_version_tuple = (0, 0, 9419)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9419")
except ImportError:
    pass
data_git_hash = "756ea0bdfd5c19b6b25cc7e83eaef32452991ba1"
data_git_describe = "v0.0-9419-g756ea0bdf"
data_git_msg = """\
commit 756ea0bdfd5c19b6b25cc7e83eaef32452991ba1
Author: Weicai Yang <weicai@google.com>
Date:   Mon Jan 10 14:31:47 2022 -0800

    [dv] Update checklist
    
    As discussed in SRAM Ctrl V2 review, updated these checklist
    1. Updated the description for “pre_verified_sub_modules_v2”
    2. Updated V2S checklist to add an item for FPV
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
