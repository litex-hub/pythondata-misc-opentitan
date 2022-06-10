import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12628"
version_tuple = (0, 0, 12628)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12628")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12486"
data_version_tuple = (0, 0, 12486)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12486")
except ImportError:
    pass
data_git_hash = "ec88d27257f8eae66ef51783310a39633d373687"
data_git_describe = "v0.0-12486-gec88d2725"
data_git_msg = """\
commit ec88d27257f8eae66ef51783310a39633d373687
Author: Luís Marques <luismarques@lowrisc.org>
Date:   Tue Apr 19 12:00:37 2022 +0200

    [sw] Fix function prototypes
    
    Several functions without parameters were declared as `foo()` instead of
    `foo(void)`. The former is considered a function without a prototype, not
    a function without parameters. Newer versions of Clang implement a
    stricter check of this condition, and the new warnings were breaking the
    build. Fix this by adding the missing `void` in several places.
    
    Signed-off-by: Luís Marques <luismarques@lowrisc.org>

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
