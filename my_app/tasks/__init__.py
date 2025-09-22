"""Task orchestration for the Buildium integration."""

from importlib import import_module
from typing import Any

__all__ = [
    "BuildiumProcessorError",
    "BuildiumWebhookProcessor",
    "enqueue_buildium_webhook",
]


def __getattr__(name: str) -> Any:
    if name in __all__:
        module = import_module("my_app.tasks.buildium_processor")
        return getattr(module, name)
    raise AttributeError(name)
