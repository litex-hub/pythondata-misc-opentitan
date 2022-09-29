import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14498"
version_tuple = (0, 0, 14498)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14498")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14356"
data_version_tuple = (0, 0, 14356)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14356")
except ImportError:
    pass
data_git_hash = "43ad5a53274c5d62c544140ff02a369c5d3d3144"
data_git_describe = "v0.0-14356-g43ad5a5327"
data_git_msg = """\
commit 43ad5a53274c5d62c544140ff02a369c5d3d3144
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Sep 28 17:58:10 2022 -0700

    [dv/sv] Fix comment typos and improve format
    
    This only changes comments.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
