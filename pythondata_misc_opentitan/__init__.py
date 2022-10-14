import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14752"
version_tuple = (0, 0, 14752)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14752")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14610"
data_version_tuple = (0, 0, 14610)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14610")
except ImportError:
    pass
data_git_hash = "96e2c3580cb64d1526609031c2163ed3f7207c7e"
data_git_describe = "v0.0-14610-g96e2c3580c"
data_git_msg = """\
commit 96e2c3580cb64d1526609031c2163ed3f7207c7e
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Oct 14 08:24:41 2022 -0700

    [entropy_src/rtl] Remove unused state from ack_sm
    
    In the `entropy_src_ack_sm`, the ACK_IMMED state allows the
    `entropy_src` to immediately output any seeds which may be available
    when the module is first enabled.  Since the `entropy_src` flushes its
    internal state when it is enabled, this condition is not expected, and
    so this state is never expected, and appears as an FSM coverage gap.
    (Note: interestingly enough, UNR analysis seems to claim that this state
    is somehow still reachable, even though this condition is not expected.)
    
    Given that this state is at best an unused optimization, it's here
    removed to help close FSM coverage.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
