import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10893"
version_tuple = (0, 0, 10893)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10893")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10767"
data_version_tuple = (0, 0, 10767)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10767")
except ImportError:
    pass
data_git_hash = "d8492a38f89ed28328e1bf08dcef4507a7801e81"
data_git_describe = "v0.0-10767-gd8492a38f"
data_git_msg = """\
commit d8492a38f89ed28328e1bf08dcef4507a7801e81
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Mar 14 13:22:43 2022 -0700

    [keymgr] d2s configuration cross checks
    
    - Addresses the cross check item in #11387
    
    - dest_sel cross check
      - check that when a sideload key operation is written, the original
        register configuration and the final select used are consistent
    
    - operation cross check
      - check that after the one hot command check, the "deployed" command
        value is continuously checked with the original configuration.
      - check that when the main fsm changes state into one of the key states,
        it was due to an advancted type command
      - check that if the operational state is in generate or advanced, it is
        consistent with the original configuration input
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
