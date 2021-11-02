import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8569"
version_tuple = (0, 0, 8569)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8569")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8457"
data_version_tuple = (0, 0, 8457)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8457")
except ImportError:
    pass
data_git_hash = "3f2a1c1223d3ca969b726d0ca982e936c5a42e4b"
data_git_describe = "v0.0-8457-g3f2a1c122"
data_git_msg = """\
commit 3f2a1c1223d3ca969b726d0ca982e936c5a42e4b
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Oct 27 14:13:42 2021 -0700

    [clkmgr, pwrmgr] Add clock handshaking for usb
    
    Since usb clocks can be turned on/off outside of normal
    low power routines, it creates some corner cases depending
    on how it is used.
    
    This PR fixes [sw, dif pwrmgr smoketest] Deadlock when disabling USB clock in active power #6504 by handshaking usb oscillator disables.
    Specifically, before the usb oscillator can be disabled, it must
    first request downstream gating to assert. Only when this is done,
    can the usb oscillator be turned off. This ensures there is no
    low power entry / exit confusion.
    
    Note this is not the ideal fix, but this is done to minimize the amount of disruption
    on the overall design and eventually dv.
    
    Some changes in DV code are required by the clkmgr change.
    
    RTL changes by tjaychen, DV changes by matutem.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

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
