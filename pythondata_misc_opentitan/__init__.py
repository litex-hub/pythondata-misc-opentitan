import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8530"
version_tuple = (0, 0, 8530)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8530")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8418"
data_version_tuple = (0, 0, 8418)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8418")
except ImportError:
    pass
data_git_hash = "6ea17364f2dc9507e9b671f76f038ea7d953a76d"
data_git_describe = "v0.0-8418-g6ea17364f"
data_git_msg = """\
commit 6ea17364f2dc9507e9b671f76f038ea7d953a76d
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Oct 25 15:36:32 2021 +0100

    [otbn,dv] Avoid writing to STATUS in csr_hw_reset test
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
