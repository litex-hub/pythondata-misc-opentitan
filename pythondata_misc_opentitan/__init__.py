import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post8561"
version_tuple = (0, 0, 8561)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post8561")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post8449"
data_version_tuple = (0, 0, 8449)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post8449")
except ImportError:
    pass
data_git_hash = "3cb62ec91052a7c493771266bf856532cb0e2d5a"
data_git_describe = "v0.0-8449-g3cb62ec91"
data_git_msg = """\
commit 3cb62ec91052a7c493771266bf856532cb0e2d5a
Author: Todd Broch <tbroch@rivosinc.com>
Date:   Mon Nov 1 11:09:15 2021 -0700

    [dvsim] Modify resolve_branch to handle branch names with forward slash.
    
    Branch names can include forward slashes (`/`).  Details of allowable
    branch naming conventions can be found here:
    * `man git check-ref-format`
    
    This CL replaces `/` with `-` when creating necessary temp file
    names.
    
    Signed-off-by: Todd Broch <tbroch@rivosinc.com>
    
    TEST=manual,
    ```
    ci/scripts/verible-lint.sh rtl
    ```
    Passes even if branch name contains `/`

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
