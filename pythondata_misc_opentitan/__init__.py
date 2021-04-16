import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5891"
version_tuple = (0, 0, 5891)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5891")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5796"
data_version_tuple = (0, 0, 5796)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5796")
except ImportError:
    pass
data_git_hash = "63011da45db8257635c117517309f7d204325554"
data_git_describe = "v0.0-5796-g63011da45"
data_git_msg = """\
commit 63011da45db8257635c117517309f7d204325554
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Thu Apr 15 08:23:12 2021 -0700

    [edn/dv] Added cfg variables/knobs
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
