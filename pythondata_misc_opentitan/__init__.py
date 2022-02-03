import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10061"
version_tuple = (0, 0, 10061)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10061")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9937"
data_version_tuple = (0, 0, 9937)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9937")
except ImportError:
    pass
data_git_hash = "00a2a30c6cb4d292b1364d86433e050427cf6f22"
data_git_describe = "v0.0-9937-g00a2a30c6"
data_git_msg = """\
commit 00a2a30c6cb4d292b1364d86433e050427cf6f22
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Tue Feb 1 09:49:56 2022 -0800

    [kmac] Fix Fatal Alert connection
    
    @m-temp reported incorrect connection for the fatal alert in #10516.
    The alert_sender modules are instantiated in opposit way.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
