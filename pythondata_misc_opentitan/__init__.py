import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5666"
version_tuple = (0, 0, 5666)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5666")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5571"
data_version_tuple = (0, 0, 5571)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5571")
except ImportError:
    pass
data_git_hash = "2799bf0de69b3d7878375a51901fba96aeadac45"
data_git_describe = "v0.0-5571-g2799bf0de"
data_git_msg = """\
commit 2799bf0de69b3d7878375a51901fba96aeadac45
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 18 14:48:47 2021 -0700

    [tlul] Add support for data integrity passthrough
    
    - Top level/otbn rams are now fully connected without dropping or pading bits
    - The integrity is fully passed through, however, integrity recalculation on byte writes for top level memories will be done in a separate PR.
    - ROM handling will also be separately done as it needs to be padded out to byte alignment
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
