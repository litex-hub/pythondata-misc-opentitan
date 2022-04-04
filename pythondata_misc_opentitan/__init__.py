import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11325"
version_tuple = (0, 0, 11325)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11325")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11199"
data_version_tuple = (0, 0, 11199)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11199")
except ImportError:
    pass
data_git_hash = "f25c8cb2de214a7bc88879f6baf7f9c5053f5cd9"
data_git_describe = "v0.0-11199-gf25c8cb2d"
data_git_msg = """\
commit f25c8cb2de214a7bc88879f6baf7f9c5053f5cd9
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue Mar 15 05:30:19 2022 -0700

    [aes/dv] added exclusion files for common and UNR for nomasking DUT
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
