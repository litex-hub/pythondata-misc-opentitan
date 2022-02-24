import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10514"
version_tuple = (0, 0, 10514)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10514")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10388"
data_version_tuple = (0, 0, 10388)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10388")
except ImportError:
    pass
data_git_hash = "3ca54ba03fd6fbddeefb7a8fc4df07c61f1a94b8"
data_git_describe = "v0.0-10388-g3ca54ba03"
data_git_msg = """\
commit 3ca54ba03fd6fbddeefb7a8fc4df07c61f1a94b8
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Wed Feb 23 10:20:19 2022 +0000

    [otbn,rtl] Lint Fix
    
    Changes dmem(imem)_key_sel_otp type to logic.
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
