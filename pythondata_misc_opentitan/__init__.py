import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9358"
version_tuple = (0, 0, 9358)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9358")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9241"
data_version_tuple = (0, 0, 9241)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9241")
except ImportError:
    pass
data_git_hash = "02337e0ce70da9f42ec23401505a3f63fc4a432b"
data_git_describe = "v0.0-9241-g02337e0ce"
data_git_msg = """\
commit 02337e0ce70da9f42ec23401505a3f63fc4a432b
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Wed Jan 5 14:44:44 2022 -0800

    [csrng/dv] Modify for efuse, certain enables off
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
