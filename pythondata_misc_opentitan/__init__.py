import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14302"
version_tuple = (0, 0, 14302)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14302")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14160"
data_version_tuple = (0, 0, 14160)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14160")
except ImportError:
    pass
data_git_hash = "4278b4be90f15e45ef6e66b127b345b4b0227851"
data_git_describe = "v0.0-14160-g4278b4be90"
data_git_msg = """\
commit 4278b4be90f15e45ef6e66b127b345b4b0227851
Author: Jade Philipoom <jadep@google.com>
Date:   Wed Sep 14 09:57:15 2022 +0200

    [crypto] Update cryptolib OTBN driver based on silicon_creator version.
    
    Since the cryptolib's OTBN driver was originally copied over from
    silicon_creator, extensive effort has been applied to hardening the
    silicon_creator version. This commit essentially replaces the cryptolib
    OTBN driver with the silicon_creator version in order to take advantage
    of the existing hardening effort.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
