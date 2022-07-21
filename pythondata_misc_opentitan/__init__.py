import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13231"
version_tuple = (0, 0, 13231)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13231")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13089"
data_version_tuple = (0, 0, 13089)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13089")
except ImportError:
    pass
data_git_hash = "aaa96c532401e30201f80d0f032f60962578f5b2"
data_git_describe = "v0.0-13089-gaaa96c5324"
data_git_msg = """\
commit aaa96c532401e30201f80d0f032f60962578f5b2
Author: Weicai Yang <weicai@google.com>
Date:   Thu Jul 21 11:32:29 2022 -0700

    [spi_device/dv] Support testing JEDEC command
    
    Enable testing it in intercept_vseq and pass_all_vseq
    Update scb to check the returne data
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
