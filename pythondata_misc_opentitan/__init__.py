import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "resources")
src = "https://github.com/lowRISC/opentitan"

# Module version
version_str = "0.0.post12427"
version_tuple = (0, 0, 12427)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post12427")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post12285"
data_version_tuple = (0, 0, 12285)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post12285")
except ImportError:
    pass
data_git_hash = "b4d3dedb2f09a22614f365a0c156aa4afa88e375"
data_git_describe = "v0.0-12285-gb4d3dedb2"
data_git_msg = """\
commit b4d3dedb2f09a22614f365a0c156aa4afa88e375
Author: Rupert Swarbrick <rswarbrick@lowrisc.org>
Date:   Mon May 30 14:55:00 2022 +0100

    [bazelisk] Use a lock to avoid downloading Bazel lots of times
    
    Before this change, running lots of instances of bazelisk.sh at once
    meant downloading lots of copies of Bazel. Oops!
    
    Now, if you run bazelisk.sh on its own on a clean checkout, the first
    call to up_to_date will fail. We'll then take a lock, check again that
    we need to download bazelisk (we do!) and then download it, finally
    releasing the lock.
    
    If we run bazelisk.sh in a clean checkout with 100 threads at once,
    they will will all race to get the first flock. One of them will win
    the race and follow the steps above. All of the others will sit and
    wait for that first thread. Once it is done, they will run in order,
    each checking that bazelisk is up to date (it is!) and then do
    whatever job they are supposed to be doing.
    
    Of course, the usual situation is that we've already got bazelisk
    installed. In this case, the first call to up_to_date will pass and we
    won't do any locking at all.
    
    Signed-off-by: Rupert Swarbrick <rswarbrick@lowrisc.org>

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
