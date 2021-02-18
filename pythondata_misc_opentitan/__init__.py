import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5043"
version_tuple = (0, 0, 5043)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5043")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post4952"
data_version_tuple = (0, 0, 4952)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post4952")
except ImportError:
    pass
data_git_hash = "f4e8f95fee05259c3beeb6f815606945edb66479"
data_git_describe = "v0.0-4952-gf4e8f95fe"
data_git_msg = """\
commit f4e8f95fee05259c3beeb6f815606945edb66479
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Tue Feb 9 08:06:40 2021 -0800

    [csrng/dv] V0->V1
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
