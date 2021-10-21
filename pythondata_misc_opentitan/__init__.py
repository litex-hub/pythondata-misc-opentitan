import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8368"
version_tuple = (0, 0, 8368)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8368")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8256"
data_version_tuple = (0, 0, 8256)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8256")
except ImportError:
    pass
data_git_hash = "13b4afba9b7f04445d061e446e7201762395c5fa"
data_git_describe = "v0.0-8256-g13b4afba9"
data_git_msg = """\
commit 13b4afba9b7f04445d061e446e7201762395c5fa
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 20 00:54:23 2021 +0000

    [dif] Autogen all `dif_<ip>_init()` DIFs for all IPs.
    
    This is the last task that fixes #8409.
    
    This commit:
    1. updates the DIF autogen templates to auto-generate the
       `dif_<ip>_init()` DIF and corresponding unit tests for all IPs,
    2. re-auto-generates all IP's (autogen'd) DIFs, and
    3. deprecates all manually defined `dif_<ip>_init()` DIFs and unit
       tests.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
