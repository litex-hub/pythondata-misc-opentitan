import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11233"
version_tuple = (0, 0, 11233)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11233")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11107"
data_version_tuple = (0, 0, 11107)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11107")
except ImportError:
    pass
data_git_hash = "75885e656149d5a4a49f91d2977acb3a4ffe1b2f"
data_git_describe = "v0.0-11107-g75885e656"
data_git_msg = """\
commit 75885e656149d5a4a49f91d2977acb3a4ffe1b2f
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Mar 7 14:54:45 2022 +0000

    [otbn,rtl] Rewire how we pass around error bits
    
    Before this change, we passed lots of signals up to
    top-level, where they were assembled into an "err_bits" struct and
    then passed back down to the core. This had lots of scope for
    accidental combinational loops because as soon as you qualify one
    error with another, you've got a loop all the way around.
    
    This commit tries to simplify things a bit. Now, the controller and
    core have their own cut-down versions of the err_bits_t struct that
    they pass out. We also need signals going "the other way" to tell the
    controller when there has been a fatal error. Since these are
    all (morally) local escalation signals, I've standardised on that
    naming. Now, for example, otbn.sv defines core_escalate_en which
    contains all the "extra" error signals that are OR'd into err_bits and
    didn't come from otbn_core. This signal gets passed down to tell the
    core to stop.
    
    The net result should be that the flow of information is a bit
    clearer (and more one-way!).
    
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
