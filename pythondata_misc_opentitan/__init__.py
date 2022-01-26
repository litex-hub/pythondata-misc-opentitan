import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9807"
version_tuple = (0, 0, 9807)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9807")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9685"
data_version_tuple = (0, 0, 9685)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9685")
except ImportError:
    pass
data_git_hash = "09a20560bfe4048727bcbbd006298f21d9177630"
data_git_describe = "v0.0-9685-g09a20560b"
data_git_msg = """\
commit 09a20560bfe4048727bcbbd006298f21d9177630
Author: Steve Nelson <steve.nelson@wdc.com>
Date:   Fri Jan 7 04:58:19 2022 -0800

    [entropy_src/edn/dv] Create stress_all vseqs/tests
    
    Signed-off-by: Steve Nelson <steve.nelson@wdc.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
