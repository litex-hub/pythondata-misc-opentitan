import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10847"
version_tuple = (0, 0, 10847)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10847")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10721"
data_version_tuple = (0, 0, 10721)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10721")
except ImportError:
    pass
data_git_hash = "951a93e8f41193439d0121cf89afc39da56a4e7e"
data_git_describe = "v0.0-10721-g951a93e8f"
data_git_msg = """\
commit 951a93e8f41193439d0121cf89afc39da56a4e7e
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue Mar 1 18:28:32 2022 +0000

    [sw, aes] Add unit test for AES status register
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
