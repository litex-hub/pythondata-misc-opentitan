import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14484"
version_tuple = (0, 0, 14484)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14484")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14342"
data_version_tuple = (0, 0, 14342)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14342")
except ImportError:
    pass
data_git_hash = "87ad4f063e9f06a978922ecdc251fc088845f6d9"
data_git_describe = "v0.0-14342-g87ad4f063e"
data_git_msg = """\
commit 87ad4f063e9f06a978922ecdc251fc088845f6d9
Author: Eli Kim <eli@opentitan.org>
Date:   Tue Sep 27 15:02:45 2022 -0700

    refactor(dvsim): Remove `verdi` checker
    
    dvsim checks if `verdi` tool is searchable to dump `.fsdb` waveform.
    However, it is not applicable if dvsim launches the task to LSF or cloud
    farm.
    
    This commit removes the checker and let users to specify the waveform
    type with `-w {type}` argument.
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
