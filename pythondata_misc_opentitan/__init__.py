import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8782"
version_tuple = (0, 0, 8782)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8782")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8670"
data_version_tuple = (0, 0, 8670)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8670")
except ImportError:
    pass
data_git_hash = "0913134fcc8b1759bbbb4af569f008e4b3c471d5"
data_git_describe = "v0.0-8670-g0913134fc"
data_git_msg = """\
commit 0913134fcc8b1759bbbb4af569f008e4b3c471d5
Author: Mark Branstad <mark.branstad@wdc.com>
Date:   Fri Nov 19 06:25:07 2021 -0800

    [entropy/rtl] added count pkg to fix lint errors
    
    The prim_count package needs to be added to the core file to fix lint errors.
    
    Signed-off-by: Mark Branstad <mark.branstad@wdc.com>

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
