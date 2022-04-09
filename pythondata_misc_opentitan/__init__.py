import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11499"
version_tuple = (0, 0, 11499)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11499")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11373"
data_version_tuple = (0, 0, 11373)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11373")
except ImportError:
    pass
data_git_hash = "8d83613c4cd516e0e619384984d0d62072ebadf8"
data_git_describe = "v0.0-11373-g8d83613c4"
data_git_msg = """\
commit 8d83613c4cd516e0e619384984d0d62072ebadf8
Author: Martin Lueker-Boden <martin.lueker-boden@wdc.com>
Date:   Fri Apr 8 12:59:04 2022 -0700

    [entropy_src/rtl] Suppress re-assertion of interrupts
    
    The entropy_data and observe FIFOs are cleared with the entropy_src
    is disabled, but any interrupts saying they have data must be
    cleared by FW.
    
    As noted in issue #11951, there is also a delay between when the
    IP is disabled and the FIFO is cleared.  This means that
    even when FIFO interrupts are cleared after disabling, the interrupt
    can reassert itself in this brief delay period.
    
    This PR therefore suppresses these interrupt events from
    retriggering when the IP is disabled.
    
    Signed-off-by: Martin Lueker-Boden <martin.lueker-boden@wdc.com>

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
