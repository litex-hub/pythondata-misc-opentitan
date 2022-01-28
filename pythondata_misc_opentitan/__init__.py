import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9856"
version_tuple = (0, 0, 9856)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9856")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9732"
data_version_tuple = (0, 0, 9732)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9732")
except ImportError:
    pass
data_git_hash = "369cffc85db0e6d5a667676a6f89987b94210e70"
data_git_describe = "v0.0-9732-g369cffc85"
data_git_msg = """\
commit 369cffc85db0e6d5a667676a6f89987b94210e70
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jan 26 15:23:48 2022 -0800

    [prim] Update behavior of prim_count
    
    - During cross count, compare is always valid
    - When a "max value" has not been supplied, the counter always compares
      the default value of 0 and max count size
    - When a "max value" is supplied, normal comparisons are made
    - When the counter is cleared, the counts are restored to the default
      comparison points.  It is up to the user to supply the max value again.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
