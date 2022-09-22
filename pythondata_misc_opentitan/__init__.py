import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14383"
version_tuple = (0, 0, 14383)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14383")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14241"
data_version_tuple = (0, 0, 14241)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14241")
except ImportError:
    pass
data_git_hash = "5377391e8930bd9dbda22372d292ef37603f5623"
data_git_describe = "v0.0-14241-g5377391e89"
data_git_msg = """\
commit 5377391e8930bd9dbda22372d292ef37603f5623
Author: Alphan Ulusoy <alphan@google.com>
Date:   Wed Sep 21 10:16:45 2022 -0400

    [test] Run additional functests with rom
    
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
