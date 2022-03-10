import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10833"
version_tuple = (0, 0, 10833)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10833")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10707"
data_version_tuple = (0, 0, 10707)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10707")
except ImportError:
    pass
data_git_hash = "57cc44f6f5d166a2b4d9079811d6c1aca4675252"
data_git_describe = "v0.0-10707-g57cc44f6f"
data_git_msg = """\
commit 57cc44f6f5d166a2b4d9079811d6c1aca4675252
Author: Alexander Williams <awill@google.com>
Date:   Wed Feb 23 09:04:33 2022 -0800

    [usbdev] Move pinflip and dp_o/dn_o to usb_fs_nb_pe
    
    Handle the interface changes and alternate TX interface in logic, before
    the final register. Prior to this change, the pinflip was sometimes
    handled in clock muxes, on the I/O side of the first/final registers,
    and the dp_o/dn_o interface was only done in behavioral logic. Move this
    all inside the USB clock domain, and perform only the pin overrides with
    clock muxes.
    
    Add override for rx_enable and remove the redundant one for
    tx_use_d_se0.
    
    Signed-off-by: Alexander Williams <awill@google.com>

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
