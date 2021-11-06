import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8619"
version_tuple = (0, 0, 8619)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8619")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8507"
data_version_tuple = (0, 0, 8507)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8507")
except ImportError:
    pass
data_git_hash = "7dd8ba4dc8e5d77f3b77b4ba16af57b0a4804591"
data_git_describe = "v0.0-8507-g7dd8ba4dc"
data_git_msg = """\
commit 7dd8ba4dc8e5d77f3b77b4ba16af57b0a4804591
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Fri Nov 5 17:14:34 2021 -0700

    [fpv/secded] Fix FPV auto-gen script
    
    In previous PR where we renamed the FPV testbench to `_tb` suffix. I
    manually changed the FPV files, but did not change the template.
    This PR updates the FPV template for gen_secded.py
    
    Thanks Tim for finding the issue.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
