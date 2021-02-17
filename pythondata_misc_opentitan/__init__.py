import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5030"
version_tuple = (0, 0, 5030)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5030")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4939"
data_version_tuple = (0, 0, 4939)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4939")
except ImportError:
    pass
data_git_hash = "b7248ba84ecafbc3cdd2feb824b68dda767fa232"
data_git_describe = "v0.0-4939-gb7248ba84"
data_git_msg = """\
commit b7248ba84ecafbc3cdd2feb824b68dda767fa232
Author: Igor Kouznetsov <igor.kouznetsov@wdc.com>
Date:   Wed Feb 10 15:53:15 2021 -0800

    [i2c, rtl] Lint errors due to full_o
    
    Fixed lint errors cause by full_o output wiring of prim_fifo_sync
    
    Signed-off-by: Igor Kouznetsov <igor.kouznetsov@wdc.com>

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
