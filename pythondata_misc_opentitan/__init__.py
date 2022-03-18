import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10983"
version_tuple = (0, 0, 10983)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10983")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10857"
data_version_tuple = (0, 0, 10857)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10857")
except ImportError:
    pass
data_git_hash = "5abad2426ef3579f59532be7a0734507d60edd96"
data_git_describe = "v0.0-10857-g5abad2426"
data_git_msg = """\
commit 5abad2426ef3579f59532be7a0734507d60edd96
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Thu Dec 30 15:52:27 2021 -0800

    [edn, dv] Test EDN interrupts, alerts and errors
    
      - Add vseqs for EDN interrupt, alert and error tests
      - Update related config files to include the interrupt, alert and error tests
      - Add a virtual assert interface to turn off assertions that have long paths
      - Add a virtual path interface to remove the full path reference in the test sequences
    
    Signed-off-by: Muqing Liu <muqing.liu@wdc.com>

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
