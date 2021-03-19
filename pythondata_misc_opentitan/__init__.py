import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5493"
version_tuple = (0, 0, 5493)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5493")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5398"
data_version_tuple = (0, 0, 5398)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5398")
except ImportError:
    pass
data_git_hash = "d0f8ea619a9aed32aa62a83ff5c14dad12fbfadf"
data_git_describe = "v0.0-5398-gd0f8ea619"
data_git_msg = """\
commit d0f8ea619a9aed32aa62a83ff5c14dad12fbfadf
Author: Jacob Levy <jacob.levy@opentitan.org>
Date:   Fri Mar 19 11:29:55 2021 +0200

    [TLUL] Add ecc calculation functions
    
    Signed-off-by: Jacob Levy <jacob.levy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
