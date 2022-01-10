import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9400"
version_tuple = (0, 0, 9400)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9400")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9282"
data_version_tuple = (0, 0, 9282)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9282")
except ImportError:
    pass
data_git_hash = "1a55e94b62470c933d59e4d3dfedfc689eb0df76"
data_git_describe = "v0.0-9282-g1a55e94b6"
data_git_msg = """\
commit 1a55e94b62470c933d59e4d3dfedfc689eb0df76
Author: Alex Bradbury <asb@lowrisc.org>
Date:   Mon Jan 10 15:11:06 2022 +0000

    [site/landing] Add Winbond partner logo
    
    Signed-off-by: Alex Bradbury <asb@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
