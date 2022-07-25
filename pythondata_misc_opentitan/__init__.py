import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13257"
version_tuple = (0, 0, 13257)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13257")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13115"
data_version_tuple = (0, 0, 13115)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13115")
except ImportError:
    pass
data_git_hash = "ebb8ace4620efb27ddcce11b8a912d4779ac8f56"
data_git_describe = "v0.0-13115-gebb8ace462"
data_git_msg = """\
commit ebb8ace4620efb27ddcce11b8a912d4779ac8f56
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Fri Jul 22 11:45:10 2022 -0700

    feat(rdc): ENV file and Reset Scenario
    
    This commit tweaks the script to read ENV file for additional
    constraints based on the recommended method from Real Intent.
    
    In addition to above, this commit adds a reset scenario template.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
