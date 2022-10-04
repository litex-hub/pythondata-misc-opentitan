import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14539"
version_tuple = (0, 0, 14539)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14539")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14397"
data_version_tuple = (0, 0, 14397)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14397")
except ImportError:
    pass
data_git_hash = "fa5abdb5cb9f7157a6c1a0f3318257e52a742aae"
data_git_describe = "v0.0-14397-gfa5abdb5cb"
data_git_msg = """\
commit fa5abdb5cb9f7157a6c1a0f3318257e52a742aae
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Sun Oct 2 23:43:14 2022 +0000

    [flash_ctrl,dv] fix regression fail
    
    Adjust error conditions of following error tests
    - flash_ctrl_sec_cm
    - flash_ctrl_derr_detect
    - flash_ctrl_phy_arb_redun
    - flash_ctrl_phy_host_grant_err
    - flash_ctrl_phy_ack_consistency
    
    Disable irrelevant assert from flash_ctrl_hw_rma_rest
    Set ecc/scramble randomize for error tests
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

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
