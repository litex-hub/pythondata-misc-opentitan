import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11426"
version_tuple = (0, 0, 11426)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11426")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11300"
data_version_tuple = (0, 0, 11300)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11300")
except ImportError:
    pass
data_git_hash = "8e486b17ac5821a80db6e0b7d624e0ffaa450b52"
data_git_describe = "v0.0-11300-g8e486b17a"
data_git_msg = """\
commit 8e486b17ac5821a80db6e0b7d624e0ffaa450b52
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Tue Apr 5 22:35:10 2022 +0200

    [aes] Add missing countermeasure labels to RTL
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
