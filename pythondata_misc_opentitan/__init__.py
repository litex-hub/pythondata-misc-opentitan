import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post5120"
version_tuple = (0, 0, 5120)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post5120")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post5029"
data_version_tuple = (0, 0, 5029)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post5029")
except ImportError:
    pass
data_git_hash = "1b001576ba32555b5260617585cf0a25f3714f30"
data_git_describe = "v0.0-5029-g1b001576b"
data_git_msg = """\
commit 1b001576ba32555b5260617585cf0a25f3714f30
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon Feb 22 12:53:54 2021 +0000

    [otbn] Inline set_half_word_unsigned into BN.MULQACC.SO in ISS
    
    This should have no change on behaviour, but inlining the one and only
    call site gets rid of another state method from the generated
    documentation.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post91"
tool_version_tuple = (0, 0, 91)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post91")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
