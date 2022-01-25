import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9760"
version_tuple = (0, 0, 9760)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9760")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9638"
data_version_tuple = (0, 0, 9638)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9638")
except ImportError:
    pass
data_git_hash = "608c35c8c0a1aa7c46fdfa7855fad17309c31a4a"
data_git_describe = "v0.0-9638-g608c35c8c"
data_git_msg = """\
commit 608c35c8c0a1aa7c46fdfa7855fad17309c31a4a
Author: Michael Tempelmeier <michael.tempelmeier@gi-de.com>
Date:   Wed Dec 15 17:42:30 2021 +0100

    [kmac/entropy_src] added prim_count for keccak_round counter
    
    Signed-off-by: Michael Tempelmeier <michael.tempelmeier@gi-de.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
