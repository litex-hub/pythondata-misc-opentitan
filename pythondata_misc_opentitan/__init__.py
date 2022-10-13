import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post14726"
version_tuple = (0, 0, 14726)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post14726")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post14584"
data_version_tuple = (0, 0, 14584)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post14584")
except ImportError:
    pass
data_git_hash = "d5f561baac6ab140eb76679020bdbb591a3d80d6"
data_git_describe = "v0.0-14584-gd5f561baac"
data_git_msg = """\
commit d5f561baac6ab140eb76679020bdbb591a3d80d6
Author: Vladimir Rozic <vrozic@lowrisc.org>
Date:   Wed Sep 28 17:14:15 2022 +0100

    [topgen] Strong random class.
    
    A class for generating random numbers using an entropy pool.
    The intention is to use this class to generate random netlist
    constants and permutations.
    
    This commit contains:
        1. strong_random.py containing class strong_random()
            -Constructor
            -load() function for loading the entropy buffer from an
            external entropy buffer file.
            -getrandbits(k) - a function for fetching k random bits
            -randbelow(n) - a function for generating a random
            integer smaller than n
            -shuffle(x) - for generating a random permutation of x
            -bookkeeping and debugging functions isempty() and
            printstatus().
        In case that the buffer runs out of entropy the class issues
        an error and exits.
    
        2. entropy_buffer_generator.py - a script for generating an
        entropy file using random.py
    
    Signed-off-by: Vladimir Rozic <vrozic@lowrisc.org>

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
