import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14544"
version_tuple = (0, 0, 14544)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14544")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14402"
data_version_tuple = (0, 0, 14402)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14402")
except ImportError:
    pass
data_git_hash = "3cd03728a90b2e5b6d55b9d79a27fd64555a2082"
data_git_describe = "v0.0-14402-g3cd03728a9"
data_git_msg = """\
commit 3cd03728a90b2e5b6d55b9d79a27fd64555a2082
Author: Weicai Yang <weicai@google.com>
Date:   Mon Oct 3 16:41:21 2022 -0700

    [spi_device] Fix CmdAddrInfo_A assertion
    
    Need to add a condition - is_tpm_reg before checking the addr
    Without is_tpm_reg, locality won't be latched
    
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
