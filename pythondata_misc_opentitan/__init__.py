import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13321"
version_tuple = (0, 0, 13321)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13321")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13179"
data_version_tuple = (0, 0, 13179)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13179")
except ImportError:
    pass
data_git_hash = "0ca714ff4e77b12c0c74e94b7f13ed78b6127121"
data_git_describe = "v0.0-13179-g0ca714ff4e"
data_git_msg = """\
commit 0ca714ff4e77b12c0c74e94b7f13ed78b6127121
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jul 27 16:02:50 2022 -0700

    [sw/flash_ctrl] remove software mention of flash macro error
    
    - flash macro error is no longer part of the recoverable error
      codes. Make corresponding changes in the dif and testutils
    
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
