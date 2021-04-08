import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5767"
version_tuple = (0, 0, 5767)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5767")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5672"
data_version_tuple = (0, 0, 5672)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5672")
except ImportError:
    pass
data_git_hash = "8961a8026331fcf39899d73e10a9e5a3c69193b2"
data_git_describe = "v0.0-5672-g8961a8026"
data_git_msg = """\
commit 8961a8026331fcf39899d73e10a9e5a3c69193b2
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 31 19:56:10 2021 -0700

    [sw] Minor software updates for dif_entropy_src and test
    
    - This change should now ensure the new seed is used and
      the entropy reads should be different between reads.
    - Lastly, a few auxillary functions are added to poll for specific
      status.  These likely should be replaced long term by something
      more robust
    - unittests are also udpated for the slightly tweaked sequence
    - At the moment, since we disable / re-enable entropy_src, the
      timing differences between platforms (dv vs verilator) causes
      the test to spit out different results.  For the time being,
      favor verilator until #5941 is in.
    
    Signed-off-by: Timothy Chen <timothytim@google.com>

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
