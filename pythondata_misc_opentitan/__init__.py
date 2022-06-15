import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12706"
version_tuple = (0, 0, 12706)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12706")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12564"
data_version_tuple = (0, 0, 12564)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12564")
except ImportError:
    pass
data_git_hash = "92e78884cb23a37119e066ee99344a7235e8ca18"
data_git_describe = "v0.0-12564-g92e78884c"
data_git_msg = """\
commit 92e78884cb23a37119e066ee99344a7235e8ca18
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Wed Jun 15 11:33:58 2022 -0700

    [entropy_src/dv] Fix vcs coverage errors
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
