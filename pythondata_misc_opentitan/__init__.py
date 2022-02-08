import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10150"
version_tuple = (0, 0, 10150)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10150")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10026"
data_version_tuple = (0, 0, 10026)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10026")
except ImportError:
    pass
data_git_hash = "5a990dd81fb8b33c21232c9621da7274ff5b643b"
data_git_describe = "v0.0-10026-g5a990dd81"
data_git_msg = """\
commit 5a990dd81fb8b33c21232c9621da7274ff5b643b
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Mon Jan 31 06:47:51 2022 -0800

    [aes/dv] updated dv to handle new reseeding feature
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
