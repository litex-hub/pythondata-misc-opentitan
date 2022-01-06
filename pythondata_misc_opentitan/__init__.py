import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9367"
version_tuple = (0, 0, 9367)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9367")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9250"
data_version_tuple = (0, 0, 9250)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9250")
except ImportError:
    pass
data_git_hash = "029d20f5daf06c862b1b8b426a923b28efffd90b"
data_git_describe = "v0.0-9250-g029d20f5d"
data_git_msg = """\
commit 029d20f5daf06c862b1b8b426a923b28efffd90b
Author: Guillermo Maturana <maturana@google.com>
Date:   Wed Jan 5 20:56:01 2022 -0800

    [dv/pwrmgr] Add more pwrmgr SVAs
    
    Add SVA checking the incoming reset requests cause rstreqs outputs to
    rstmgr to respond correctly.
    Bind clkmgr_pwrmgr_sva_if into pwrmgr to check clk_en/status protocol.
    Fix some SVAs to be less rigid without loosing checks.
    Split clkmgr_pwrmgr_sva_if.sv into separate target for sharing.
    Improve escalation stimulus to get cleared when pwrmgr requests lc reset.
    Clear resets at the end of each wakeup_reset round in case they were disabled.
    Disable estclk_ctrl selection at the end of each extclk sequence round.
    Minor formatting fixes for verible.
    
    Signed-off-by: Guillermo Maturana <maturana@google.com>

"""

# Tool version info
tool_version_str = "0.0.post117"
tool_version_tuple = (0, 0, 117)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post117")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
