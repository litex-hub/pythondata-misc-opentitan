import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5782"
version_tuple = (0, 0, 5782)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5782")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5687"
data_version_tuple = (0, 0, 5687)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5687")
except ImportError:
    pass
data_git_hash = "57be47e8aba1edb9d40c1d8f1fe725ce80506d9d"
data_git_describe = "v0.0-5687-g57be47e8a"
data_git_msg = """\
commit 57be47e8aba1edb9d40c1d8f1fe725ce80506d9d
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Thu Apr 8 10:08:35 2021 -0700

    [kmac] Fix typo in kmac.waiver
    
    while renaming kmac_keymgr.sv to kmac_app.sv, kmac.waiver was left
    behind having its original name in the waiver rule. This commit
    corrected it and slightly revised the priority condition too.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
