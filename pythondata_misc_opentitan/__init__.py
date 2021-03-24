import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5564"
version_tuple = (0, 0, 5564)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5564")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5469"
data_version_tuple = (0, 0, 5469)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5469")
except ImportError:
    pass
data_git_hash = "2e6a6c60964fac43b9dfd3a9de5057154107248d"
data_git_describe = "v0.0-5469-g2e6a6c609"
data_git_msg = """\
commit 2e6a6c60964fac43b9dfd3a9de5057154107248d
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Mar 23 15:43:08 2021 +0100

    [aes] Add documentation on security hardening, enable masking by default
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
