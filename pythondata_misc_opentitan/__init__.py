import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9943"
version_tuple = (0, 0, 9943)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9943")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9819"
data_version_tuple = (0, 0, 9819)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9819")
except ImportError:
    pass
data_git_hash = "a40e387cfb5aa154ff6311e0a2101670cf7e52db"
data_git_describe = "v0.0-9819-ga40e387cf"
data_git_msg = """\
commit a40e387cfb5aa154ff6311e0a2101670cf7e52db
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Jan 27 09:42:24 2022 -0800

    [dv] Fix some Xcelium warnings
    
    These are some of them:
    - Imporing packages in classes (only modules and packages can import
      other packages)
    - Missing return type on functions
    - Incorrect signal type
    - Some code reorg (without changing functionality)
    - Line length exceeded
    - Assign integer to unsigned signals
    - Cast raw signals to enum when assigning to enum literals
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
