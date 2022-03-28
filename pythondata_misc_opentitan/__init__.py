import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11162"
version_tuple = (0, 0, 11162)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11162")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11036"
data_version_tuple = (0, 0, 11036)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11036")
except ImportError:
    pass
data_git_hash = "ce0b9241b4bf70ee407e5cd5385d246140b5ae10"
data_git_describe = "v0.0-11036-gce0b9241b"
data_git_msg = """\
commit ce0b9241b4bf70ee407e5cd5385d246140b5ae10
Author: Jaedon Kim <jdonjdon@google.com>
Date:   Fri Mar 25 19:43:18 2022 +0000

    [dv,clkmgr] sec cm testplan
    
    Signed-off-by: Jaedon Kim <jdonjdon@google.com>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
