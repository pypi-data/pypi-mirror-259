from contextlib import contextmanager
from datetime import datetime
from io import TextIOBase
from pathlib import Path
from string import Template
from typing import Any, Iterator, NamedTuple, Type

from pydoctrace.callfilter import CallFilter
from pydoctrace.domain.execution import CallEnd, Error


class Exporter:
    """
    Base class for sequence diagram exporters.
    Extend it to to support various export formats.
    """

    def __init__(self, io_sink: TextIOBase):
        self.io_sink = io_sink

    def on_header(self, start_module: str, start_func_name: str):
        """
        Writes the header of the sequence diagram file.
        This method is supposed to be called only once during an export process.
        """
        raise NotImplementedError()

    def on_raw_content(self, raw_content: str):
        """
        Writes the given raw content to the sink.
        This method is not meant to be used directly.
        """
        self.io_sink.write(raw_content)

    def on_tracing_start(self, called: CallEnd):
        """
        Writes the diagram content leading to the first call (to the decorated function).
        This may be a no-operation.
        """
        raise NotImplementedError()

    def on_start_call(self, caller: CallEnd, called: CallEnd):
        """
        Writes the diagram content corresponding to a call between:
        - a caller: the block of code being executed
        - a called: a block of code being called
        These blocks of code are functions or methods.
        """
        raise NotImplementedError()

    def format_arg_value(self, arg: Any) -> str:
        """
        Formats a value being included in the diagram contents.
        Typically, a value returned by a function.
        Special care must be taken for the None value.
        """
        raise NotImplementedError()

    def on_error_propagation(self, error_called: CallEnd, error_caller: CallEnd, error: Error):
        """
        Writes the diagram contents corresponding to an error propagating
        between the called (which raised or propagated the error) and its caller
        """
        raise NotImplementedError()

    def on_return(self, *, called: CallEnd, caller: CallEnd, arg: Any):
        """
        Writes the diagram contents corresponding to a value returned
        by a called block of code to a caller block of code.
        """
        raise NotImplementedError()

    def on_tracing_end(self, called: CallEnd, arg: Any):
        """
        Special case of on_return when the last executed function returns a value.
        """
        raise NotImplementedError()

    def on_unhandled_error_end(self, called: CallEnd, error: Error):
        """
        Special case of on_tracing_end when an error was not handled by an except block.
        """
        raise NotImplementedError()

    def on_footer(self):
        """
        Writes the footer of the sequence diagram file.
        This method is supposed to be called only once during an export process.
        """
        raise NotImplementedError()

    @staticmethod
    def _template_dynamic_tags(export_file_path_template: str, moment: datetime) -> str:
        return Template(export_file_path_template).safe_substitute(
            datetime_millis=moment.strftime('%Y-%m-%d_%H.%M.%S_%f')[:-3]
        )

    @classmethod
    @contextmanager
    def export_manager_factory(exporter_class: 'Exporter', export_file_path: str) -> Iterator['Exporter']:
        """
        This factory function is meant to be used as a context manager to provide
        an exporter instance usable during the lifetime of the export context.

        The lifetime of the exporter instance is bound to the one of the context, which often
        involves a file handler resource (the export file being written) that is closed at
        the end of the context.
        """

        # hydrates datetime markers in the file name template
        export_file_path = exporter_class._template_dynamic_tags(export_file_path, datetime.utcnow())

        # creates the directories leading to the file
        Path(export_file_path).parent.mkdir(parents=True, exist_ok=True)

        # opens the contents file in write mode and yields the exporter that can write into it
        with open(export_file_path, 'w', encoding='utf8') as diagram_file:
            exporter = exporter_class(diagram_file)
            yield exporter


class Context(NamedTuple):
    """
    Stores information about the tracing process.
    It is used to pass information between the tracer and the diagram exporter.
    """

    exporter_class: Type[Exporter]
    export_file_path: str
    start_module: str
    start_function_name: str
    call_filter: CallFilter
