import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9350"
version_tuple = (0, 0, 9350)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9350")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9233"
data_version_tuple = (0, 0, 9233)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9233")
except ImportError:
    pass
data_git_hash = "f508d2d9b15bd147cb444749c0b7fea0756ea252"
data_git_describe = "v0.0-9233-gf508d2d9b"
data_git_msg = """\
commit f508d2d9b15bd147cb444749c0b7fea0756ea252
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Thu Dec 30 12:04:47 2021 -0800

    [csrng/dv] Updated testplan, Create/debug stress_all_vseq/test
    
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
