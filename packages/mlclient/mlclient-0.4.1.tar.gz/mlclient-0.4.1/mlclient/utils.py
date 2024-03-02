"""The ML Client Utils module.

It contains all useful functions and classes shared in ML Client package.
It exports following functions:

    * get_accept_header_for_format(data_format: str) -> str
        Return an Accept header for data format.
    * get_content_type_header_for_data(data: str | dict) -> str
        Return a Content-Type header for data provided.
    * get_resource(resource_name: str) -> TextIO
        Return an MLClient resource.

It also exports a single class:

    * BiDict
        A bidirectional dictionary.
"""
from __future__ import annotations

import importlib.resources as pkg_resources
import json
from typing import Any, TextIO

from mlclient import constants, exceptions
from mlclient import resources as data
from mlclient.exceptions import ResourceNotFoundError


def get_accept_header_for_format(
    data_format: str,
) -> str:
    """Return an Accept header for data format.

    Parameters
    ----------
    data_format : str
        Data format

    Returns
    -------
    str
        An Accept header value

    Raises
    ------
    UnsupportedFormatError
        If the format provided is not being supported
    """
    if data_format in ["xml"]:
        return constants.HEADER_XML
    if data_format in ["json"]:
        return constants.HEADER_JSON
    if data_format in ["html"]:
        return constants.HEADER_HTML
    if data_format in ["text"]:
        return constants.HEADER_PLAIN_TEXT

    msg = f"Provided format [{data_format}] is not supported."
    raise exceptions.UnsupportedFormatError(msg)


def get_content_type_header_for_data(
    content: str | dict,
) -> str:
    """Return a Content-Type header for data provided.

    Parameters
    ----------
    content : str | dict
        Data to send in a request

    Returns
    -------
    str
        A Content-Type header value
    """
    if isinstance(content, dict):
        return constants.HEADER_JSON
    try:
        json.loads(content)
    except ValueError:
        return constants.HEADER_XML
    else:
        return constants.HEADER_JSON


def get_resource(
    resource_name: str,
) -> TextIO:
    """Return an MLClient resource.

    The resource needs to be included in mlclient.resources package
    to be returned.

    Parameters
    ----------
    resource_name : str
        An MLClient resource name

    Returns
    -------
    TextIO
        A MLClient resource

    Raises
    ------
    ResourceNotFoundError
        If the resource does not exist
    """
    try:
        return pkg_resources.open_text(data, resource_name)
    except FileNotFoundError:
        raise ResourceNotFoundError(resource_name) from FileNotFoundError


class BiDict:
    """A bidirectional dictionary.

    This dict allows you to find a corresponding value by key in two directions.
    """

    def __init__(
        self,
        input_dict: dict,
    ):
        """Initialize a BiDict instance.

        Parameters
        ----------
        input_dict : dict
            An input regular dictionary
        """
        self._origin = dict(input_dict)
        self._inverse = {value: key for key, value in input_dict.items()}

    def get(
        self,
        key: Any,
        default: Any = None,
    ) -> Any:
        """Return a corresponding value for a key regardless direction.

        Parameters
        ----------
        key : Any
            A dictionary key or value
        default : Ant, default None
            A default value

        Returns
        -------
        Any
            A corresponding value from the dictionary
        """
        return self._origin.get(key, self._inverse.get(key, default))
