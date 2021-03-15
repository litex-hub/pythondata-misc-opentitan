import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5388"
version_tuple = (0, 0, 5388)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5388")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5293"
data_version_tuple = (0, 0, 5293)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5293")
except ImportError:
    pass
data_git_hash = "58b9bf2326c522ac8869e69524386736ea79a961"
data_git_describe = "v0.0-5293-g58b9bf232"
data_git_msg = """\
commit 58b9bf2326c522ac8869e69524386736ea79a961
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Mon Mar 15 09:11:23 2021 -0700

    [csrng/dv] Added alerts
    
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
