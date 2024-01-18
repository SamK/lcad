"""
Take care of the command line interface
"""
import sys
import textwrap
import argparse
from lcad import log, __version__

import lcad.parserlib

__description__ = """
Convert a data type to any data type.
"""

__epilog__ = ""


def list_formats(_):
    """
    Print all the supported formats
    """
    output = []
    for name, properties in lcad.parserlib.discover_parsers().items():
        format_lines = []

        # skip if required
        if properties["hide"]:
            log.debug(f"Hiding format {format}")
            continue

        # determine capabilities
        capabilities = []
        for operation in ["load", "dump"]:
            if operation in properties and properties[operation]:
                capabilities.append(operation)
        f_cap = ", ".join(capabilities)
        format_lines.append(f"{name} ({f_cap}):")

        # determine doc
        doc = properties["doc"]
        if doc:
            doc = doc.rstrip("\n").lstrip("\n")
            doc = textwrap.indent(doc, " " * 4)
            format_lines.append(doc)

        # build output
        output.append("\n".join(format_lines))
    print("\n\n".join(output))


def convert(args):
    """load, convert and dump"""

    output_args = parse_output_extra_args(args.output_args)

    try:
        input_result = lcad.parserlib.load_file(args)
        output_result = lcad.parserlib.dump_file(
            input_result, args.output_format, output_args
        )
    except (
        lcad.errors.UnknownFileFormat,
        lcad.errors.DataInputError,
        lcad.errors.DataOutputError,
    ) as error:
        log.critical(error)
        sys.exit(2)

    print(output_result, file=args.output_file)


def parse_arguments(args=None):
    """Parse the command line arguments given by the user"""
    _help_output_args = """
    Provide specific output arguments to the output format.
    The arguments are directly passed to the function provided by the parser.
    The format documentation (command "formats") should provide more detailed informations.
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=__description__,
        epilog=textwrap.dedent(__epilog__),
    )

    parser.add_argument("--version", "-V", action="version", version=__version__)
    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        default=0,
        help="verbose mode; use -vv for debug mode",
    )

    subparsers = parser.add_subparsers(
        help="choose between these actions", dest="action"
    )
    subparsers.required = True

    sp_formats = subparsers.add_parser("formats", help="list supported file formats")
    sp_formats.set_defaults(call_function=list_formats)

    sp_conv = subparsers.add_parser("convert", help='Convert (see "convert --help")')

    sp_conv.add_argument("--input-format", "--from", help="input format", required=True)
    sp_conv.add_argument("--output-format", "--to", help="output format", required=True)
    sp_conv.add_argument(
        "--input-file",
        "-i",
        help="input file",
        type=argparse.FileType("r"),
        default=sys.stdin,
        nargs="?",
    )
    sp_conv.add_argument(
        "--output-file",
        "-o",
        help="output file",
        type=argparse.FileType("w"),
        default=sys.stdout,
        nargs="?",
    )
    sp_conv.add_argument("--output-args", nargs="*", help=_help_output_args, default=[])
    sp_conv.set_defaults(call_function=convert)

    return parser.parse_args(args)


def parse_output_extra_args(output_args):
    """
    https://stackoverflow.com/a/45025811/238913
    """
    parsed_conf = {}
    for pair in output_args:
        key, value = pair.split("=")
        if value.isnumeric():
            value_ = int(value)
        elif value in ["True", "False"]:
            value_ = bool(value)
        else:
            value_ = value
        parsed_conf[key] = value_
    return parsed_conf


def main(special_args=None):
    """Main function"""

    # retrive the user args
    args = parse_arguments(special_args)
    # setup logging
    log.setup_logging(args)
    log.debug("args: " + str(args))

    # execute the appropriate function
    args.call_function(args)
