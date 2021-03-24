import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5550"
version_tuple = (0, 0, 5550)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5550")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5455"
data_version_tuple = (0, 0, 5455)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5455")
except ImportError:
    pass
data_git_hash = "a558aaa3f1924b72f47cb98196e3d0a6f2635a3f"
data_git_describe = "v0.0-5455-ga558aaa3f"
data_git_msg = """\
commit a558aaa3f1924b72f47cb98196e3d0a6f2635a3f
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Wed Mar 17 15:48:03 2021 +0000

    [test, systemtest] Add DIF AON smoketest to CI
    
    Signed-off-by: Silvestrs Timofejevs <silvestrst@lowrisc.org>

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
