import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5355"
version_tuple = (0, 0, 5355)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5355")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5260"
data_version_tuple = (0, 0, 5260)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5260")
except ImportError:
    pass
data_git_hash = "bbba55462b49f139f013fc804e9fb9999cee7102"
data_git_describe = "v0.0-5260-gbbba55462"
data_git_msg = """\
commit bbba55462b49f139f013fc804e9fb9999cee7102
Author: Udi Jonnalagadda <udij@google.com>
Date:   Wed Mar 10 02:42:37 2021 -0800

    [dv/sram] implement pipelining test and update scb
    
    this PR adds the SRAM pipelining test as laid out in the testplan.
    
    in this test, we choose a random mem address and send a series of
    back-to-back transactions to that address, to stress the internal
    pipelining and forwarding logic.
    
    this requires an overhaul of the scoreboard as the SRAM pipelining logic
    means that while TL memory requests are handled in-order, the underlying
    memory macro is updated in an out-of-order fashion, leading to several
    tricky edge cases.
    
    NOTE: this PR depends on #5530 to be merged first, as that contains a
          fix for an issue uncovered by this test.
    
    Signed-off-by: Udi Jonnalagadda <udij@google.com>

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
