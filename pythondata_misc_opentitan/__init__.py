import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10884"
version_tuple = (0, 0, 10884)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10884")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10758"
data_version_tuple = (0, 0, 10758)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10758")
except ImportError:
    pass
data_git_hash = "8d95e28682ff4d70f11d6b8b663969768daa7ff1"
data_git_describe = "v0.0-10758-g8d95e2868"
data_git_msg = """\
commit 8d95e28682ff4d70f11d6b8b663969768daa7ff1
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Thu Mar 10 13:36:16 2022 -0800

    [entropy_src, dv] Fix data integrity issue in entropy_src interrupt/error test
    
      - Fix the data integrity error when forcing esrng fifo write error in entropy_src interrupt/error test
      - Fix some health test bugs
      - Fixes #11144
    
    Signed-off-by: Muqing Liu <muqing.liu@wdc.com>

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
