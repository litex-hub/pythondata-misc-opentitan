import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9722"
version_tuple = (0, 0, 9722)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9722")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9600"
data_version_tuple = (0, 0, 9600)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9600")
except ImportError:
    pass
data_git_hash = "bf53287bfa8828af45b1caa38a98047af2107cd4"
data_git_describe = "v0.0-9600-gbf53287bf"
data_git_msg = """\
commit bf53287bfa8828af45b1caa38a98047af2107cd4
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Mon Jan 24 10:47:34 2022 +0100

    [aes] Fix wrapper for FI experiments
    
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
