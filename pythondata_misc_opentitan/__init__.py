import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5743"
version_tuple = (0, 0, 5743)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5743")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5648"
data_version_tuple = (0, 0, 5648)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5648")
except ImportError:
    pass
data_git_hash = "3590a1d81431713d283937ff3fe3267b69af844b"
data_git_describe = "v0.0-5648-g3590a1d81"
data_git_msg = """\
commit 3590a1d81431713d283937ff3fe3267b69af844b
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Apr 6 17:46:48 2021 +0100

    [ci] Switch from a blacklist to a whitelist for executable files
    
    And remove executable bits from everything that's not allowed.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
