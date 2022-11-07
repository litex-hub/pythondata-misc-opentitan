import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15295"
version_tuple = (0, 0, 15295)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15295")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15153"
data_version_tuple = (0, 0, 15153)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15153")
except ImportError:
    pass
data_git_hash = "41330b19aec489f2fd4115e369389563e6453cd2"
data_git_describe = "v0.0-15153-g41330b19ae"
data_git_msg = """\
commit 41330b19aec489f2fd4115e369389563e6453cd2
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Nov 4 16:16:53 2022 -0700

    [i2c] Adjust bit count idx
    
    - do not increment bit count based on start
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    More clean-up
    
    Signed-off-by: Timothy Chen <timothytim@google.com>
    
    continued ...
    
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
