import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9728"
version_tuple = (0, 0, 9728)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9728")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9606"
data_version_tuple = (0, 0, 9606)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9606")
except ImportError:
    pass
data_git_hash = "c1376765178184f1a3e1b1d5a3941c31fcd9f080"
data_git_describe = "v0.0-9606-gc13767651"
data_git_msg = """\
commit c1376765178184f1a3e1b1d5a3941c31fcd9f080
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Jan 19 15:51:08 2022 -0800

    [dif/alert_handler] Add class locking DIFs.
    
    This commit adds two DIFs to lock the configuration CSRs of a specific
    alert class, and check if a specific alert class' CSRs are locked. This
    gives users fine grained control over the locking of a specific alert
    class' configuration.
    
    This addresses a task in #9899.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
