import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9825"
version_tuple = (0, 0, 9825)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9825")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9703"
data_version_tuple = (0, 0, 9703)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9703")
except ImportError:
    pass
data_git_hash = "06d3a28fd6c98a721dc9766268950049a50f67ed"
data_git_describe = "v0.0-9703-g06d3a28fd"
data_git_msg = """\
commit 06d3a28fd6c98a721dc9766268950049a50f67ed
Author: Dave Williams <dave.williams@ensilica.com>
Date:   Thu Jan 20 17:45:46 2022 +0000

    [sw,tests] SRAM execution test DV integration
    
    Checks whether code can be executed from the SRAM depending on the values
    of LC_STATE, OTP HW_CFG[IFETCH] and SRAM_CTRL EXEC CSR.
    
    Signed-off-by: Dave Williams <dave.williams@ensilica.com>

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
