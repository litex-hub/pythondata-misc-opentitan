import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11068"
version_tuple = (0, 0, 11068)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11068")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10942"
data_version_tuple = (0, 0, 10942)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10942")
except ImportError:
    pass
data_git_hash = "a66d66236aa3077e753a0c84533f64410c371d68"
data_git_describe = "v0.0-10942-ga66d66236"
data_git_msg = """\
commit a66d66236aa3077e753a0c84533f64410c371d68
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Mar 15 21:31:58 2022 -0700

    [rv_dm dv] Testplan & DV doc updates
    
    This commit adds the (almost) complete testplan for rv_dm.
    It incorporates the testplan review comments captured in the meeting
    notes:
    https://docs.google.com/document/d/1zIU5XQKFuu72SqUzEpaFGZEgQlIKgy6_iejXfatb1PQ/edit#heading=h.5utrntqp5k6d
    
    The DV doc highlights the testbench block diagram and the flow of
    information into the scoreboard where most of the checks will be
    performed.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
