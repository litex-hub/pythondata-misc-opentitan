import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5381"
version_tuple = (0, 0, 5381)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5381")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5286"
data_version_tuple = (0, 0, 5286)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5286")
except ImportError:
    pass
data_git_hash = "0949e6de79510494050e5aa39121162a0be7aa3b"
data_git_describe = "v0.0-5286-g0949e6de7"
data_git_msg = """\
commit 0949e6de79510494050e5aa39121162a0be7aa3b
Author: Philipp Wagner <phw@lowrisc.org>
Date:   Mon Mar 8 17:01:01 2021 +0000

    [lint_commits] Propose a command line which signs the commit
    
    We do some basic checks on the commit author to check if it is likely a
    "real name." When this check fails we give a git command line to fix it.
    However in that command line we do not include the `--signoff` flag to add a
    `Signed-off-by` line, meaning users following our guidance will then be
    facing another lint failure. This is fixed in this commit, hopefully
    making our developer experience slightly nicer.
    
    Also replace all uses of `-s` in this doc with `--signoff` to make it
    clearer to users what this flag actually means.
    
    Signed-off-by: Philipp Wagner <phw@lowrisc.org>

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
