import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5387"
version_tuple = (0, 0, 5387)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5387")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5292"
data_version_tuple = (0, 0, 5292)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5292")
except ImportError:
    pass
data_git_hash = "b08d79a9873f730e5d66b5f87ccc40457dc744aa"
data_git_describe = "v0.0-5292-gb08d79a98"
data_git_msg = """\
commit b08d79a9873f730e5d66b5f87ccc40457dc744aa
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Thu Mar 11 14:04:50 2021 -0800

    [edn/dv] dv doc, testplan, checklist, regression, csrng_agent mod, whitespace removed
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

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
