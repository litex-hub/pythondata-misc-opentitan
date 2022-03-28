import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11159"
version_tuple = (0, 0, 11159)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11159")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11033"
data_version_tuple = (0, 0, 11033)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11033")
except ImportError:
    pass
data_git_hash = "9b35ca29afe50da312b9c18c9bda80ef9c8a79f2"
data_git_describe = "v0.0-11033-g9b35ca29a"
data_git_msg = """\
commit 9b35ca29afe50da312b9c18c9bda80ef9c8a79f2
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Fri Mar 25 16:37:31 2022 -0700

    [csrng, dv] Fix a bug for csrng intr/err test
    
      - Fix a path reference issue in csrng intr/err test
    
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
