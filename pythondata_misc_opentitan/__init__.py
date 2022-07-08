import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12975"
version_tuple = (0, 0, 12975)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12975")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12833"
data_version_tuple = (0, 0, 12833)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12833")
except ImportError:
    pass
data_git_hash = "461b8f3c41f9d1f3341f9a5582a51018daeb6243"
data_git_describe = "v0.0-12833-g461b8f3c41"
data_git_msg = """\
commit 461b8f3c41f9d1f3341f9a5582a51018daeb6243
Author: Prajwala Puttappa <prajwalaputtappa@lowrisc.org>
Date:   Wed Jun 22 11:29:45 2022 +0100

    [otbn, dv] Adds otbn_pc_ctrl_flow_redun testcase
    
    This commit adds a new testcase to verify OTBN.PC.CTRL_FLOW.REDUN
    countermeasure.
    
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
