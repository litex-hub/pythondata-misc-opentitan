import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8697"
version_tuple = (0, 0, 8697)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8697")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8585"
data_version_tuple = (0, 0, 8585)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8585")
except ImportError:
    pass
data_git_hash = "40e87bc3ca98090b9bafd87968995ff414de77f7"
data_git_describe = "v0.0-8585-g40e87bc3c"
data_git_msg = """\
commit 40e87bc3ca98090b9bafd87968995ff414de77f7
Author: Canberk Topal <ctopal@lowrisc.org>
Date:   Mon Oct 25 13:07:00 2021 +0100

    [dv] Support Multiple EDN Interfaces in OpenTitan
    
    This commit includes changes in CIP to support multiple EDN IFs with
    setting NUM_EDN parameter in *env_pkg.sv and num_edn in *env_cfg.sv
    Also includes changes in:
    - OTBN testbench to allow connecting two EDN interfaces
    - In order to support EDN IF changes, DV enviroments of:
      - AES, Key Manager, KMAC, OTP Controller, Alert Handler
    
    Signed-off-by: Canberk Topal <ctopal@lowrisc.org>

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
