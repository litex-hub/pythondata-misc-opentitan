import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13249"
version_tuple = (0, 0, 13249)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13249")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13107"
data_version_tuple = (0, 0, 13107)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13107")
except ImportError:
    pass
data_git_hash = "248c03a7dedb172d6a47bf4f1618dc2e37f6c95d"
data_git_describe = "v0.0-13107-g248c03a7de"
data_git_msg = """\
commit 248c03a7dedb172d6a47bf4f1618dc2e37f6c95d
Author: Weicai Yang <weicai@google.com>
Date:   Thu Jul 21 16:19:12 2022 -0700

    [spi_device/dv] Enable testing SFDP command
    
    Similar to the JEDEC command, enable testing it in intercept_vseq and
    pass_all_vseq.
    
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
