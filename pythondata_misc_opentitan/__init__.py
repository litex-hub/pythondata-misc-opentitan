import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11078"
version_tuple = (0, 0, 11078)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11078")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10952"
data_version_tuple = (0, 0, 10952)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10952")
except ImportError:
    pass
data_git_hash = "3cb095466f4e404ad585364887878654d2ebc6db"
data_git_describe = "v0.0-10952-g3cb095466"
data_git_msg = """\
commit 3cb095466f4e404ad585364887878654d2ebc6db
Author: David Pudner <davidpudner@protonmail.com>
Date:   Fri Feb 11 15:04:51 2022 +0000

    [hw/dv] Removed colon from Questa build and run fail patterns.
    
    It was found that not all error messages output in the Questa log output contained a colon following the Error keyword.
    This meant some error messages were missed.
    
    Signed-off-by: David Pudner <davidpudner@protonmail.com>

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
