import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post13180"
version_tuple = (0, 0, 13180)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post13180")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13038"
data_version_tuple = (0, 0, 13038)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13038")
except ImportError:
    pass
data_git_hash = "4f8abe14ebd952f4159b77646ab233013860aecc"
data_git_describe = "v0.0-13038-g4f8abe14eb"
data_git_msg = """\
commit 4f8abe14ebd952f4159b77646ab233013860aecc
Author: Chris Frantz <cfrantz@google.com>
Date:   Mon Jul 18 12:57:06 2022 -0700

    [bazel] Improve output artifact query
    
    1. Integrate output files queries into bazelisk as the custom `outquery`
       command.
    2. Update CI scripts.
    
    The `outquery` command provides a number of different query functions
    that may be useful to scripts:
    
    ```
    bazelisk.sh outquery //some:target       # Emit an output filename associated with the target.
    bazelisk.sh outquery-all //some:target   # Emit all output filenames associated with the target.
    bazelisk.sh outquery-foo //some:target   # Emit output filenames with the substring "foo".
    bazelisk.sh outquery.foo //some:target   # Emit output filenames ending with ".foo".
    ```
    
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
