import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14821"
version_tuple = (0, 0, 14821)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14821")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14679"
data_version_tuple = (0, 0, 14679)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14679")
except ImportError:
    pass
data_git_hash = "14a82273e226623cdb0abf3a74610b89121603f9"
data_git_describe = "v0.0-14679-g14a82273e2"
data_git_msg = """\
commit 14a82273e226623cdb0abf3a74610b89121603f9
Author: Alphan Ulusoy <alphan@google.com>
Date:   Sat Oct 15 20:12:10 2022 -0400

    [test] Add rom_e2e_sigverify_mod_exp
    
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
