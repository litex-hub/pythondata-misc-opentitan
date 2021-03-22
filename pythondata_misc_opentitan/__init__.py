import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5508"
version_tuple = (0, 0, 5508)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5508")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5413"
data_version_tuple = (0, 0, 5413)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5413")
except ImportError:
    pass
data_git_hash = "c42725cdb717f9e059759a26bfbfdc4e37ccf96e"
data_git_describe = "v0.0-5413-gc42725cdb"
data_git_msg = """\
commit c42725cdb717f9e059759a26bfbfdc4e37ccf96e
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Fri Mar 19 17:14:37 2021 +0000

    [otbn] Refactor ISS stalling behaviour
    
    Previously the ISS would execute an instruction then stall for some
    number of cycles before committing the result. This alters the behaviour
    so instructions can explicitly request a stall (via returning False from
    OTBN.pre_execute) and multi-cycle instructions (LW/BN.LID are the only
    examples so far) will stall themselves before they execute rather than
    after.
    
    A seperate OTBNState.non_insn_stall is introduced to support non
    instuction related sources of stall. For now this is just used by a
    single stall cycle at the beginning of execution.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

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
