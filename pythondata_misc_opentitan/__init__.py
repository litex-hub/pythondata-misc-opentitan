import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14374"
version_tuple = (0, 0, 14374)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14374")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14232"
data_version_tuple = (0, 0, 14232)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14232")
except ImportError:
    pass
data_git_hash = "0a3ba57c724eb7e842f74fd3bd8595939a02c432"
data_git_describe = "v0.0-14232-g0a3ba57c72"
data_git_msg = """\
commit 0a3ba57c724eb7e842f74fd3bd8595939a02c432
Author: Douglas Reis <doreis@lowrisc.org>
Date:   Tue Sep 20 10:59:43 2022 +0100

    [silicon_creator] Refactor the epmp lib
    
     This commit refactors the epmp lib to use the epmp_state global
     from the static_critical section rather than receiving the object.
    
    Signed-off-by: Douglas Reis <doreis@lowrisc.org>

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
