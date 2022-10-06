import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14604"
version_tuple = (0, 0, 14604)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14604")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14462"
data_version_tuple = (0, 0, 14462)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14462")
except ImportError:
    pass
data_git_hash = "691ebe22351e94e566518f020330114451cdc6c6"
data_git_describe = "v0.0-14462-g691ebe2235"
data_git_msg = """\
commit 691ebe22351e94e566518f020330114451cdc6c6
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Oct 5 14:27:43 2022 -0700

    [dv,top] Share common code in pwrmgr_*sleep_all_wake_ups
    
    This facilitates the creation of a random version of these tests,
    and removes redundant code.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
