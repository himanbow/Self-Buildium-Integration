from __future__ import annotations

import sys
import types
from dataclasses import dataclass
from pathlib import Path
from typing import Any


_PACKAGE_ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class _StubVerifiedBuildiumWebhook:
    account_context: Any
    account_id: str
    envelope: Any
    signature: str = "signature"
    verification_scheme: str = "stub"


def _ensure_package_module(name: str, path: Path) -> types.ModuleType:
    module = sys.modules.get(name)
    if module is None:
        module = types.ModuleType(name)
        module.__path__ = [str(path)]
        sys.modules[name] = module
    else:
        module_path = getattr(module, "__path__", [])
        if str(path) not in module_path:
            if module_path:
                module.__path__ = list(module_path) + [str(path)]
            else:
                module.__path__ = [str(path)]
    return module


_ensure_package_module("my_app", _PACKAGE_ROOT)
_ensure_package_module("my_app.webhooks", _PACKAGE_ROOT / "webhooks")

verification_name = "my_app.webhooks.verification"
if verification_name not in sys.modules:
    verification_module = types.ModuleType(verification_name)
    verification_module.__all__ = ["VerifiedBuildiumWebhook"]
    verification_module.VerifiedBuildiumWebhook = _StubVerifiedBuildiumWebhook
    verification_module.__package__ = "my_app.webhooks"
    sys.modules[verification_name] = verification_module


def pytest_configure() -> None:
    _ensure_package_module("my_app", _PACKAGE_ROOT)
    _ensure_package_module("my_app.webhooks", _PACKAGE_ROOT / "webhooks")

    if verification_name not in sys.modules:
        verification_module = types.ModuleType(verification_name)
        verification_module.__all__ = ["VerifiedBuildiumWebhook"]
        verification_module.VerifiedBuildiumWebhook = _StubVerifiedBuildiumWebhook
        verification_module.__package__ = "my_app.webhooks"
        sys.modules[verification_name] = verification_module
