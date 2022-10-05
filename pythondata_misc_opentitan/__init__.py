import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14566"
version_tuple = (0, 0, 14566)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14566")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14424"
data_version_tuple = (0, 0, 14424)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14424")
except ImportError:
    pass
data_git_hash = "6c710842200064ace0bcf6da58605e6ce57fb1b4"
data_git_describe = "v0.0-14424-g6c71084220"
data_git_msg = """\
commit 6c710842200064ace0bcf6da58605e6ce57fb1b4
Author: Guillermo Maturana <maturana@google.com>
Date:   Thu Sep 29 09:58:07 2022 -0700

    [rtl/prim] Fix some prim_esc_receiver SVAs
    
    Delay the start of EscRespCheck_A by a cycle because it uses $past.
    Minor formatting changes.
    
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
