import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5854"
version_tuple = (0, 0, 5854)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5854")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5759"
data_version_tuple = (0, 0, 5759)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5759")
except ImportError:
    pass
data_git_hash = "22c185623d66436e3ffa3da9da33235f6d3d9fb3"
data_git_describe = "v0.0-5759-g22c185623"
data_git_msg = """\
commit 22c185623d66436e3ffa3da9da33235f6d3d9fb3
Author: Timothy Chen <timothytim@google.com>
Date:   Fri Apr 9 14:52:12 2021 -0700

    [usb / top] Hook-up usb rx enable
    
    - Currently the rx enable is assumed to be dynamic, but this may
      change based on Nuvoton feedback.
    
    There was a discussion regarding whether we should make most of the usbdev inter-signals instead of pinmux signals.
    See below for rationale.
    
    In addition to dp/dn, sense and dp/dn_pullup_en all have to remain pinmux-able signals.
    Sense may need to come through pinmux since it is used to detect vbus power.  As long as the vbus voltage is not too high (or is clamped to a safe range), it can be muxed on nay pin.
    dp/dn_pullup_en make use of pinmux's sleep capture as part of usbdev's suspend / resume feature.
    
    This ends up leaving a few scattered signals that may or may not fall into the pinmux category.
    Ultimateily, it is difficult from the perspective of the usbdev to know whether a signal should be pinmuxed or directly signaled out.
    
    The ideal solution are two-fold
    
    1. Make all signals inter-signal, and use a top specific wrapper that connects the necessary signals to pinmux.
    2. Make all signals pinmuxable, and manually handle the pad connections where required.
    
    In our design, we currently have most of the support needed for 2, (see #6042) for possible enhancements
    
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
