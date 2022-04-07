import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11425"
version_tuple = (0, 0, 11425)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11425")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11299"
data_version_tuple = (0, 0, 11299)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11299")
except ImportError:
    pass
data_git_hash = "c67e7fe129c145a65b6506dc962e5abdc11bdb7e"
data_git_describe = "v0.0-11299-gc67e7fe12"
data_git_msg = """\
commit c67e7fe129c145a65b6506dc962e5abdc11bdb7e
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Thu Mar 17 18:12:38 2022 +0000

    [prim] Add prim_blanker
    
    This wraps prim_and2 for use in blanking. prim_blanker provides a neater
    interface and a clear statement of intent for what it's being used for.
    
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
