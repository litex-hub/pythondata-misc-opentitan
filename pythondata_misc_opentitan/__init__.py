import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8411"
version_tuple = (0, 0, 8411)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8411")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8299"
data_version_tuple = (0, 0, 8299)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8299")
except ImportError:
    pass
data_git_hash = "e22f87e96487471b7c4117c133ab60069d767cef"
data_git_describe = "v0.0-8299-ge22f87e96"
data_git_msg = """\
commit e22f87e96487471b7c4117c133ab60069d767cef
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Oct 22 01:02:34 2021 +0000

    [dif] Fix typos in autogen'd DIF comments.
    
    This commit fixes the autogen DIF templates to remove typos in generated
    code comments as requested in the review comments of #8775 and #8780.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
