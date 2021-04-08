import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5777"
version_tuple = (0, 0, 5777)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5777")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5682"
data_version_tuple = (0, 0, 5682)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5682")
except ImportError:
    pass
data_git_hash = "bf57a5c1e1f8a87a3bc8ba57a50c08c650c72479"
data_git_describe = "v0.0-5682-gbf57a5c1e"
data_git_msg = """\
commit bf57a5c1e1f8a87a3bc8ba57a50c08c650c72479
Author: Udi Jonnalagadda <udij@google.com>
Date:   Fri Mar 19 01:15:24 2021 -0700

    [dv/kmac] add cycle accurate model in scoreboard
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
