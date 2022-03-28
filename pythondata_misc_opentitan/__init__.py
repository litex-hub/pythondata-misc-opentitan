import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11154"
version_tuple = (0, 0, 11154)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11154")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11028"
data_version_tuple = (0, 0, 11028)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11028")
except ImportError:
    pass
data_git_hash = "f95053d98ae63cc11627b9526ef96775ff18979a"
data_git_describe = "v0.0-11028-gf95053d98"
data_git_msg = """\
commit f95053d98ae63cc11627b9526ef96775ff18979a
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Fri Mar 25 17:14:19 2022 -0700

    [edn, dv] Fix a bug for edn intr/err test
    
      - Fix a path reference issue in edn intr/err test
    
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
