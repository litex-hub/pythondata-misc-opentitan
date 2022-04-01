import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11287"
version_tuple = (0, 0, 11287)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11287")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11161"
data_version_tuple = (0, 0, 11161)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11161")
except ImportError:
    pass
data_git_hash = "1d750d8dc3af404939b58a565272e44a82d79ab7"
data_git_describe = "v0.0-11161-g1d750d8dc"
data_git_msg = """\
commit 1d750d8dc3af404939b58a565272e44a82d79ab7
Author: Timothy Trippel <ttrippel@google.com>
Date:   Fri Apr 1 12:09:08 2022 -0700

    [bazel] use depset instead of custom `_unique_deps()` function
    
    In order to merge OTTF deps with user-provided deps in
    opentitan_functests, a custom helper method was created to remove
    duplicate deps. However, it seems the `.to_list()` method of `depsets`
    can be used in place of this. This further simplifies this code.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
