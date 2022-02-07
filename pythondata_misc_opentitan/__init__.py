import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10110"
version_tuple = (0, 0, 10110)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10110")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9986"
data_version_tuple = (0, 0, 9986)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9986")
except ImportError:
    pass
data_git_hash = "8eb1639b9a7b3709705b46e20f246c7bb5693de2"
data_git_describe = "v0.0-9986-g8eb1639b9"
data_git_msg = """\
commit 8eb1639b9a7b3709705b46e20f246c7bb5693de2
Author: Weicai Yang <weicai@google.com>
Date:   Fri Feb 4 14:41:56 2022 -0800

    [dv] Clean up mem_bkdr_util__sram
    
    1. Use the new get_addr function as Tim suggested #10613
    2. clean up unused write/read functions. Only the read32/write32_integ
       is applicable
    Signed-off-by: Weicai Yang <weicai@google.com>

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
