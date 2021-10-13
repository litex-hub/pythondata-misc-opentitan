import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8248"
version_tuple = (0, 0, 8248)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8248")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8136"
data_version_tuple = (0, 0, 8136)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8136")
except ImportError:
    pass
data_git_hash = "e56b147144d2d9c2a412e7a52d90cd39f4a9274a"
data_git_describe = "v0.0-8136-ge56b14714"
data_git_msg = """\
commit e56b147144d2d9c2a412e7a52d90cd39f4a9274a
Author: Timothy Trippel <ttrippel@google.com>
Date:   Wed Oct 6 19:01:01 2021 +0000

    [hw/aon_timer] Make IRQ and signal names consistent.
    
    This fixes #8533.
    
    Every IP that can raise IRQs has an `interrupt_list` field in its HJSON
    file that lists the names (in snake case) and brief descriptions (in a
    full sentence/phrase) of each interrupt it produces.
    
    Additionally, for IPs that raise IRQs, their HJSON usually defines the
    following three registers: INTR_STATE, INTR_ENABLE, and INTR_TEST.
    Typically, the bit fields within each of those three registers map 1:1
    with the interrupts listed above in the `interrupt_list` field, and
    **_therefore their names match_**.
    
    However, in the aon_timer, the `wdog_timer_bark` interrupt was also
    referred to as `wdog_timer_expired`. This fixes this naming
    irregularity.
    
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
