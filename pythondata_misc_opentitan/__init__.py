import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9804"
version_tuple = (0, 0, 9804)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9804")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9682"
data_version_tuple = (0, 0, 9682)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9682")
except ImportError:
    pass
data_git_hash = "68e86515989c047e28915f6d5d534c578c9bdb3d"
data_git_describe = "v0.0-9682-g68e865159"
data_git_msg = """\
commit 68e86515989c047e28915f6d5d534c578c9bdb3d
Author: Cindy Chen <chencindy@google.com>
Date:   Tue Jan 25 10:17:54 2022 -0800

    [dv/otp_ctrl] Fix prim_tl_agent close source monitor error
    
    Due to the current reggen tool, we have an empty prim_tl_o/i interface
    without any CSRs for test_access. To ensure the connection for
    read/write works, open source OTP tb creates a temp tl_agent. However,
    because it hooks up same interface with close source, the monitor will
    report some runtime error.
    To avoid this, we introduced a cfg flag that can disable creating this temp
    tl_agent.
    
    Signed-off-by: Cindy Chen <chencindy@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
