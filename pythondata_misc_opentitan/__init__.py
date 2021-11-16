import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8732"
version_tuple = (0, 0, 8732)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8732")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8620"
data_version_tuple = (0, 0, 8620)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8620")
except ImportError:
    pass
data_git_hash = "393e28e41487fa9896e6f366a632229a5a1568da"
data_git_describe = "v0.0-8620-g393e28e41"
data_git_msg = """\
commit 393e28e41487fa9896e6f366a632229a5a1568da
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Nov 16 16:24:40 2021 +0000

    [ci] Simplify check-generated.sh; allow it to catch multiple errors
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
