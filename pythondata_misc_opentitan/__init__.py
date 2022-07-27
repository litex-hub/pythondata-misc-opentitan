import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13299"
version_tuple = (0, 0, 13299)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13299")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13157"
data_version_tuple = (0, 0, 13157)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13157")
except ImportError:
    pass
data_git_hash = "5ede35cd4d2b5af311cc747f156000da930232e2"
data_git_describe = "v0.0-13157-g5ede35cd4d"
data_git_msg = """\
commit 5ede35cd4d2b5af311cc747f156000da930232e2
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Jul 26 16:24:31 2022 -0700

    fix(entropy_src): Change port type to mubi4_t
    
    SHA3 absorbed signal is converted to mubi4_t. entropy_src uses SHA3
    internally.
    
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
