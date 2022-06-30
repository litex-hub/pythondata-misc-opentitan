import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12897"
version_tuple = (0, 0, 12897)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12897")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12755"
data_version_tuple = (0, 0, 12755)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12755")
except ImportError:
    pass
data_git_hash = "749ef4f591c2587c251cda3a1eafab7a7cd730e2"
data_git_describe = "v0.0-12755-g749ef4f591"
data_git_msg = """\
commit 749ef4f591c2587c251cda3a1eafab7a7cd730e2
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Jun 30 07:22:48 2022 -0400

    [util] Make util/generate_compilation_db.py compatiable with python 3.6
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
