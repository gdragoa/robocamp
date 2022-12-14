from __future__ import annotations

from asyncio import CancelledError
from typing import TYPE_CHECKING, Any, List, Optional, Union

from ....jsonrpc2.protocol import rpc_method
from ....utils.async_tools import async_tasking_event, threaded
from ....utils.logging import LoggingDescriptor
from ..decorators import HasLanguageId, language_id_filter
from ..has_extend_capabilities import HasExtendCapabilities
from ..lsp_types import (
    DocumentFilter,
    DocumentSelector,
    InlineValue,
    InlineValueContext,
    InlineValueParams,
    InlineValueRegistrationOptions,
    Position,
    Range,
    ServerCapabilities,
    TextDocumentIdentifier,
)
from ..text_document import TextDocument

if TYPE_CHECKING:
    from ..protocol import LanguageServerProtocol  # pragma: no cover

from .protocol_part import LanguageServerProtocolPart


class InlineValueProtocolPart(LanguageServerProtocolPart, HasExtendCapabilities):

    _logger = LoggingDescriptor()

    def __init__(self, parent: LanguageServerProtocol) -> None:
        super().__init__(parent)

    @async_tasking_event
    async def collect(
        sender, document: TextDocument, range: Range, context: InlineValueContext  # pragma: no cover, NOSONAR
    ) -> Optional[List[InlineValue]]:
        ...

    def extend_capabilities(self, capabilities: ServerCapabilities) -> None:
        if len(self.collect):
            document_filters: DocumentSelector = []
            for e in self.collect:
                if isinstance(e, HasLanguageId):
                    document_filters.append(DocumentFilter(language=e.__language_id__))
            capabilities.inline_value_provider = InlineValueRegistrationOptions(
                work_done_progress=True, document_selector=document_filters if document_filters else None
            )

    @rpc_method(name="textDocument/inlineValue", param_type=InlineValueParams)
    @threaded()
    async def _text_document_inline_value(
        self,
        text_document: TextDocumentIdentifier,
        range: Union[Range, List[Position]],
        context: InlineValueContext,
        *args: Any,
        **kwargs: Any,
    ) -> Optional[List[InlineValue]]:

        results: List[InlineValue] = []
        document = await self.parent.documents.get(text_document.uri)
        if document is None:
            return None

        for result in await self.collect(self, document, range, context, callback_filter=language_id_filter(document)):
            if isinstance(result, BaseException):
                if not isinstance(result, CancelledError):
                    self._logger.exception(result, exc_info=result)
            else:
                if result is not None:
                    results += result

        if len(results) == 0:
            return None

        return results

    async def refresh(self) -> None:
        if (
            self.parent.client_capabilities
            and self.parent.client_capabilities.workspace
            and self.parent.client_capabilities.workspace.inline_value
            and self.parent.client_capabilities.workspace.inline_value.refresh_support
        ):
            await self.parent.send_request_async("workspace/inlineValue/refresh")
