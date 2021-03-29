import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5615"
version_tuple = (0, 0, 5615)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5615")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5520"
data_version_tuple = (0, 0, 5520)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5520")
except ImportError:
    pass
data_git_hash = "d0111856d59cf53046fd2d372e0bbbd3bfb2d9bc"
data_git_describe = "v0.0-5520-gd0111856d"
data_git_msg = """\
commit d0111856d59cf53046fd2d372e0bbbd3bfb2d9bc
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Mar 29 14:02:26 2021 +0100

    [otbn] Move loop nesting into programmers guide
    
    The "Loop nesting" section in the OTBN documentation is targeting
    programmers. Move it from the "Processor state" section to the
    "Programmers guide" section.
    
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
