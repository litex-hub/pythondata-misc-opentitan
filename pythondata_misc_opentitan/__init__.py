import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5340"
version_tuple = (0, 0, 5340)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5340")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5245"
data_version_tuple = (0, 0, 5245)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5245")
except ImportError:
    pass
data_git_hash = "13cdb23996c6548494b5b41069592798486e1767"
data_git_describe = "v0.0-5245-g13cdb2399"
data_git_msg = """\
commit 13cdb23996c6548494b5b41069592798486e1767
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Tue Mar 9 15:34:53 2021 +0000

    [topgen] Remove alert_module and interrupt_module from top_*.hjson
    
    These lists actually had code to populate them in topgen/merge.py's
    amend_alert function, but this didn't ever run because it already has
    a value. That value means that you need to remember to update it
    whenever you add a new instance of an IP block.
    
    The original motivation behind listing these explicitly was that the
    top-level might not want to wire up all the alerts / interrupts from
    the modules that it instantiates. We're not doing that at the moment
    and, if we start doing that again, it's probably cleaner to explicitly
    disable things rather than to have to add everything twice.
    
    With this patch, we fix the code in amend_interrupt and amend_alert to
    add everything. Now the only difference between that and the manual
    list is the exact ordering of the bits in the signal. Since we access
    these bits through auto-generated named constants anyway, we can
    dispense with the manual step entirely.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
