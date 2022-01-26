import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post9824"
version_tuple = (0, 0, 9824)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post9824")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post9702"
data_version_tuple = (0, 0, 9702)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post9702")
except ImportError:
    pass
data_git_hash = "a768d0b30ca8fcb6ea249546280f845ee7ef9710"
data_git_describe = "v0.0-9702-ga768d0b30"
data_git_msg = """\
commit a768d0b30ca8fcb6ea249546280f845ee7ef9710
Author: Drew Macrae <drewmacrae@google.com>
Date:   Wed Jan 26 07:40:16 2022 -0800

    [CODEOWNERS] Extra codeowners for CI
    
    I solicited extra codeowners for CI tools before seeing that @mcy was
    already assigned as an owner but a typo kept it from controlling the
    file that should have assigned it. I've added in the volunteers because
    I think that will just help with review and situational awareness and I
    don't think it will change anyone's ability to submit code.
    
    Signed-off-by: Drew Macrae <drewmacrae@google.com>

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
