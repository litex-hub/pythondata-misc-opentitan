import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12581"
version_tuple = (0, 0, 12581)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12581")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12439"
data_version_tuple = (0, 0, 12439)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12439")
except ImportError:
    pass
data_git_hash = "ad74c389f1e2a3f6c24292a6f3e99e43f7e9f7e5"
data_git_describe = "v0.0-12439-gad74c389f"
data_git_msg = """\
commit ad74c389f1e2a3f6c24292a6f3e99e43f7e9f7e5
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Jun 6 13:56:57 2022 -0700

    [aes/rtl] Enhance alert output in AES FSM
    
    Follow the change in PR #12898, we think it is better to immediately
    output error signal when the state goes to `default` unknown state.
    The reason is because if the attacker continues to drive the FSM to
    unknown states, the alert actually won't fire.
    
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
