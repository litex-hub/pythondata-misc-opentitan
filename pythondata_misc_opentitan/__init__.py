import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14784"
version_tuple = (0, 0, 14784)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14784")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14642"
data_version_tuple = (0, 0, 14642)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14642")
except ImportError:
    pass
data_git_hash = "8f985b9f2af6271bb5bf2e5f567bc57662989f7d"
data_git_describe = "v0.0-14642-g8f985b9f2a"
data_git_msg = """\
commit 8f985b9f2af6271bb5bf2e5f567bc57662989f7d
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Oct 14 14:25:18 2022 -0700

    [dv/adc_ctrl] Fix adc_ctrl regression error
    
    This PR fixes adc_ctrl regression error due to reset_aon_ni and reset_ni
    not issuing at the same time.
    Because the reset_aon_ni has very small frequency compares to reset_ni
    clock, so issuing reset with normal `apply_reset` task would cause the
    following issue:
    The reset_ni will finsh toggle but reset_aon_ni has not start activation
    yet.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
