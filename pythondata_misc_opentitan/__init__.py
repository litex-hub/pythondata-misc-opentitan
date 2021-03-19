import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5483"
version_tuple = (0, 0, 5483)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5483")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5388"
data_version_tuple = (0, 0, 5388)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5388")
except ImportError:
    pass
data_git_hash = "f63bf6a5e8bb5f74665420c6b988a757cacc927e"
data_git_describe = "v0.0-5388-gf63bf6a5e"
data_git_msg = """\
commit f63bf6a5e8bb5f74665420c6b988a757cacc927e
Author: Weicai Yang <weicai@google.com>
Date:   Thu Mar 18 13:48:30 2021 -0700

    [xbar/dv] Fix assertion error due to short reset
    
    xbar has 2 clock domains. reset needs to last for at least one clock to
    avoid false alarm from SVA as assertion checks reset at the active clock
    edge.
    increase reset to 50-100 TL clock periods, which should be long enough
    for most of IPs. (default faster clock / slowest clock < 10)
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
