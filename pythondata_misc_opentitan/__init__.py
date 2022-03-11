import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10843"
version_tuple = (0, 0, 10843)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10843")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10717"
data_version_tuple = (0, 0, 10717)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10717")
except ImportError:
    pass
data_git_hash = "5e07d95e2102e1392d2b2c4552a415a44f4b1638"
data_git_describe = "v0.0-10717-g5e07d95e2"
data_git_msg = """\
commit 5e07d95e2102e1392d2b2c4552a415a44f4b1638
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Thu Mar 10 09:36:48 2022 +0000

    Point fusesoc/edalize dependencies at a tag, not a branch
    
    Historically, these have pointed at the tip of the 'ot' branch, which
    seems like a bad idea for reproducibility. These "ot-0.1" tags point
    at where the branch is at the moment, and we can then switch to
    "ot-0.2" or whatever when we want to make changes.
    
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
