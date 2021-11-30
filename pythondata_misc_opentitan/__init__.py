import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8909"
version_tuple = (0, 0, 8909)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8909")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8797"
data_version_tuple = (0, 0, 8797)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8797")
except ImportError:
    pass
data_git_hash = "ba63d1e6ad6702cfb661f8fd8233d9bfb5f692ea"
data_git_describe = "v0.0-8797-gba63d1e6a"
data_git_msg = """\
commit ba63d1e6ad6702cfb661f8fd8233d9bfb5f692ea
Author: kosta-kojdic <kosta.kojdic@ensilica.com>
Date:   Tue Nov 30 13:08:00 2021 +0000

    CSB Selection Implemented
    
    Signed-off-by: kosta-kojdic <kosta.kojdic@ensilica.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
