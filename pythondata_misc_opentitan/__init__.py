import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13032"
version_tuple = (0, 0, 13032)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13032")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12890"
data_version_tuple = (0, 0, 12890)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12890")
except ImportError:
    pass
data_git_hash = "db5ae4da3144f15ac8f5e3150502213b1491b054"
data_git_describe = "v0.0-12890-gdb5ae4da31"
data_git_msg = """\
commit db5ae4da3144f15ac8f5e3150502213b1491b054
Author: Chris Frantz <cfrantz@google.com>
Date:   Tue Jun 21 18:32:47 2022 -0700

    [base] Add a `status_t` for use in user code
    
    `status_t` is modelled after `absl::Status` and uses the same error
    categories.
    
    - Ok status codes can carry any positive integer value from [0 .. INT_MAX].
    - Error status codes carry the error code, the module id that
      created the error (the first 3 letters of the filename) and a
      parameter in the range [0 .. 2047] that, by default, is the
      source line number in the module that created the error.
    - A nonstandard printf specifier `%r` prints out a text representation
      of the status value.
    
    The c++ standard is changed from `c++14` to `gnu++14`.  The preprocessor
    macro magic used to create the error values is not turned on by
    `-std=c++14` (ie: this change needs the comma elision behavior of
    `##__VA_ARGS__`).  Lamentably, standard c++20 replacement `__VA_OPT__(,)`
    does not work when `-std=c++14`.
    
    Signed-off-by: Chris Frantz <cfrantz@google.com>

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
