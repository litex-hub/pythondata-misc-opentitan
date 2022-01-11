import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9423"
version_tuple = (0, 0, 9423)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9423")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9305"
data_version_tuple = (0, 0, 9305)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9305")
except ImportError:
    pass
data_git_hash = "b293e9467b1cb828ed5794ec93d7007d73ce6565"
data_git_describe = "v0.0-9305-gb293e9467"
data_git_msg = """\
commit b293e9467b1cb828ed5794ec93d7007d73ce6565
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Fri Jan 7 14:29:41 2022 +0000

    [otbn,dv] Only run the exp_end_addr check for some runs
    
    The expected end address check wasn't quite working now that we had a
    key sideload interface. The problem is that if you read from one of
    the sideload key WSRs when there's no key, the operation immediately
    stops with an error. That's fine, but we won't stop at the address we
    expected.
    
    To allow this check to run at least some of the time (giving us more
    confidence in the rig), we define a new absent_key_allowed flag. If
    it's true, we use the normal key sideload sequence and disable the
    check. If it's false, we grab control of the sideload sequencer and
    run a specialised version where the key might change, but it always
    has a value. In this case, we can assert the end address again.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post118"
tool_version_tuple = (0, 0, 118)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post118")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
