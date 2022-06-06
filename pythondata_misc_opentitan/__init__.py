import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12518"
version_tuple = (0, 0, 12518)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12518")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12376"
data_version_tuple = (0, 0, 12376)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12376")
except ImportError:
    pass
data_git_hash = "6d211c008ce67c0ec0849d6c8724dc0146cf490b"
data_git_describe = "v0.0-12376-g6d211c008"
data_git_msg = """\
commit 6d211c008ce67c0ec0849d6c8724dc0146cf490b
Author: Weicai Yang <weicai@google.com>
Date:   Fri Jun 3 17:02:02 2022 -0700

    [dv] Add common test for reg write enable check
    
    Address #12113
    - Inject a fault in the prim_onehot_check to trigger reg integrity error
    - Check status reg and fatal alert
    
    Only add it for sram_ctrl. Will create a separate PR to enable this for
    all other blocks
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
