import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9459"
version_tuple = (0, 0, 9459)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9459")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9341"
data_version_tuple = (0, 0, 9341)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9341")
except ImportError:
    pass
data_git_hash = "ee1634b6b26f59b40e35e5c6e310c783b267db5e"
data_git_describe = "v0.0-9341-gee1634b6b"
data_git_msg = """\
commit ee1634b6b26f59b40e35e5c6e310c783b267db5e
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue Jan 11 12:46:02 2022 -0800

    [spi_host/dv] added spi_host to nightly regression
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
