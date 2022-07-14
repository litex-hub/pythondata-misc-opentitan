import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13068"
version_tuple = (0, 0, 13068)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13068")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12926"
data_version_tuple = (0, 0, 12926)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12926")
except ImportError:
    pass
data_git_hash = "97f24da8bb488090e716ce829f0684f66d2196e5"
data_git_describe = "v0.0-12926-g97f24da8bb"
data_git_msg = """\
commit 97f24da8bb488090e716ce829f0684f66d2196e5
Author: Weicai Yang <weicai@google.com>
Date:   Wed Jul 13 14:24:38 2022 -0700

    [spi/dv] some renames
    
    no functional update, just rename as follows, in order to avoid confusion
    1. m_spi_agent -> spi_host_agent
    2. in scb, add downstream/upstream prefix for spi variables/functions
    
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
