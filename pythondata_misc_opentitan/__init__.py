import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12842"
version_tuple = (0, 0, 12842)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12842")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12700"
data_version_tuple = (0, 0, 12700)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12700")
except ImportError:
    pass
data_git_hash = "d96a35a211a718c031e679774c769c6056283b7a"
data_git_describe = "v0.0-12700-gd96a35a211"
data_git_msg = """\
commit d96a35a211a718c031e679774c769c6056283b7a
Author: Dan McArdle <dmcardle@google.com>
Date:   Fri Jun 24 11:41:07 2022 -0400

    [util] Use correct working dir in generate_compilation_db.py
    
    Specifically, this PR updates the script to emit bazel-opentitan/ as the
    working directory for each compile command.
    
    I used `bazel build -s` to print out subcommands when generating a test
    target, and noticed that it was changing directory before each of the
    calls to gcc, whereas the generated compile_commands.json just points to
    the repo's root directory. Helpfully, Bazel already makes a symlink to
    the correct working directory: bazel-opentitan/.
    
    Signed-off-by: Dan McArdle <dmcardle@google.com>

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
