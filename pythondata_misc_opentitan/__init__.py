import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8314"
version_tuple = (0, 0, 8314)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8314")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8202"
data_version_tuple = (0, 0, 8202)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8202")
except ImportError:
    pass
data_git_hash = "e7d413442ad91ad81d631a2b30eb74a2935c7abe"
data_git_describe = "v0.0-8202-ge7d413442"
data_git_msg = """\
commit e7d413442ad91ad81d631a2b30eb74a2935c7abe
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Oct 18 12:19:52 2021 +0100

    [ci] Increase timeout for Verilator test
    
    We have regularly been getting timeouts in the "Execute tests
    on the Verilated system (excl. slow tests)" test recently. Increase the
    timeout from 1 to 2 hours.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
