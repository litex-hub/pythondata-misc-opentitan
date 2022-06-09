import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12597"
version_tuple = (0, 0, 12597)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12597")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12455"
data_version_tuple = (0, 0, 12455)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12455")
except ImportError:
    pass
data_git_hash = "681b4c53dd885f052f2f7e17387e3459a0e54cd1"
data_git_describe = "v0.0-12455-g681b4c53d"
data_git_msg = """\
commit 681b4c53dd885f052f2f7e17387e3459a0e54cd1
Author: Alphan Ulusoy <alphan@google.com>
Date:   Tue Jun 7 06:51:25 2022 -0400

    [sw/silicon_creator] Remove OT_IS_ENGLISH_BREAKFAST from lifecycle.c
    
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
