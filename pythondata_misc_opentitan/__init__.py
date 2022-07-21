import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13213"
version_tuple = (0, 0, 13213)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13213")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13071"
data_version_tuple = (0, 0, 13071)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13071")
except ImportError:
    pass
data_git_hash = "bc7af960ed4665ae6cd9e2577fa68f83f9ab16be"
data_git_describe = "v0.0-13071-gbc7af960ed"
data_git_msg = """\
commit bc7af960ed4665ae6cd9e2577fa68f83f9ab16be
Author: Weicai Yang <weicai@google.com>
Date:   Wed Jul 20 13:01:26 2022 -0700

    [spi_device/dv] Add read status intercept sequence
    
    1. Test 3 read status intercept and compare returned data in scb
    2. Add spi_device_pass_all_vseq which enables all passthrough features
    in one seq
    3. deleted quad/dual_vseq as they don't need to be tested in a dedicated test
    
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
