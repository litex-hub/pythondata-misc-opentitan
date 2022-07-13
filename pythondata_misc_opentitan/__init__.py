import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13053"
version_tuple = (0, 0, 13053)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13053")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12911"
data_version_tuple = (0, 0, 12911)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12911")
except ImportError:
    pass
data_git_hash = "cede80721f4d9e1a24d47feae60f4f36772c0e75"
data_git_describe = "v0.0-12911-gcede80721f"
data_git_msg = """\
commit cede80721f4d9e1a24d47feae60f4f36772c0e75
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Jul 12 12:21:25 2022 -0700

    [dv/alert_handler] Add FSM transition exclusions
    
    This PR finishes a TODO in issue #13589 that excludes from valid (not
    Idle state) to FSMErrorSt. Current common sequence only probe the FSM
    error from Idle state. The other checkings are done in FPV bench.
    
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
