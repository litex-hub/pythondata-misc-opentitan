import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9516"
version_tuple = (0, 0, 9516)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9516")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9395"
data_version_tuple = (0, 0, 9395)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9395")
except ImportError:
    pass
data_git_hash = "aae9bf89d25cbd877fa54f1e0fe448fc408f45d9"
data_git_describe = "v0.0-9395-gaae9bf89d"
data_git_msg = """\
commit aae9bf89d25cbd877fa54f1e0fe448fc408f45d9
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Jan 12 12:26:28 2022 -0800

    [ci] Add pwrmgr_smoketest to private CI
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

"""

# Tool version info
tool_version_str = "0.0.post121"
tool_version_tuple = (0, 0, 121)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post121")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
