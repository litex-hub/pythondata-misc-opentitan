import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5785"
version_tuple = (0, 0, 5785)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5785")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5690"
data_version_tuple = (0, 0, 5690)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5690")
except ImportError:
    pass
data_git_hash = "e7caaa137d2dc3a5479bb1bebe37f4e62c409f36"
data_git_describe = "v0.0-5690-ge7caaa137"
data_git_msg = """\
commit e7caaa137d2dc3a5479bb1bebe37f4e62c409f36
Author: Silvestrs Timofejevs <silvestrst@lowrisc.org>
Date:   Thu Apr 8 16:22:09 2021 +0100

    [sw, rom_ext_signer] Run the workspace through with `cargo fmt`
    
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
