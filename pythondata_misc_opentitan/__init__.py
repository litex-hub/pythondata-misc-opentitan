import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5269"
version_tuple = (0, 0, 5269)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5269")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5174"
data_version_tuple = (0, 0, 5174)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5174")
except ImportError:
    pass
data_git_hash = "fb17e44f0b035fdc0728416bea50c67ed2f40d29"
data_git_describe = "v0.0-5174-gfb17e44f0"
data_git_msg = """\
commit fb17e44f0b035fdc0728416bea50c67ed2f40d29
Author: Cindy Chen <chencindy@google.com>
Date:   Fri Mar 5 12:41:21 2021 -0800

    [dv/alert_handler] remove logic to auto-generate alert parameters
    
    In previous logic, DV will auto-generate parameters from hjson file,
    which includes NUM_ALERTS and ASYNC_ON.
    However, in design, these parameters are auto-generated from hjson as
    well. There is no need to generate again in DV, and it is easier to just
    reuse the parameter from design.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
