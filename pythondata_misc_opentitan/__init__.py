import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10923"
version_tuple = (0, 0, 10923)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10923")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10797"
data_version_tuple = (0, 0, 10797)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10797")
except ImportError:
    pass
data_git_hash = "6ee413aab2a7d3f59fcb1c7bdd62f14cf8b14ade"
data_git_describe = "v0.0-10797-g6ee413aab"
data_git_msg = """\
commit 6ee413aab2a7d3f59fcb1c7bdd62f14cf8b14ade
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Wed Mar 16 08:31:23 2022 +0000

    [opentitan] Remove Silvestrs from committers
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
