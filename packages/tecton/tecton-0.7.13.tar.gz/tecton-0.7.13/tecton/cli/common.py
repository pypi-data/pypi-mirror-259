import inspect
import logging
import re
import site
from pathlib import Path

from tecton_proto.args import repo_metadata_pb2
from tecton_proto.common import id_pb2


# Matches frame strings such as "<string>"
SKIP_FRAME_REGEX = re.compile("\<.*\>")


logger = logging.getLogger(__name__)


def get_current_workspace():
    msg = "`tecton.cli.common.get_current_workspace` is deprecated and is no longer supported in 0.7. Please use `tecton.get_current_workspace()` instead."
    raise RuntimeError(msg)


def construct_fco_source_info(fco_id: id_pb2.Id) -> repo_metadata_pb2.SourceInfo:
    """Get the SourceInfo (file name and line number) for an FCO.

    How it works:
    - This function assumed it is being called from the constructor of an FCO
    - inspect.stack() returns the call stack (starting with this function)
    - Walk up the stack frames until the first file within a tecton repo (a child of .tecton) is found
    - The first valid tecton repo file is considered the filename of the FCO.
    """
    from tecton_core.repo_file_handler import _maybe_get_repo_root

    source_info = repo_metadata_pb2.SourceInfo(fco_id=fco_id)
    repo_root = _maybe_get_repo_root()
    if not repo_root:
        return source_info

    # 'getsitepackages' and 'getusersitepackages' are not avaiable in some python envs such as EMR notebook with
    # Python 3.7.
    if not (hasattr(site, "getsitepackages") and hasattr(site, "getusersitepackages")):
        logger.warn(
            "Python 'site' pakcage doesn't contain 'getsitepackages' or 'getusersitepackages' methods. SourceInfo is not going to be populated."
        )
        return source_info

    excluded_site_pkgs = site.getsitepackages() + [site.getusersitepackages()]

    frames = inspect.stack()
    repo_root_path = Path(repo_root)
    for frame in frames:
        if SKIP_FRAME_REGEX.match(frame.frame.f_code.co_filename) is not None:
            continue
        frame_path = Path(frame.frame.f_code.co_filename).resolve()
        if not frame_path.exists():
            continue
        if any(pkg in frame.frame.f_code.co_filename for pkg in excluded_site_pkgs):
            # This filtering is needed in case `tecton` is installed using a virtual
            # environment that's created *inside* the repo root. Without this check,
            # Tecton SDK files would incorrectly be considered a valid repo files
            # and would be listed as the FCO's source filename.
            continue
        if repo_root_path in frame_path.parents:
            rel_filename = frame_path.relative_to(repo_root_path)
            source_info.source_lineno = str(frame.lineno)
            source_info.source_filename = str(rel_filename)
            break
    return source_info


def get_debug(ctx):
    while ctx.parent:
        ctx = ctx.parent
    return ctx.params["debug"]


def get_verbose(ctx):
    while ctx.parent:
        ctx = ctx.parent
    return ctx.params["verbose"]
