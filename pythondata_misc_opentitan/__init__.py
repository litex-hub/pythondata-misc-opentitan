import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5711"
version_tuple = (0, 0, 5711)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5711")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5616"
data_version_tuple = (0, 0, 5616)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5616")
except ImportError:
    pass
data_git_hash = "f29a0f7a7115e03fba734b1c00691c253aceb07e"
data_git_describe = "v0.0-5616-gf29a0f7a7"
data_git_msg = """\
commit f29a0f7a7115e03fba734b1c00691c253aceb07e
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 30 12:36:44 2021 +0100

    [dv] Allow monitor items to have different types from sequence items
    
    This was broken by 47c9510. This isn't the cleanest fix, because the
    monitor class is still parameterised by types that it has no business
    knowing about.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
