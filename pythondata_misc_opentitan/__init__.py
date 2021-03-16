import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5407"
version_tuple = (0, 0, 5407)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5407")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5312"
data_version_tuple = (0, 0, 5312)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5312")
except ImportError:
    pass
data_git_hash = "9b819fbff4d6f92a440b4c8e075d6fc25d7316f7"
data_git_describe = "v0.0-5312-g9b819fbff"
data_git_msg = """\
commit 9b819fbff4d6f92a440b4c8e075d6fc25d7316f7
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Mon Mar 15 11:38:47 2021 -0700

    [edn/dv] Added alerts
    
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
