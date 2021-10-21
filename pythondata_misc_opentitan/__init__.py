import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8386"
version_tuple = (0, 0, 8386)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8386")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8274"
data_version_tuple = (0, 0, 8274)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8274")
except ImportError:
    pass
data_git_hash = "464b736079ba91c6fe52cef12f2772ce576c1302"
data_git_describe = "v0.0-8274-g464b73607"
data_git_msg = """\
commit 464b736079ba91c6fe52cef12f2772ce576c1302
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Wed Oct 20 17:10:23 2021 +0100

    [otbn,dv] Maybe use IRQ to detect end instead of polling STATUS
    
    Configuring this goes in two steps: firstly, you have to write to the
    enable register. There's an enable_interrupts_pct knob that sequences
    that care can get from the environment config to spot that it is
    needed.
    
    Then the run_otbn() task in the base class chooses whether to use
    interrupts or polling, based on whether interrupts are enabled (if
    not, it will poll!) and poll_despite_interrupts_pct.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
