from types import ModuleType
from typing import Any, Callable

def attach(
    package_name: str,
    submodules: list[str] | None = None,
    submod_attrs: dict[str, list[str]] | None = None,
) -> tuple[
    Callable[[str], Any],
    Callable[[], list[str]],
    list[str],
]: ...
def attach_stub(
    package_name: str,
    filename: str,
) -> tuple[
    Callable[[str], Any],
    Callable[[], list[str]],
    list[str],
]: ...
def load(
    fullname: str,
    *,
    require: str | None = None,
    error_on_import: bool = False,
    suppress_warning: bool = False,
) -> ModuleType: ...
