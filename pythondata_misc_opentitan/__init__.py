import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10976"
version_tuple = (0, 0, 10976)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10976")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10850"
data_version_tuple = (0, 0, 10850)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10850")
except ImportError:
    pass
data_git_hash = "8692367c88ef7502025fb3b6d032fb6546dac3a2"
data_git_describe = "v0.0-10850-g8692367c8"
data_git_msg = """\
commit 8692367c88ef7502025fb3b6d032fb6546dac3a2
Author: Muqing Liu <muqing.liu@wdc.com>
Date:   Wed Dec 15 20:28:05 2021 -0800

    [csrng, dv] Test CSRNG interrupts, alerts and errors
    
      - Add vseqs for CSRNG interrupt, alert and error tests
      - Update the related config files to include the interrupt, alert and error tests
      - Add a virtual assert interface to turn off assertions with long paths
      - Move the path references in the test vseqs to a separate path interface
    
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
