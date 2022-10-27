import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14999"
version_tuple = (0, 0, 14999)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14999")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14857"
data_version_tuple = (0, 0, 14857)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14857")
except ImportError:
    pass
data_git_hash = "c062fd809486043d12e10a80b97ef22aae3dee71"
data_git_describe = "v0.0-14857-gc062fd8094"
data_git_msg = """\
commit c062fd809486043d12e10a80b97ef22aae3dee71
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 26 17:42:36 2022 -0700

    [bazel] increase airgapped build test set
    
    This increases the targets that are built in an airgapped environment in
    CI to provide better coverage at catching future breakages.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
