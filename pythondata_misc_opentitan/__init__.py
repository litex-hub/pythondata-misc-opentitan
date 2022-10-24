import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14914"
version_tuple = (0, 0, 14914)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14914")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14772"
data_version_tuple = (0, 0, 14772)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14772")
except ImportError:
    pass
data_git_hash = "dd77381064eee512cd82d5747e2d59e7c768c6c0"
data_git_describe = "v0.0-14772-gdd77381064"
data_git_msg = """\
commit dd77381064eee512cd82d5747e2d59e7c768c6c0
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Oct 24 11:21:25 2022 -0700

    [flash_ctrl/doc] Update hjson description.
    
    The flash disable descritpion was incorrect as it claimed
    any value other than false would cause disable. This is not
    true as the register is `rw0c` and not `rw` type.
    
    Update the description to reflect this.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
