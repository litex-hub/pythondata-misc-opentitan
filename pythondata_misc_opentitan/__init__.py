import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10286"
version_tuple = (0, 0, 10286)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10286")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10160"
data_version_tuple = (0, 0, 10160)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10160")
except ImportError:
    pass
data_git_hash = "b50baf99ef5921a3b135cc70f7e1f8094fee80b0"
data_git_describe = "v0.0-10160-gb50baf99e"
data_git_msg = """\
commit b50baf99ef5921a3b135cc70f7e1f8094fee80b0
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Fri Feb 11 02:51:51 2022 -0800

    [aes/dv] added idle assert check
    
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
