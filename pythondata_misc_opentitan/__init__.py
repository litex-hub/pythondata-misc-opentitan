import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12782"
version_tuple = (0, 0, 12782)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12782")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12640"
data_version_tuple = (0, 0, 12640)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12640")
except ImportError:
    pass
data_git_hash = "c663c108c51ff3179395eb36a69b675bbd075af5"
data_git_describe = "v0.0-12640-gc663c108c5"
data_git_msg = """\
commit c663c108c51ff3179395eb36a69b675bbd075af5
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Jun 21 23:43:22 2022 -0400

    [lib] Fix hardened memory functions
    
    All three functions had the same bug: The second argument of
    `ct_sltuw()` should have been in bytes not words.
    
    Fixes #12350
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
