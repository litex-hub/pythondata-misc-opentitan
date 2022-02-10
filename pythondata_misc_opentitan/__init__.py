import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10217"
version_tuple = (0, 0, 10217)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10217")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10093"
data_version_tuple = (0, 0, 10093)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10093")
except ImportError:
    pass
data_git_hash = "150283a774a5c4ab6c4174d20310c16abcc5f650"
data_git_describe = "v0.0-10093-g150283a77"
data_git_msg = """\
commit 150283a774a5c4ab6c4174d20310c16abcc5f650
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Feb 8 16:45:46 2022 +0100

    [aes] Stop clearing status and trigger register to zero on fatal alerts
    
    This is related to lowRISC/OpenTitan#8460.
    
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
