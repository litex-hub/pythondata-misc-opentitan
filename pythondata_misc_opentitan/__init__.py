import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10407"
version_tuple = (0, 0, 10407)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10407")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10281"
data_version_tuple = (0, 0, 10281)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10281")
except ImportError:
    pass
data_git_hash = "3fc70360b5e814b3ce183bfff653cfe0e03b3675"
data_git_describe = "v0.0-10281-g3fc70360b"
data_git_msg = """\
commit 3fc70360b5e814b3ce183bfff653cfe0e03b3675
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Wed Feb 16 12:41:59 2022 +0000

    [dv] Add rv_core_ibex chip level tests to testplan
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
