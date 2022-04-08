import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11459"
version_tuple = (0, 0, 11459)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11459")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11333"
data_version_tuple = (0, 0, 11333)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11333")
except ImportError:
    pass
data_git_hash = "86286403a900eacb6af89686a3ccde85a4404637"
data_git_describe = "v0.0-11333-g86286403a"
data_git_msg = """\
commit 86286403a900eacb6af89686a3ccde85a4404637
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Tue Apr 5 10:20:19 2022 -0700

    [dv/otp] Increase FSM coverage
    
    This PR increases the FSM cov by:
    1). Add an enum to control random timing to issue reset or lc_esc.
    2). Add some flags to mark specific FSM states: such as digests cal,
      init, etc.
    3). Enhance some randomizations in existing tests.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
