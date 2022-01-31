import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9921"
version_tuple = (0, 0, 9921)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9921")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9797"
data_version_tuple = (0, 0, 9797)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9797")
except ImportError:
    pass
data_git_hash = "8cb33a7b336adee07424238215157e0539833df4"
data_git_describe = "v0.0-9797-g8cb33a7b3"
data_git_msg = """\
commit 8cb33a7b336adee07424238215157e0539833df4
Author: David Pudner <davidpudner@protonmail.com>
Date:   Wed Jan 26 10:49:28 2022 +0000

    [hw/dv] Changed set_response_queue to be umbounded due to queue overflow issues in Questa
    
    As discussed in issue 9514 Questa was running into queue overflow issues when running uart_stress_all_with_rand_reset tests.
    This is due to the driver put happening earlier than the sequence item get. It was aggreed that the check could be changed to be umbounded. The test now passes.
    
    Signed-off-by: David Pudner <davidpudner@protonmail.com>

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
