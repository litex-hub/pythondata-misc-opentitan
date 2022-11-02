import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15110"
version_tuple = (0, 0, 15110)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15110")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14968"
data_version_tuple = (0, 0, 14968)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14968")
except ImportError:
    pass
data_git_hash = "b9bffe464791584200251aea1039e9e4fa028d94"
data_git_describe = "v0.0-14968-gb9bffe4647"
data_git_msg = """\
commit b9bffe464791584200251aea1039e9e4fa028d94
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Nov 1 18:31:30 2022 -0700

    [chip dv] Minor enhance,ent to adc_ctrl debug cable test
    
    Check interrupt_expected to be true in the ISR.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
