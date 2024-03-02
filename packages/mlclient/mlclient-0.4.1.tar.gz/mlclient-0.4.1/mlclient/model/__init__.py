"""The ML Model package.

It contains modules with a corresponding Python representation of MarkLogic-related
data structures:

    * data
        The ML Data module.

This package exports the following classes:

    * DocumentType
        An enumeration class representing document types.
    * Document
        A class representing a single MarkLogic document.
    * JSONDocument
        A Document implementation representing a single MarkLogic JSON document.
    * XMLDocument
        A Document implementation representing a single MarkLogic XML document.
    * TextDocument
        A Document implementation representing a single MarkLogic TEXT document.
    * BinaryDocument
        A Document implementation representing a single MarkLogic BINARY document.
    * RawDocument
        A Document implementation representing a single MarkLogic document.
    * RawStringDocument
        A Document implementation representing a single MarkLogic document.
    * MetadataDocument
        A Document implementation representing a single MarkLogic document's metadata.
    * DocumentFactory
        A factory class instantiating a Document implementation classes.
    * MetadataFactory
        A factory class instantiating a Metadata class from a file.
    * Metadata
        A class representing MarkLogic's document metadata.
    * Permission:
        A class representing MarkLogic's document permission.
    * Mimetype
        A class representing mime type

Examples
--------
>>> from mlclient.model import Document, DocumentType, Metadata
"""
from .data import (
    BinaryDocument,
    Document,
    DocumentFactory,
    DocumentType,
    JSONDocument,
    Metadata,
    MetadataDocument,
    MetadataFactory,
    Mimetype,
    Permission,
    RawDocument,
    RawStringDocument,
    TextDocument,
    XMLDocument,
)

__all__ = [
    "MetadataFactory",
    "DocumentFactory",
    "Document",
    "RawDocument",
    "RawStringDocument",
    "MetadataDocument",
    "XMLDocument",
    "JSONDocument",
    "TextDocument",
    "BinaryDocument",
    "DocumentType",
    "Mimetype",
    "Metadata",
    "Permission",
]
