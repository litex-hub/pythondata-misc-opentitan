import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8557"
version_tuple = (0, 0, 8557)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8557")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8445"
data_version_tuple = (0, 0, 8445)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8445")
except ImportError:
    pass
data_git_hash = "db602db1f2063ded0b94dfd3d653615bf2898982"
data_git_describe = "v0.0-8445-gdb602db1f"
data_git_msg = """\
commit db602db1f2063ded0b94dfd3d653615bf2898982
Author: Alphan Ulusoy <alphan@google.com>
Date:   Mon Nov 1 16:42:29 2021 -0400

    [sw/silicon_creator] Fix comment typo in sigverify_mod_exp_ibex.c
    
    Signed-off-by: Alphan Ulusoy <alphan@google.com>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
