import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8175"
version_tuple = (0, 0, 8175)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8175")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8063"
data_version_tuple = (0, 0, 8063)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8063")
except ImportError:
    pass
data_git_hash = "b46a08d07671c9d6c020e54fb44424f1611c43a0"
data_git_describe = "v0.0-8063-gb46a08d07"
data_git_msg = """\
commit b46a08d07671c9d6c020e54fb44424f1611c43a0
Author: Miguel Osorio <miguelosorio@google.com>
Date:   Sun Oct 3 10:30:11 2021 -0700

    [util] Splice for prod ROM
    
    Signed-off-by: Miguel Osorio <miguelosorio@google.com>

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
