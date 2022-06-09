import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12587"
version_tuple = (0, 0, 12587)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12587")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12445"
data_version_tuple = (0, 0, 12445)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12445")
except ImportError:
    pass
data_git_hash = "f3252d358b5e16ac5b4402aac466e2f40ca9bebe"
data_git_describe = "v0.0-12445-gf3252d358"
data_git_msg = """\
commit f3252d358b5e16ac5b4402aac466e2f40ca9bebe
Author: Yen-Kai Wang <ykwang@google.com>
Date:   Wed Jun 8 12:33:58 2022 -0500

    Rename project target from '@' into '@lowrisc_opentitan'.
    
    Signed-off-by: Yen-Kai Wang <ykwang@google.com>

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
