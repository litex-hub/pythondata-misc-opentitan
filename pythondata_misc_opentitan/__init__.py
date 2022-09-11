import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14116"
version_tuple = (0, 0, 14116)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14116")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post13974"
data_version_tuple = (0, 0, 13974)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post13974")
except ImportError:
    pass
data_git_hash = "3c54b1eb225f685fe528a88992a1b8de3e30cd4b"
data_git_describe = "v0.0-13974-g3c54b1eb22"
data_git_msg = """\
commit 3c54b1eb225f685fe528a88992a1b8de3e30cd4b
Author: Srikrishna Iyer <sriyer@google.com>
Date:   Sat Sep 10 01:01:26 2022 -0700

    [util] Fix extract_sw_logs.py
    
    Fixes #14636.
    Fixes issue encountered in #14858.
    
    Rather than being told which ELF sections to parse and generate a database
    from, the script now reads ALL valid sections from the ELF and creates a
    database of address and string found at that address. This eliminates the
    need to pass sections using the `--rodata-sections` arg in the bazel rules.
    This takes care of string constants that reside in other sections (for
    example, the `chip_info` which resides in its own `.chip_info` section).
    
    The other bug was in the `get_str_at_addr()` method, which returns
    a string (or substring) starting at a particular address. This computation
    requires the original length of the string to be known. Since the strings
    go through sanitization, the orignal length may change, leading to errors
    thrown when printing single whitespace characters, such as
    `LOG_INFO("\n")`. The change records the original length of the string
    along with the string (as a tuple) at each address.
    
    Signed-off-by: Srikrishna Iyer <sriyer@google.com>

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
