import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10604"
version_tuple = (0, 0, 10604)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10604")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10478"
data_version_tuple = (0, 0, 10478)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10478")
except ImportError:
    pass
data_git_hash = "d1b0f96fabe132c6a87001281e5b2847606635d0"
data_git_describe = "v0.0-10478-gd1b0f96fa"
data_git_msg = """\
commit d1b0f96fabe132c6a87001281e5b2847606635d0
Author: Jayesh Patel <jayesh@aarishtech.com>
Date:   Mon Feb 28 09:19:53 2022 -0500

    Correct documentation typo
    
    Signed-off-by: Jayesh Patel <jayesh@aarishtech.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
