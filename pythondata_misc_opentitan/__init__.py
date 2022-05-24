import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12288"
version_tuple = (0, 0, 12288)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12288")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12160"
data_version_tuple = (0, 0, 12160)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12160")
except ImportError:
    pass
data_git_hash = "0d83958e04a0f44114fef1c5d0764ca0841cd785"
data_git_describe = "v0.0-12160-g0d83958e0"
data_git_msg = """\
commit 0d83958e04a0f44114fef1c5d0764ca0841cd785
Author: Weicai Yang <weicai@google.com>
Date:   Sun May 22 23:36:53 2022 -0700

    [top, dv] Add chip_tap_straps_prod
    
    1. Test tap straps at LC prod state
    2. force tap inputs to test DFT tap is connected correctly. This is to
       do connectivity test for DFT tap as it's just a dummy module in
       open-source.
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
