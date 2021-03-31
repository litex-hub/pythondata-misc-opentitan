import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5640"
version_tuple = (0, 0, 5640)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5640")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5545"
data_version_tuple = (0, 0, 5545)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5545")
except ImportError:
    pass
data_git_hash = "d37d10da59d9e217e5aff158d0783f88ca71c3f4"
data_git_describe = "v0.0-5545-gd37d10da5"
data_git_msg = """\
commit d37d10da59d9e217e5aff158d0783f88ca71c3f4
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Thu Mar 25 18:35:36 2021 -0700

    [dvsim] Add GUI mode for running simulations
    
    The adds support for running simulations in GUI mode. This change plumbs
    the dvsim switch `--gui` to the underlying tools. With VCS and Xcelium,
    the respective GUI windows will open, exposing the UCLI prompt, where
    the user can take control of running the simulation (debugging, adding
    breakpoints etc).
    
    If GUI mode is enabled and multiple tests are provided for run, it picks
    the first and drops everything else. The onus is on the user to pick
    correctly (pass a single test with `--items` and a specific seed with
    `--seed`).
    
    Further, in GUI mode, it drops the pass and fail patterns, since the
    whole simulation is run from inside the tool (the log file is not
    generated).
    
    Only VCS and Xcelium are currently fully supported. For all others,
    `--gui` has no effect.
    
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
