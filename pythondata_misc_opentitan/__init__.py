import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14163"
version_tuple = (0, 0, 14163)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14163")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14021"
data_version_tuple = (0, 0, 14021)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14021")
except ImportError:
    pass
data_git_hash = "85057ad934a7e13fd28ed4f142fc943259f328a6"
data_git_describe = "v0.0-14021-g85057ad934"
data_git_msg = """\
commit 85057ad934a7e13fd28ed4f142fc943259f328a6
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Tue Aug 30 10:12:52 2022 +0100

    [otbn, dv] Added a testcase to verify *_STACK.ADDR.INTEGRITY
    
    This commit adds a new testcase called otbn_stack_addr_integ_chk to
    verify OTBN.CALL_STACK.ADDR.INTEGRITY and OTBN.LOOP_STACK.ADDR.INTEGRITY
    countermeasures.
    
    Signed-off-by: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>

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
