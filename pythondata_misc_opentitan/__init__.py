import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12815"
version_tuple = (0, 0, 12815)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12815")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12673"
data_version_tuple = (0, 0, 12673)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12673")
except ImportError:
    pass
data_git_hash = "5d99252e897ffd5d1a4d7f18c43dd574653c4d6e"
data_git_describe = "v0.0-12673-g5d99252e89"
data_git_msg = """\
commit 5d99252e897ffd5d1a4d7f18c43dd574653c4d6e
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jun 23 08:14:05 2022 -0700

    [dv,chip,sva] Fix SVA checking pwrmgr to rstmgs reset requests
    
    The escalation request assertion needs to use the slow clock, since using
    other clocks makes it prone to timing out.
    Remove calls to disable these assertions, since they don't fail with this
    change.
    Make many formatting changes for verible.
    
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
