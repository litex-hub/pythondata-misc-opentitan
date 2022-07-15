import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13102"
version_tuple = (0, 0, 13102)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13102")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12960"
data_version_tuple = (0, 0, 12960)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12960")
except ImportError:
    pass
data_git_hash = "897650c1d5775a492a7188023fd72048d86310df"
data_git_describe = "v0.0-12960-g897650c1d5"
data_git_msg = """\
commit 897650c1d5775a492a7188023fd72048d86310df
Author: Andreas Kurth <adk@lowrisc.org>
Date:   Wed Jul 13 18:19:10 2022 +0200

    [otbn,dv] Reset model status in scoreboard when reset is released
    
    `otbn_scoreboard` receives status transitions of the OTBN model from
    `otbn_model_monitor`.  On a reset, the monitor waits until the reset is
    released before sampling the status (as the status is not guaranteed to
    have settled directly on the falling reset edge, see 64d77825af).  The
    scoreboard thus on a reset only receives a transaction to the initial
    status (Idle), and it cannot know if the model entered the Idle state
    due to a reset or because OTBN completed execution.
    
    This commit fills this knowledge gap of the scoreboard by adding the
    value of the reset signal (before release) to the status transition.  If
    the status transitions due to reset, the scoreboard resets its mirror of
    the model status as well before using it for checks.
    
    As a bonus side effect, this removes the need to keep the initial value
    of the model status in the scoreboard in sync with RTL and model code.
    
    Signed-off-by: Andreas Kurth <adk@lowrisc.org>

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
