import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14759"
version_tuple = (0, 0, 14759)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14759")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14617"
data_version_tuple = (0, 0, 14617)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14617")
except ImportError:
    pass
data_git_hash = "fccf1bb4863c0af197db5ce8b4418f2e03f8687e"
data_git_describe = "v0.0-14617-gfccf1bb486"
data_git_msg = """\
commit fccf1bb4863c0af197db5ce8b4418f2e03f8687e
Author: Weicai Yang <weicai@google.com>
Date:   Thu Oct 13 23:43:56 2022 -0700

    [spi_device/dv] Update DV doc
    
    1. Update the diagram
    2. Update spi_agent section and the fcov section
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
