import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11545"
version_tuple = (0, 0, 11545)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11545")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11419"
data_version_tuple = (0, 0, 11419)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11419")
except ImportError:
    pass
data_git_hash = "79a3d01253a7e6d32bac88bd8096a0c2b0051ea6"
data_git_describe = "v0.0-11419-g79a3d0125"
data_git_msg = """\
commit 79a3d01253a7e6d32bac88bd8096a0c2b0051ea6
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Apr 8 15:52:55 2022 +0100

    [otbn,rtl] Signal done on escalation when waiting for URND
    
    As far as the external model of OTBN is concerned, an operation has
    started. So we should ping the "done" interrupt as we lock ourselves.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
