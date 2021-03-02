import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5204"
version_tuple = (0, 0, 5204)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5204")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5113"
data_version_tuple = (0, 0, 5113)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5113")
except ImportError:
    pass
data_git_hash = "03018e827c7c8b2f0ca591207c609301e7abd4b7"
data_git_describe = "v0.0-5113-g03018e827"
data_git_msg = """\
commit 03018e827c7c8b2f0ca591207c609301e7abd4b7
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Feb 26 15:11:12 2021 +0000

    [lint] Waivers for rv_core_ibex lint
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
