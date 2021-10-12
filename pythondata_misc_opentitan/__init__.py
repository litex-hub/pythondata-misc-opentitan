import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8225"
version_tuple = (0, 0, 8225)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8225")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8113"
data_version_tuple = (0, 0, 8113)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8113")
except ImportError:
    pass
data_git_hash = "4b3d232ee42c5f24511c89c5eefecc113e9a3ee3"
data_git_describe = "v0.0-8113-g4b3d232ee"
data_git_msg = """\
commit 4b3d232ee42c5f24511c89c5eefecc113e9a3ee3
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Tue Oct 12 07:47:11 2021 -0700

    [entropy_src/dv] push_pull_agent cfg.zero_delays
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
