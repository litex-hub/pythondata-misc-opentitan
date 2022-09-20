import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14333"
version_tuple = (0, 0, 14333)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14333")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14191"
data_version_tuple = (0, 0, 14191)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14191")
except ImportError:
    pass
data_git_hash = "3575ab2b6f1fff58cdc5a3111632fe30ec59bfb8"
data_git_describe = "v0.0-14191-g3575ab2b6f"
data_git_msg = """\
commit 3575ab2b6f1fff58cdc5a3111632fe30ec59bfb8
Author: Timothy Trippel <ttrippel@google.com>
Date:   Tue Sep 20 05:39:45 2022 -0700

    [dif] update checklists to align with #14632
    
    This updates the checklists of the following IPs:
    - sysrst_ctrl
    - uart
    - usbdev
    
    This fixes #14632.
    
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
