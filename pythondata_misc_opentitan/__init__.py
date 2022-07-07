import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12956"
version_tuple = (0, 0, 12956)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12956")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12814"
data_version_tuple = (0, 0, 12814)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12814")
except ImportError:
    pass
data_git_hash = "be73450cd45b20afa4153e064d83f18d66074999"
data_git_describe = "v0.0-12814-gbe73450cd4"
data_git_msg = """\
commit be73450cd45b20afa4153e064d83f18d66074999
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue Jul 5 11:35:22 2022 +0100

    [test, aes] Add chip level test aes_sideload_test
    
    Fixes #13232
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
