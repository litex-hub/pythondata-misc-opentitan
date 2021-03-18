import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5456"
version_tuple = (0, 0, 5456)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5456")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5361"
data_version_tuple = (0, 0, 5361)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5361")
except ImportError:
    pass
data_git_hash = "b1e4b6d9f02e98546200ca88a147a370f3ecc8ef"
data_git_describe = "v0.0-5361-gb1e4b6d9f"
data_git_msg = """\
commit b1e4b6d9f02e98546200ca88a147a370f3ecc8ef
Author: Tom Roberts <tomroberts@lowrisc.org>
Date:   Tue Mar 16 15:43:44 2021 +0000

    [aon_timer/rtl] Fix bugs found by smoke test
    
    Lifecycle input signals are the wrong way around.
    Only clock the prescale counter when enabled.
    
    Relates to #5624
    
    Signed-off-by: Tom Roberts <tomroberts@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
