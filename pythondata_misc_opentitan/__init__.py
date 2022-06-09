import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12584"
version_tuple = (0, 0, 12584)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12584")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12442"
data_version_tuple = (0, 0, 12442)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12442")
except ImportError:
    pass
data_git_hash = "fcdc4e943331b5bdd14721a187ee3819942f2772"
data_git_describe = "v0.0-12442-gfcdc4e943"
data_git_msg = """\
commit fcdc4e943331b5bdd14721a187ee3819942f2772
Author: Greg Chadwick <gac@lowrisc.org>
Date:   Tue Jun 7 18:15:11 2022 +0100

    [otbn, rtl] Add control flow target checking
    
    For loop, branch and jump (other than JALR) the target can be calculated
    within the predecode stage as it's just the PC + some immediate. This
    adds that calulation to the predecode stage and cross checks it against
    the calculated target in the execute stage.
    
    Signed-off-by: Greg Chadwick <gac@lowrisc.org>

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_misc_opentitan."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_misc_opentitan".format(f))
    return fn
