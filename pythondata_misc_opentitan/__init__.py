import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post10630"
version_tuple = (0, 0, 10630)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post10630")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10504"
data_version_tuple = (0, 0, 10504)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10504")
except ImportError:
    pass
data_git_hash = "538963449db03df4ee9dd61715fa8d261e4cdfe3"
data_git_describe = "v0.0-10504-g538963449"
data_git_msg = """\
commit 538963449db03df4ee9dd61715fa8d261e4cdfe3
Author: Timothy Chen <timothytim@google.com>
Date:   Mon Feb 28 10:54:27 2022 -0800

    [adc_ctrl] Documentation update for pwrup timing
    
    - fixes #10782
    - clarify that after adc power up complete, the internal fsm mechanism
      takes two more cycles before an adc channel is selected
    
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
