import ujson as json

from typing import Optional

from starlette.requests import Request
from starlette.responses import StreamingResponse

from spinta.components import Context, Action, UrlParams, Model, Node
from spinta import commands
from spinta.formats.jsonlines.components import JsonLines
from spinta.utils.response import aiter, peek_and_stream


@commands.render.register(Context, Request, Model, JsonLines)
def render(
    context: Context,
    request: Request,
    model: Model,
    fmt: JsonLines,
    *,
    action: Action,
    params: UrlParams,
    data,
    status_code: int = 200,
    headers: Optional[dict] = None,
):
    return _render(fmt, data, status_code, headers)


@commands.render.register(Context, Request, Node, JsonLines)
def render(
    context: Context,
    request: Request,
    node: Node,
    fmt: JsonLines,
    *,
    action: Action,
    params: UrlParams,
    data,
    status_code: int = 200,
    headers: Optional[dict] = None,
):
    return _render(fmt, data, status_code, headers)


def _render(fmt: JsonLines, data, status_code: int, headers: dict):
    return StreamingResponse(
        aiter(peek_and_stream(fmt(data))),
        status_code=status_code,
        media_type=fmt.content_type,
        headers=headers
    )
