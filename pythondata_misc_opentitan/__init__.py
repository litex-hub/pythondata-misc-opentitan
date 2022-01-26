import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9806"
version_tuple = (0, 0, 9806)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9806")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9684"
data_version_tuple = (0, 0, 9684)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9684")
except ImportError:
    pass
data_git_hash = "250a94b38c1aad9b6f5b1f606e0d3f375cd11d16"
data_git_describe = "v0.0-9684-g250a94b38"
data_git_msg = """\
commit 250a94b38c1aad9b6f5b1f606e0d3f375cd11d16
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Fri Jan 21 13:23:31 2022 -0800

    [edn/dv] Verify boot_req_mode
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
