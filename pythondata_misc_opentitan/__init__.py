import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post15264"
version_tuple = (0, 0, 15264)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post15264")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post15122"
data_version_tuple = (0, 0, 15122)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post15122")
except ImportError:
    pass
data_git_hash = "a029fa5c6c48ddb5e23d473c793f1f279a943fe9"
data_git_describe = "v0.0-15122-ga029fa5c6c"
data_git_msg = """\
commit a029fa5c6c48ddb5e23d473c793f1f279a943fe9
Author: Weicai Yang <weicai@google.com>
Date:   Fri Nov 4 16:27:48 2022 -0700

    [keymgr/dv] Test fsm_consistency
    
    Test one more custom countermeasure
     - Set `ral.control_shadowed` to OpDisable, so that no Advance or Generate operation
      is selected.
     - Force internal `tb.dut.u_ctrl.adv_en_o` or `tb.dut.u_ctrl.gen_en_o` to 1
    
    Signed-off-by: Weicai Yang <weicai@google.com>

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
