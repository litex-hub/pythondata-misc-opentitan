import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10179"
version_tuple = (0, 0, 10179)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10179")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10055"
data_version_tuple = (0, 0, 10055)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10055")
except ImportError:
    pass
data_git_hash = "40848841bd43fecd1048c3fbe9cf2b2da02e9cc3"
data_git_describe = "v0.0-10055-g40848841b"
data_git_msg = """\
commit 40848841bd43fecd1048c3fbe9cf2b2da02e9cc3
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Jan 25 16:59:10 2022 +0100

    [aes/pre_sca] Specify tool versions known to work with the Alma flow
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
