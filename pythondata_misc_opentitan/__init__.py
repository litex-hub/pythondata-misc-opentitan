import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14699"
version_tuple = (0, 0, 14699)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14699")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14557"
data_version_tuple = (0, 0, 14557)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14557")
except ImportError:
    pass
data_git_hash = "380178dc3ac3bbf79e4e605b732e599c3f46fa1e"
data_git_describe = "v0.0-14557-g380178dc3a"
data_git_msg = """\
commit 380178dc3ac3bbf79e4e605b732e599c3f46fa1e
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Oct 12 07:51:22 2022 -0400

    [sw/silicon_creator] Describe bits 5:0 masking behavior for cpuctrl
    
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
