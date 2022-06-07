import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12540"
version_tuple = (0, 0, 12540)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12540")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12398"
data_version_tuple = (0, 0, 12398)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12398")
except ImportError:
    pass
data_git_hash = "9ec5d1d3de843378453344724813036f6c34afa2"
data_git_describe = "v0.0-12398-g9ec5d1d3d"
data_git_msg = """\
commit 9ec5d1d3de843378453344724813036f6c34afa2
Author: Alexander Williams <awill@google.com>
Date:   Fri May 27 14:40:55 2022 -0700

    [top] Change usbdev bus clock to usb clock
    
    For top_earlgrey, also move usbdev to xbar_main. This keeps the number
    of clock domain crossings down and should improve latency considerably.
    In a follow-up, much of usbdev's CDC for CSRs will be removed.
    
    Because nearly the entire IP is clocked by the 48 MHz USB clock and it
    is of a similar magnitude as the main clock, it's best to place the CDC
    in the crossbar instead of at individual register sites.
    
    Signed-off-by: Alexander Williams <awill@google.com>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
