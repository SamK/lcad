"""
Functions related to the manipulation of the parsers
"""
import importlib
from pkgutil import iter_modules
from importlib.util import find_spec
from inspect import getmembers, isfunction
import lcad.parsers
import lcad.errors
from lcad import log


def has_function(module, function_name):
    """Determine if a given module contains a function called "function_name" """
    functions_list = getmembers(module, isfunction)
    return any(f[0] == function_name for f in functions_list)
    # return function_name in functions_list


def list_submodules(module):
    """Return a list of submodules objects who are part of the module given"""
    submodules = []
    for submodule in iter_modules(module.__path__):
        submodules.append(submodule)
    return submodules


def discover_parsers():
    """Return a list of discovered parsers"""
    parsers_found = {}
    for submodule in list_submodules(lcad.parsers):
        log.debug("Found submodule: {}".format(submodule.name))
        parser_module_name = "lcad.parsers.{}".format(submodule.name)
        module = importlib.import_module(parser_module_name)
        parser = {
            "load": has_function(module, "load"),
            "dump": has_function(module, "dump"),
            "doc": module.__doc__,
        }
        parsers_found[submodule.name] = parser
    return parsers_found


def find_module_spec(module_name):
    """Dynamically import a module based on the module name"""
    log.debug('Importing module {}..."'.format(module_name))
    parser_spec = find_spec(module_name)
    if parser_spec is None:
        log.warn('Parser "{}" not found!'.format(module_name))
        raise lcad.errors.UnknownFileFormat
    log.debug('Found parser "{}": {}'.format(module_name, parser_spec))
    return parser_spec


def load_file(args):
    parser_module_name = "lcad.parsers." + args.input_format
    try:
        find_module_spec(parser_module_name)
    except lcad.errors.UnknownFileFormat as error:
        raise type(error)('Unknown input format: "{}"'.format(args.input_format))
    parser = importlib.import_module(parser_module_name)
    return parser.load(args.input_file)


def dump_file(data, output_format, output_args):
    parser_module_name = "lcad.parsers." + output_format
    try:
        find_module_spec(parser_module_name)
    except lcad.errors.UnknownFileFormat as error:
        raise type(error)('Unknown output format: "{}"'.format(output_format))
    parser = importlib.import_module(parser_module_name)
    return parser.dump(data, output_args)
