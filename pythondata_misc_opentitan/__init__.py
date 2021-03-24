import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5542"
version_tuple = (0, 0, 5542)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5542")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5447"
data_version_tuple = (0, 0, 5447)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5447")
except ImportError:
    pass
data_git_hash = "37b0c994439615f70b45202b1f90e15dc5510dd1"
data_git_describe = "v0.0-5447-g37b0c9944"
data_git_msg = """\
commit 37b0c994439615f70b45202b1f90e15dc5510dd1
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Tue Mar 23 16:27:26 2021 -0700

    [dvsim] Spot fixes for LSF and internal launcher
    
    Over the past few weeks, the scheduling and launching mechanism were
    refactored to fully support LSF and our Google cloud which is used
    internally.
    
    The fixes made in this PR are minor ones to support our internal cloud
    launcher (which will not be committed to our open repo).
    
    The fixes are as follows:
    - Updates to commands and env vars in the HJson data
    - Addition of `input_dirs` and `output_dirs` variables in `Deploy`
      - This is needed only for the cloud launcher because jobs with cloud
      run in a hermetically sealed VM which needs to explicitly indicate
      what the input and output data is.
      - We will refactor this again in future when we will flip the Deploy
      and Launcher hierarchy.
    - Fixes to command sub-strings (ensure they are quoted properly)
    - Allow remote launchers to set their own python virtualenv region
    - Some cosmetic changes
    
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
