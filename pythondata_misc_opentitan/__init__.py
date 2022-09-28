import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14481"
version_tuple = (0, 0, 14481)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14481")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14339"
data_version_tuple = (0, 0, 14339)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14339")
except ImportError:
    pass
data_git_hash = "81118ff4ed767b6ecdbe78e56f34ba20658a05e7"
data_git_describe = "v0.0-14339-g81118ff4ed"
data_git_msg = """\
commit 81118ff4ed767b6ecdbe78e56f34ba20658a05e7
Author: Chris Frantz <cfrantz@google.com>
Date:   Mon Sep 19 19:47:08 2022 -0700

    [ottool] Emit results as colorized hjson
    
    1. Use serde_annotate as the emitter.
    1a. Select an output format with `-f` or `--format`.  `json`, `json5`,
        `hjson` and `yaml` are available as output formats.
    1b. If stdout is a terminal, default to color output.
    2. Use serde_annotate to parse the opentitantool config files.  This
       means the various json configs no longer have to be strict-json and
       can use hjson or json5 extensions like comments or hex-literals.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
