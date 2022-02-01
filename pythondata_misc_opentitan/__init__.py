import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9959"
version_tuple = (0, 0, 9959)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9959")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9835"
data_version_tuple = (0, 0, 9835)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9835")
except ImportError:
    pass
data_git_hash = "553759a3928c85f48d5bf56bc08f32d919eb21f7"
data_git_describe = "v0.0-9835-g553759a39"
data_git_msg = """\
commit 553759a3928c85f48d5bf56bc08f32d919eb21f7
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Jan 28 18:32:37 2022 +0100

    [aes] Use one-hot encoding for OPERATION field in main control register
    
    This is related to lowRISC/OpenTitan#10422.
    
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
