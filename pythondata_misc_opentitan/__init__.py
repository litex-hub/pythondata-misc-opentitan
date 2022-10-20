import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14862"
version_tuple = (0, 0, 14862)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14862")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14720"
data_version_tuple = (0, 0, 14720)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14720")
except ImportError:
    pass
data_git_hash = "26f2ee3db18fadbb4198bc763aba61b44b64e558"
data_git_describe = "v0.0-14720-g26f2ee3db1"
data_git_msg = """\
commit 26f2ee3db18fadbb4198bc763aba61b44b64e558
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Mon Oct 10 18:39:59 2022 -0700

    [dv/chip] Skip creating dv_base_reg coverage
    
    This PR adds the following flag:
    In dv_base_reg_block, add a flag to skip creating fcov for mubi and
    regwen regs.
    
    This flag is only disabled in chip level because we do not sample these
    values in chip level env.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

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
