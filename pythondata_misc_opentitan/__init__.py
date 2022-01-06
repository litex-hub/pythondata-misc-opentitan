import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9360"
version_tuple = (0, 0, 9360)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9360")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9243"
data_version_tuple = (0, 0, 9243)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9243")
except ImportError:
    pass
data_git_hash = "b5eefa44470c62121d4556b349ef2709b7e69bce"
data_git_describe = "v0.0-9243-gb5eefa444"
data_git_msg = """\
commit b5eefa44470c62121d4556b349ef2709b7e69bce
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue Jan 4 06:09:24 2022 -0800

    [spi_host/dv] modified transactional behavior for more randomized behavior
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
