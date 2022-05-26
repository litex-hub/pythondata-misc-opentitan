import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12354"
version_tuple = (0, 0, 12354)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12354")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12216"
data_version_tuple = (0, 0, 12216)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12216")
except ImportError:
    pass
data_git_hash = "e1961043f6308107ec570b5791b2c3606cf17b33"
data_git_describe = "v0.0-12216-ge1961043f"
data_git_msg = """\
commit e1961043f6308107ec570b5791b2c3606cf17b33
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Wed May 25 01:19:34 2022 +0000

    [adc_ctrl,dv] regression fix fsm_reset test
    
    - trigger aon reset and main reset at the same time during the test
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

"""

# Tool version info
tool_version_str = "0.0.post138"
tool_version_tuple = (0, 0, 138)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post138")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
