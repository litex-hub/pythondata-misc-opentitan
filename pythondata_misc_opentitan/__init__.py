import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12246"
version_tuple = (0, 0, 12246)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12246")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12118"
data_version_tuple = (0, 0, 12118)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12118")
except ImportError:
    pass
data_git_hash = "eb25b5bb4f583a0dcba970539cbfc0799413e8de"
data_git_describe = "v0.0-12118-geb25b5bb4"
data_git_msg = """\
commit eb25b5bb4f583a0dcba970539cbfc0799413e8de
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue May 17 14:59:48 2022 +0100

    [dif, hmac] Add unittest for `...mode_hmac_start` function
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post128"
tool_version_tuple = (0, 0, 128)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post128")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
