import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14589"
version_tuple = (0, 0, 14589)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14589")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14447"
data_version_tuple = (0, 0, 14447)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14447")
except ImportError:
    pass
data_git_hash = "2a73d673e16f91027d7d6898b2f0df9fe68b975c"
data_git_describe = "v0.0-14447-g2a73d673e1"
data_git_msg = """\
commit 2a73d673e16f91027d7d6898b2f0df9fe68b975c
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Oct 5 19:47:35 2022 -0400

    [doc] Fix typo in manifest.md
    
    Thanks for catching this @cdgori!
    
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
