import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14467"
version_tuple = (0, 0, 14467)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14467")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14325"
data_version_tuple = (0, 0, 14325)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14325")
except ImportError:
    pass
data_git_hash = "db069385899684ae5b736270cb5ed3d8dd745b1a"
data_git_describe = "v0.0-14325-gdb06938589"
data_git_msg = """\
commit db069385899684ae5b736270cb5ed3d8dd745b1a
Author: Miles Dai <milesdai@google.com>
Date:   Mon Sep 26 16:02:08 2022 -0400

    [lint] Make the flake8 check mandatory on CI
    
    Signed-off-by: Miles Dai <milesdai@google.com>

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
