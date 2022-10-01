import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14531"
version_tuple = (0, 0, 14531)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14531")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14389"
data_version_tuple = (0, 0, 14389)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14389")
except ImportError:
    pass
data_git_hash = "67a41e3bc3ff025554a024cdb15fbf892c4752b3"
data_git_describe = "v0.0-14389-g67a41e3bc3"
data_git_msg = """\
commit 67a41e3bc3ff025554a024cdb15fbf892c4752b3
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Sep 21 11:42:16 2022 -0700

    [i2c] fix target mode start / stop handling
    
    - instead of looking for start / stop in specific states, jump directly
      to AcquireSrP when in target mode.
    
    - stop detection is cleared in AcquireSrP, while start_detection is
      only cleared once we cycle through start address decode handling
      again.
    
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
