import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9678"
version_tuple = (0, 0, 9678)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9678")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9556"
data_version_tuple = (0, 0, 9556)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9556")
except ImportError:
    pass
data_git_hash = "2d323d68624f8c426b111908411d6b38a506322c"
data_git_describe = "v0.0-9556-g2d323d686"
data_git_msg = """\
commit 2d323d68624f8c426b111908411d6b38a506322c
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Thu Jan 20 14:03:34 2022 -0800

    [dv/otp_ctrl] Test access sequence
    
    This PR connects test access `prim_tl_i/o` to tl_agent.
    The tool should automatically create this tl_agent, but currently the
    auto-generated RAL block does not contain any registers, thus we will
    run into a runtime error.
    Until the reggen tool is optimized, the current solution is to only
    manually create a tl_agent for this test_access area without an adapter
    or RAL.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
