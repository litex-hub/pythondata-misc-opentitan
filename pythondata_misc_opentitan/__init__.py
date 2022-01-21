import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9703"
version_tuple = (0, 0, 9703)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9703")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9581"
data_version_tuple = (0, 0, 9581)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9581")
except ImportError:
    pass
data_git_hash = "2e85ff19f1cf83b5c881e1537e0fc280fccfbb32"
data_git_describe = "v0.0-9581-g2e85ff19f"
data_git_msg = """\
commit 2e85ff19f1cf83b5c881e1537e0fc280fccfbb32
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Jan 19 14:15:02 2022 -0800

    [dif/alert_handler] Add local alert locking DIFs.
    
    This commit adds two DIFs to lock the configuration CSRs of a specific
    local alert, and check if a specific local alert's CSRs are locked. This
    gives users fine grained control over the locking of a specific local
    alert's configuration.
    
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
