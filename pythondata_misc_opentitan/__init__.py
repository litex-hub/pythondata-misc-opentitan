import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13302"
version_tuple = (0, 0, 13302)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13302")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13160"
data_version_tuple = (0, 0, 13160)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13160")
except ImportError:
    pass
data_git_hash = "b009abd2b9734e4b7cd9df0cc02282512f30cc5d"
data_git_describe = "v0.0-13160-gb009abd2b9"
data_git_msg = """\
commit b009abd2b9734e4b7cd9df0cc02282512f30cc5d
Author: Pirmin Vogel <vogelpi@lowrisc.org>
Date:   Fri Jun 10 16:43:07 2022 +0200

    [otbn,rtl] Remove reset from FF-based regfiles
    
    This removes the reset from the flip-flop based general-purpose
    registers (GPRs and wide data registers (WDRs) as well as the `ACC` and
    the `MOD` register.  This improves security:  If a register holds a
    random mask to be applied to some other register (remember that the
    masking is implemented in SW here) and an attacker manages to reset that
    register while OTBN is running, the masking is effectively switched off.
    
    Co-authored-by: Andreas Kurth <adk@lowrisc.org>
    Signed-off-by: Pirmin Vogel <vogelpi@lowrisc.org>

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
