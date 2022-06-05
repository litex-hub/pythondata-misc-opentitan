import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12502"
version_tuple = (0, 0, 12502)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12502")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12360"
data_version_tuple = (0, 0, 12360)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12360")
except ImportError:
    pass
data_git_hash = "0124ced9192e6aa2e7f5049164626fb56555ad18"
data_git_describe = "v0.0-12360-g0124ced91"
data_git_msg = """\
commit 0124ced9192e6aa2e7f5049164626fb56555ad18
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Jun 2 20:52:18 2022 -0700

    [sw,rstmgr] Fix doc and checks for dump code
    
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
