import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5500"
version_tuple = (0, 0, 5500)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5500")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5405"
data_version_tuple = (0, 0, 5405)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5405")
except ImportError:
    pass
data_git_hash = "5270b7c5366f4cd49c0330fc6b1726b174b339f6"
data_git_describe = "v0.0-5405-g5270b7c53"
data_git_msg = """\
commit 5270b7c5366f4cd49c0330fc6b1726b174b339f6
Author: Timothy Chen <timothytim@google.com>
Date:   Wed Mar 17 17:38:30 2021 -0700

    [top] Hook up latest ast ports and complete a few other integration
    
    - hookup rng_fips to entropy_src
    - properly name test_voltage/test_mode ports and hook them up
    - hookup analog test connections to the pad
    
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
