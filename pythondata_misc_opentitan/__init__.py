import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10997"
version_tuple = (0, 0, 10997)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10997")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10871"
data_version_tuple = (0, 0, 10871)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10871")
except ImportError:
    pass
data_git_hash = "70a63d44f0a14edd3a7cae3847fd7476895f2563"
data_git_describe = "v0.0-10871-g70a63d44f"
data_git_msg = """\
commit 70a63d44f0a14edd3a7cae3847fd7476895f2563
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Mar 4 14:32:10 2022 +0100

    [aes] Clear START trigger when ignoring it
    
    The START trigger is ignored by the AES unit when the current
    configuration is invalid (MODE = AES_NONE) or when performing automatic
    operation (MANUAL_OPERATION = 0). When ignoring it, it's better to
    clear this trigger bit back to 0 to avoid the unintentional operations
    to start once a valid configuration is written or manual operation is
    enabled.
    
    This resolves lowRISC/OpenTitan#11166.
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
