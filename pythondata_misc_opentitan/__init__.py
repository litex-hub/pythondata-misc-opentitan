import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5383"
version_tuple = (0, 0, 5383)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5383")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5288"
data_version_tuple = (0, 0, 5288)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5288")
except ImportError:
    pass
data_git_hash = "4fe07f960e57d0381005de430a896502c7fedb8e"
data_git_describe = "v0.0-5288-g4fe07f960"
data_git_msg = """\
commit 4fe07f960e57d0381005de430a896502c7fedb8e
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Mar 15 11:06:11 2021 +0000

    Display error message from topgen in topgen-fusesoc
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
