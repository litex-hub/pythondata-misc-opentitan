import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14162"
version_tuple = (0, 0, 14162)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14162")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14020"
data_version_tuple = (0, 0, 14020)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14020")
except ImportError:
    pass
data_git_hash = "db5c8367b0474e7cad215db8dc0ad6ad1271cacb"
data_git_describe = "v0.0-14020-gdb5c8367b0"
data_git_msg = """\
commit db5c8367b0474e7cad215db8dc0ad6ad1271cacb
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Tue Aug 30 15:57:40 2022 -0700

    [test] alert_handler_reverse_ping_in_deep_sleep
    
    Check that escalation receivers located inside always-on blocks do not
    auto-escalate due to the reverse ping feature while the system is in deep
    sleep.
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
