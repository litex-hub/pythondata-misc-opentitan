import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10230"
version_tuple = (0, 0, 10230)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10230")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10106"
data_version_tuple = (0, 0, 10106)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10106")
except ImportError:
    pass
data_git_hash = "08d3b8b5fec118437aab51a69d9189b9b6cea79e"
data_git_describe = "v0.0-10106-g08d3b8b5f"
data_git_msg = """\
commit 08d3b8b5fec118437aab51a69d9189b9b6cea79e
Author: Cindy Chen <chencindy@opentitan.org>
Date:   Wed Feb 9 18:24:41 2022 -0800

    [dv/aes] ctrl_shadowed register update
    
    This PR updates shadow reg in AES:
    1). There are more than one shadow reg in AES, need to gate the
      customized write to only apply to `ctrl_shadowed``
    2). Ctrl_shadowed register has some field update, this PR aligns it in
      DV.
    
    Signed-off-by: Cindy Chen <chencindy@opentitan.org>

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
