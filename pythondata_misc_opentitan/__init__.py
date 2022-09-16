import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14267"
version_tuple = (0, 0, 14267)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14267")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14125"
data_version_tuple = (0, 0, 14125)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14125")
except ImportError:
    pass
data_git_hash = "d4214070b91694a4656507cf705ec56e000219c7"
data_git_describe = "v0.0-14125-gd4214070b9"
data_git_msg = """\
commit d4214070b91694a4656507cf705ec56e000219c7
Author: Eli Kim <eli@opentitan.org>
Date:   Fri Sep 16 11:38:33 2022 -0700

    refactor(chip): Use override_test_status_and_finish()
    
    Signed-off-by: Eli Kim <eli@opentitan.org>

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
