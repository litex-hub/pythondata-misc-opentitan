import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14523"
version_tuple = (0, 0, 14523)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14523")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14381"
data_version_tuple = (0, 0, 14381)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14381")
except ImportError:
    pass
data_git_hash = "3cdeca44231439984dd01683df20979a442a40a2"
data_git_describe = "v0.0-14381-g3cdeca4423"
data_git_msg = """\
commit 3cdeca44231439984dd01683df20979a442a40a2
Author: Alphan Ulusoy <alphan@google.com>
Date:   Thu Sep 29 13:04:16 2022 -0400

    [test] Add rom_e2e_sigverify_key_auth
    
    Fixes #14478
    
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
