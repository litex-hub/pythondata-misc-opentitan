import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8500"
version_tuple = (0, 0, 8500)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8500")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8388"
data_version_tuple = (0, 0, 8388)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8388")
except ImportError:
    pass
data_git_hash = "255c02843e7ded785130b86b76af0daa3a800158"
data_git_describe = "v0.0-8388-g255c02843"
data_git_msg = """\
commit 255c02843e7ded785130b86b76af0daa3a800158
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Oct 25 16:20:35 2021 +0100

    [otbn,dv] Fix timeout when we inject an IMEM error early in a run
    
    Before commit a85aae3, we only signalled an expected alert when we saw
    a change to STATUS. That didn't work once we'd flopped the STATUS
    register because it changed at the same time as the alert going out.
    
    Unfortunately, there's also a problem with the "fix" in that commit.
    It changed to sending the "expect an alert now" signal as soon as we
    injected an error. However, if we inject an IMEM error just after
    starting OTBN then it might be a while before we get URND data and
    start trying to fetch stuff (and see that IMEM is invalid). In that
    case, it's a while before we see the alert.
    
    Calling set_exp_alert has two effects. Firstly, it allows an alert to
    come in without causing an error. Secondly, it sets a timeout,
    requiring an alert to come in by then in order to avoid an error.
    Here, we set max_delay to some large number of cycles (10k) to
    essentially disable the second of these effects. However, our ISS will
    stop soon afterwards, so we can tighten things up again by requiring
    that an alert goes out at most 10 cycles after that happens.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
