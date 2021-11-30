import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8888"
version_tuple = (0, 0, 8888)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8888")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8776"
data_version_tuple = (0, 0, 8776)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8776")
except ImportError:
    pass
data_git_hash = "4d875cf4acae78db035a275d9080c2e8b84fe7a7"
data_git_describe = "v0.0-8776-g4d875cf4a"
data_git_msg = """\
commit 4d875cf4acae78db035a275d9080c2e8b84fe7a7
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Fri Nov 12 16:29:01 2021 +0000

    [sw, tests] Introduce retention SRAM execution test
    
    This test makes sure that execution from SRAM is disabled.
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
