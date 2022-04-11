import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11512"
version_tuple = (0, 0, 11512)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11512")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11386"
data_version_tuple = (0, 0, 11386)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11386")
except ImportError:
    pass
data_git_hash = "bee94fda2845061741afa6b85c448378e1be2b8f"
data_git_describe = "v0.0-11386-gbee94fda2"
data_git_msg = """\
commit bee94fda2845061741afa6b85c448378e1be2b8f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Apr 11 12:52:24 2022 +0100

    [rom_ctrl,rtl] Tighten up expression for counter_data_rdy
    
    This signal is used to tell the counter that it can increment on this
    cycle. Usually, that would be because we'd managed to pass a packet of
    data to KMAC (when state is ReadingLow).
    
    Once we've finished passing things to KMAC, we want to race through
    the last 8 words with no back pressure. This was implemented by the
    "state_q != ReadingLow" term. Unfortunately, an injected error on
    state_q when we're in the ReadingLow state caused us to spuriously
    increment the ROM index which, in turn, meant that the data we were
    presenting to KMAC changed.
    
    This isn't a big deal (the chip is already going to deadlock), but it
    causes an assertion failure. Rather than messing around with
    assertions, let's just tighten up the expression so that we control
    the "race ahead" behaviour more explicitly. ReadingHigh and KmacAhead
    are the two FSM states where we've finished passing data to KMAC but
    haven't yet finished reading the top of the ROM.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
