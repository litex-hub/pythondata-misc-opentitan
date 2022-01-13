import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9511"
version_tuple = (0, 0, 9511)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9511")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9391"
data_version_tuple = (0, 0, 9391)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9391")
except ImportError:
    pass
data_git_hash = "5ef1bff3de774e7c58e0a61bb64d383e30440c4c"
data_git_describe = "v0.0-9391-g5ef1bff3d"
data_git_msg = """\
commit 5ef1bff3de774e7c58e0a61bb64d383e30440c4c
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Wed Jan 12 04:28:58 2022 -0800

    [edn/dv] Add scoreboard checking
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post120"
tool_version_tuple = (0, 0, 120)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post120")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
