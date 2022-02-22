import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10462"
version_tuple = (0, 0, 10462)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10462")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10336"
data_version_tuple = (0, 0, 10336)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10336")
except ImportError:
    pass
data_git_hash = "0d2da6b2eb9910952b006295c5a674c2389edb27"
data_git_describe = "v0.0-10336-g0d2da6b2e"
data_git_msg = """\
commit 0d2da6b2eb9910952b006295c5a674c2389edb27
Author: Weicai Yang <weicai@google.com>
Date:   Thu Feb 17 15:08:53 2022 -0800

    [sram/dv] Update scb
    
    No real function update. Only remove unused functions and create a
    function `reset_key_nonce` to reduce replication
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
