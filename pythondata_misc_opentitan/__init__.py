import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10566"
version_tuple = (0, 0, 10566)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10566")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10440"
data_version_tuple = (0, 0, 10440)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10440")
except ImportError:
    pass
data_git_hash = "f23cfa98e3931f4e939c9ab19bb371e8b4f53ff3"
data_git_describe = "v0.0-10440-gf23cfa98e"
data_git_msg = """\
commit f23cfa98e3931f4e939c9ab19bb371e8b4f53ff3
Author: Eunchan Kim <eunchan@opentitan.org>
Date:   Fri Feb 25 11:40:06 2022 -0800

    [kmac] Add config knob to CFG_SHADOWED
    
    This commit adds `en_unsupported_modestrength` config knob to
    CFG_SHADOWED CSR and connect to the signal in the top-level.
    
    Signed-off-by: Eunchan Kim <eunchan@opentitan.org>

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
