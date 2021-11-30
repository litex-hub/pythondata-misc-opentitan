import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8911"
version_tuple = (0, 0, 8911)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8911")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8799"
data_version_tuple = (0, 0, 8799)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8799")
except ImportError:
    pass
data_git_hash = "a847073fb8c333cbf1c240d25794517f1562c0af"
data_git_describe = "v0.0-8799-ga847073fb"
data_git_msg = """\
commit a847073fb8c333cbf1c240d25794517f1562c0af
Author: Timothy Trippel <ttrippel@google.com>
Date:   Mon Nov 22 19:42:42 2021 +0000

    [sw/ottf] Decouple OTTF ISRs into separate lib.
    
    Previously, all default ISRs were contained in the single OTTF build
    target. This made using the default OTTF ISRs in a standalone bare metal
    test application that does not make use of the OTTF impossible.
    
    This commit isolates the OTTF default ISRs into a separate library, so
    they can be used similar to the existing `sw/device/lib/handler.<c,h>`
    ISRs, since those will be deprecated in the near future when all
    chip-level tests migrate to the OTTF.
    
    Signed-off-by: Timothy Trippel <ttrippel@google.com>

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
