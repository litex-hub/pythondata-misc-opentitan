import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10484"
version_tuple = (0, 0, 10484)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10484")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10358"
data_version_tuple = (0, 0, 10358)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10358")
except ImportError:
    pass
data_git_hash = "b5ecf74d27e1fce04e16d739897d18be7acb6236"
data_git_describe = "v0.0-10358-gb5ecf74d2"
data_git_msg = """\
commit b5ecf74d27e1fce04e16d739897d18be7acb6236
Author: Rasmus Madsen <rasmus.madsen@wdc.com>
Date:   Tue Feb 22 12:23:51 2022 -0800

    [tools/xcelium] updated common coverage exclusions to exclude single bit correctly
    
    Signed-off-by: Rasmus Madsen <rasmus.madsen@wdc.com>

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
