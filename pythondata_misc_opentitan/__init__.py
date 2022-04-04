import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11322"
version_tuple = (0, 0, 11322)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11322")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11196"
data_version_tuple = (0, 0, 11196)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11196")
except ImportError:
    pass
data_git_hash = "83393ce973773679c56777566f5818eb7e5f5e08"
data_git_describe = "v0.0-11196-g83393ce97"
data_git_msg = """\
commit 83393ce973773679c56777566f5818eb7e5f5e08
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue Mar 22 15:10:11 2022 +0000

    [test, aes] Add aes idle chip level test
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
