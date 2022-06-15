import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12705"
version_tuple = (0, 0, 12705)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12705")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12563"
data_version_tuple = (0, 0, 12563)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12563")
except ImportError:
    pass
data_git_hash = "f15b409b7cb1fbddb818ed4074437c2265e0c3ed"
data_git_describe = "v0.0-12563-gf15b409b7"
data_git_msg = """\
commit f15b409b7cb1fbddb818ed4074437c2265e0c3ed
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Jun 15 10:15:20 2022 -0400

    [opentitantool] resolve a warning by avoiding unused dependence on "bail"
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
