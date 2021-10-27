import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8472"
version_tuple = (0, 0, 8472)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8472")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8360"
data_version_tuple = (0, 0, 8360)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8360")
except ImportError:
    pass
data_git_hash = "f18f37367b31af0bd51227c0879be604d129064b"
data_git_describe = "v0.0-8360-gf18f37367"
data_git_msg = """\
commit f18f37367b31af0bd51227c0879be604d129064b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Oct 26 14:59:32 2021 +0100

    [otbn,dv] Modify bigla test to work with 2kiB DMEM window
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
