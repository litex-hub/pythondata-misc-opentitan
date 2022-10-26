import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14967"
version_tuple = (0, 0, 14967)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14967")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14825"
data_version_tuple = (0, 0, 14825)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14825")
except ImportError:
    pass
data_git_hash = "f929c4ea71d04020b11c71d46b2d21b22ca9b6f2"
data_git_describe = "v0.0-14825-gf929c4ea71"
data_git_msg = """\
commit f929c4ea71d04020b11c71d46b2d21b22ca9b6f2
Author: Weicai Yang <weicai@google.com>
Date:   Tue Oct 25 22:41:08 2022 -0700

    [spi_device/dv] Disable overflow/underflow SVAs
    
    It's fine to have these SVA, but disable them when the test verifies
    underflow/overflow.
    
    Signed-off-by: Weicai Yang <weicai@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
