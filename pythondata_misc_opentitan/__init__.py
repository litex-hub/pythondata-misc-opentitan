import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14852"
version_tuple = (0, 0, 14852)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14852")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14710"
data_version_tuple = (0, 0, 14710)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14710")
except ImportError:
    pass
data_git_hash = "2a9bfc422332ab89c91d30928e82537ddeb7c218"
data_git_describe = "v0.0-14710-g2a9bfc4223"
data_git_msg = """\
commit 2a9bfc422332ab89c91d30928e82537ddeb7c218
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Oct 18 15:53:04 2022 -0700

    [dv/chip] improve assigning the initial value in sysctrl_rst test
    
    PR #15546 fixes a regression issue by assigning an initial value to
    sysrst_ctrl input. However, a better way (I think) to do it is to use
    the pulldown method.
    
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
