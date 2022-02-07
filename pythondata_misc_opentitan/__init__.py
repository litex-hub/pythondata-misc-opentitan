import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10097"
version_tuple = (0, 0, 10097)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10097")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9973"
data_version_tuple = (0, 0, 9973)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9973")
except ImportError:
    pass
data_git_hash = "9ac60548b86f3e5aad1fd4fdc753a79504599aee"
data_git_describe = "v0.0-9973-g9ac60548b"
data_git_msg = """\
commit 9ac60548b86f3e5aad1fd4fdc753a79504599aee
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jan 10 15:40:48 2022 +0100

    [aes] Add list of countermeasures for D2S sign-off
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
