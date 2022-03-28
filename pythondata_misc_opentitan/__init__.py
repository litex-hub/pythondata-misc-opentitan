import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post11165"
version_tuple = (0, 0, 11165)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post11165")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post11039"
data_version_tuple = (0, 0, 11039)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post11039")
except ImportError:
    pass
data_git_hash = "a21a5b1116250e0960c2aaf53ad9f723fa402448"
data_git_describe = "v0.0-11039-ga21a5b111"
data_git_msg = """\
commit a21a5b1116250e0960c2aaf53ad9f723fa402448
Author: Timothy Chen <timothytim@google.com>
Date:   Thu Mar 24 19:17:37 2022 -0700

    [adc_ctrl] slightly tweak assertion
    
    - previous assertion is no longer true due to the way
      stay_match is now computed (0 -> new value is counted as a match)
    
    - add an assertion to check to make sure when adc is powered down
      counters are actually cleared.  This caused an issue previously
      when they were not.
    
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
