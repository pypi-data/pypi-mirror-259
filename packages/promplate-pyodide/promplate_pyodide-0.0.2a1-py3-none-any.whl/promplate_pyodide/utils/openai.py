from contextlib import suppress
from functools import cache
from typing import cast

from pyodide.code import run_js
from pyodide.ffi import JsCallable, register_js_module, to_js


async def ensure_openai(fallback_import_url: str = "https://esm.sh/openai"):
    with suppress(ModuleNotFoundError):
        import openai

    openai = await run_js(f"import({fallback_import_url!r})")  # noqa

    register_js_module("openai", openai)


@cache
def translate_openai():
    from openai import AsyncClient as js_openai_class

    js_openai_class = cast(JsCallable, js_openai_class)

    def make_client(
        api_key: str | None = None,
        organization: str | None = None,
        base_url: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        default_headers: dict | None = None,
        default_query: dict | None = None,
        **_,
    ):
        return js_openai_class.new(
            apiKey=api_key or "",
            organization=organization,
            baseURL=base_url,
            timeout=timeout,
            maxRetries=max_retries,
            defaultHeaders=to_js(default_headers),
            defaultQuery=to_js(default_query),
            dangerouslyAllowBrowser=True,
        )

    return make_client