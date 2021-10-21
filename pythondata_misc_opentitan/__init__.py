import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8374"
version_tuple = (0, 0, 8374)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8374")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8262"
data_version_tuple = (0, 0, 8262)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8262")
except ImportError:
    pass
data_git_hash = "5feafbe44e8fc9e19c280a5b1183dac67ac90cea"
data_git_describe = "v0.0-8262-g5feafbe44"
data_git_msg = """\
commit 5feafbe44e8fc9e19c280a5b1183dac67ac90cea
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Oct 20 17:17:52 2021 -0400

    [sw/silicon_creator] Fix typo in bootstrap module enum name
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

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
