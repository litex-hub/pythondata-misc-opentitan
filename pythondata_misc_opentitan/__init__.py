import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5455"
version_tuple = (0, 0, 5455)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5455")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5360"
data_version_tuple = (0, 0, 5360)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5360")
except ImportError:
    pass
data_git_hash = "6307c2a178b90b0ceb63f4e620d2f53223705a63"
data_git_describe = "v0.0-5360-g6307c2a17"
data_git_msg = """\
commit 6307c2a178b90b0ceb63f4e620d2f53223705a63
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 18 08:56:48 2021 +0000

    [lint] Waive Verilator warning about filename for dm package
    
    This file is vendored, so we don't really want to change it. Waive the
    warning instead.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
