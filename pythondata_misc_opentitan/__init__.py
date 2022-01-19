import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9624"
version_tuple = (0, 0, 9624)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9624")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9502"
data_version_tuple = (0, 0, 9502)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9502")
except ImportError:
    pass
data_git_hash = "73b373ddc161d9d2e2d1809c164cd786ddb123de"
data_git_describe = "v0.0-9502-g73b373ddc"
data_git_msg = """\
commit 73b373ddc161d9d2e2d1809c164cd786ddb123de
Author: Jade Philipoom <jadep@google.com>
Date:   Wed Dec 15 17:24:28 2021 +0000

    [sw,otbn] Add scripts for OTBN information-flow analysis.
    
    Adds two scripts based on the recently added information-flow analysis
    machinery:
    - check_const_time.py checks if certain secret values can influence the
    control flow of a subroutine or program
    - analyze_information_flow.py provides more information, e.g. the full
    information-flow graph for a subroutine or program or the final secrets
    given a particular initial set
    
    Signed-off-by: Jade Philipoom <jadep@google.com>

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
