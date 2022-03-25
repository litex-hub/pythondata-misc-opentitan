import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11126"
version_tuple = (0, 0, 11126)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11126")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11000"
data_version_tuple = (0, 0, 11000)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11000")
except ImportError:
    pass
data_git_hash = "313611f217e0e1cc52fd6faec306f866decb502b"
data_git_describe = "v0.0-11000-g313611f21"
data_git_msg = """\
commit 313611f217e0e1cc52fd6faec306f866decb502b
Author: Jade Philipoom <jadep@google.com>
Date:   Wed Mar 23 13:59:17 2022 +0000

    [doc] Clean up after feedback on Getting Started refactor.
    
    Fix some awkward wording etc, add some clarification about the
    `--meminit` arguments to Verilator, and clarify that we do not currently
    provide pre-built Docker containers.
    
    Also incorporate sometext about Siemens Questa that was added to the
    old install guide while the PR was pending.
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

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
