import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8459"
version_tuple = (0, 0, 8459)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8459")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8347"
data_version_tuple = (0, 0, 8347)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8347")
except ImportError:
    pass
data_git_hash = "a5bc6b3f3c45969247aa7dc5ba5ded0715994186"
data_git_describe = "v0.0-8347-ga5bc6b3f3"
data_git_msg = """\
commit a5bc6b3f3c45969247aa7dc5ba5ded0715994186
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Oct 25 17:33:24 2021 -0700

    [dv/alert_init] Handle reset during alert_init
    
    This PR handles the scenario where reset is issued during alert_init.
    We make the `wait_alert_init_done` to be a non-blocking task and use a
    fork join_any to handle this scenario.
    Thanks @weicaiyang for helping debugging this issue in uart seq.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
