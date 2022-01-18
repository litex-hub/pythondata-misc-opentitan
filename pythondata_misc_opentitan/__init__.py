import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9592"
version_tuple = (0, 0, 9592)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9592")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9470"
data_version_tuple = (0, 0, 9470)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9470")
except ImportError:
    pass
data_git_hash = "ce2da4b2b2c5964d37cc67fa75b4adeac67b088e"
data_git_describe = "v0.0-9470-gce2da4b2b"
data_git_msg = """\
commit ce2da4b2b2c5964d37cc67fa75b4adeac67b088e
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Jan 13 18:32:45 2022 -0800

    [all] various simple lint fixes
    
    - remove unused parameters in flash_ctrl
    - add mubi waivers
    - add reset waives and change parameters to unsigned
    - handle undriven / unloaded signals in socket when there is no error responder
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
