import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15063"
version_tuple = (0, 0, 15063)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15063")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14921"
data_version_tuple = (0, 0, 14921)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14921")
except ImportError:
    pass
data_git_hash = "476db4900615051334747592a12553d2b56b14f4"
data_git_describe = "v0.0-14921-g476db49006"
data_git_msg = """\
commit 476db4900615051334747592a12553d2b56b14f4
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Oct 31 08:30:50 2022 -0700

    [dvsim] fix bindgen error in nightlies
    
    This also rolls-forward #15831.
    
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
