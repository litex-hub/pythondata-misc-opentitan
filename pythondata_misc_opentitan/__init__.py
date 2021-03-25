import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5577"
version_tuple = (0, 0, 5577)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5577")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5482"
data_version_tuple = (0, 0, 5482)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5482")
except ImportError:
    pass
data_git_hash = "f49bee189f77c731ad00b92627c1b70d905b2a90"
data_git_describe = "v0.0-5482-gf49bee189"
data_git_msg = """\
commit f49bee189f77c731ad00b92627c1b70d905b2a90
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Wed Mar 24 17:55:16 2021 -0700

    [dvsim] Prevent command echo suppression
    
    At some point in the past, I had refactored the way SW images were
    handled. I had added `.ONESHELL:` to the `sw_build` target, assuming
    that the `.ONESHELL` would only affect that target (cause all recipes of
    a target to execute in the same shell). Turns out, its more of a global
    setting - it affects ALL recipes of all targets.
    
    This had an unintended consequence:
    For all targets, the first recipe is an echo command printing the name
    of that target, the echoing of which is suppressed with an `@`. Because the
    rest of the recipes get invoked in the same shell, their echoing is also
    suppressed. This makes issues hard to debug.
    
    In this change, the `.ONESHELL` is removed, and all recipes of
    `sw_build` are invoked one the same line with a trailing `\`. The first
    command is `set -e` which is the equivalent of all commands chained with
    `&&` (which is already what we want).
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
