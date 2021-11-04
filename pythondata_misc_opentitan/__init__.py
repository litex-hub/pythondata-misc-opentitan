import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8584"
version_tuple = (0, 0, 8584)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8584")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8472"
data_version_tuple = (0, 0, 8472)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8472")
except ImportError:
    pass
data_git_hash = "e4bfe80f68668e88f9023a2a359d50cc0060655f"
data_git_describe = "v0.0-8472-ge4bfe80f6"
data_git_msg = """\
commit e4bfe80f68668e88f9023a2a359d50cc0060655f
Author: Jacob Levy <jacob.levy@opentitan.org>
Date:   Sun Oct 24 11:12:47 2021 +0300

    [ast] Update review comments
    
    Signed-off-by: Jacob Levy <jacob.levy@opentitan.org>

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
