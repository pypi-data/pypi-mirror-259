"""The ML Data module.

It exports 5 classes:
    * DocumentType
        An enumeration class representing document types.
    * Document
        An abstract class representing a single MarkLogic document.
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
        A class representing mime type.
"""
from __future__ import annotations

import copy
import json
import logging
import re
import xml.etree.ElementTree as ElemTree
from abc import ABCMeta, abstractmethod
from enum import Enum
from pathlib import Path
from typing import Any, ClassVar, List, TextIO
from xml.dom import minidom

import xmltodict
from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class DocumentType(Enum):
    """An enumeration class representing document types."""

    XML: str = "xml"
    JSON: str = "json"
    BINARY: str = "binary"
    TEXT: str = "text"


class Document(metaclass=ABCMeta):
    """An abstract class representing a single MarkLogic document."""

    def __init__(
        self,
        uri: str | None = None,
        doc_type: DocumentType | None = DocumentType.XML,
        metadata: Metadata | None = None,
        temporal_collection: str | None = None,
    ):
        """Initialize Document instance.

        Parameters
        ----------
        uri : str
            A document URI
        doc_type : DocumentType | None
            A document type
        metadata : Metadata
            A document metadata
        temporal_collection : str | None
            The temporal colllection
        """
        self._uri = self._get_non_blank_uri(uri)
        self._doc_type = doc_type
        self._metadata = metadata
        self._temporal_collection = temporal_collection

    @classmethod
    def __subclasshook__(
        cls,
        subclass: Document,
    ):
        """Verify if a subclass implements all abstract methods.

        Parameters
        ----------
        subclass : Document
            A Document subclass

        Returns
        -------
        bool
            True if the subclass includes the content property
        """
        return (
            "content" in subclass.__dict__
            and not callable(subclass.content)
            and "content_bytes" in subclass.__dict__
            and not callable(subclass.content_bytes)
            and "content_string" in subclass.__dict__
            and not callable(subclass.content_string)
        )

    @property
    @abstractmethod
    def content(
        self,
    ) -> Any:
        """A document content.

        Returns
        -------
        Any
            A document's content
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def content_bytes(
        self,
    ) -> bytes:
        """A document content bytes.

        Returns
        -------
        bytes
            A document's content bytes
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def content_string(
        self,
    ) -> str:
        """A document content in string format.

        Returns
        -------
        str
            A document's content in string format
        """
        raise NotImplementedError

    @property
    def uri(
        self,
    ) -> str:
        """A document URI."""
        return self._uri

    @property
    def doc_type(
        self,
    ) -> DocumentType | None:
        """A document type."""
        return self._doc_type

    @property
    def metadata(
        self,
    ) -> Metadata:
        """A document metadata."""
        return copy.copy(self._metadata)

    @property
    def temporal_collection(
        self,
    ) -> str | None:
        """The temporal collection."""
        return self._temporal_collection

    @staticmethod
    def _get_non_blank_uri(
        uri: str,
    ) -> str | None:
        """Return URI or None when blank."""
        return uri if uri is not None and not re.search("^\\s*$", uri) else None


class JSONDocument(Document):
    """A Document implementation representing a single MarkLogic JSON document.

    This implementation stores content in dict format.
    """

    def __init__(
        self,
        content: dict,
        uri: str | None = None,
        metadata: Metadata | None = None,
        temporal_collection: str | None = None,
    ):
        """Initialize JSONDocument instance.

        Parameters
        ----------
        content : dict
            A document content
        uri : str
            A document URI
        metadata : Metadata
            A document metadata
        temporal_collection : bool
            The temporal colllection
        """
        super().__init__(uri, DocumentType.JSON, metadata, temporal_collection)
        self._content = content

    @property
    def content(
        self,
    ) -> dict:
        """A document content.

        Returns
        -------
        dict
            A document's content
        """
        return self._content

    @property
    def content_bytes(
        self,
    ) -> bytes:
        """A document content bytes.

        Returns
        -------
        bytes
            A document's content bytes
        """
        return self.content_string.encode("utf-8")

    @property
    def content_string(
        self,
    ) -> str:
        """A document content in string format.

        Returns
        -------
        str
            A document's content in string format
        """
        return json.dumps(self._content)


class XMLDocument(Document):
    """A Document implementation representing a single MarkLogic XML document.

    This implementation stores content in ElemTree.ElementTree format.
    """

    def __init__(
        self,
        content: ElemTree.ElementTree,
        uri: str | None = None,
        metadata: Metadata | None = None,
        temporal_collection: str | None = None,
    ):
        """Initialize XMLDocument instance.

        Parameters
        ----------
        content : ElemTree.ElementTree
            A document content
        uri : str
            A document URI
        metadata : Metadata
            A document metadata
        temporal_collection : bool
            The temporal colllection
        """
        super().__init__(uri, DocumentType.XML, metadata, temporal_collection)
        self._content = content

    @property
    def content(
        self,
    ) -> ElemTree.ElementTree:
        """A document content.

        Returns
        -------
        ElemTree.ElementTree
            A document's content
        """
        return self._content

    @property
    def content_bytes(
        self,
    ) -> bytes:
        """A document content bytes.

        Returns
        -------
        bytes
            A document's content bytes
        """
        return ElemTree.tostring(
            self._content.getroot(),
            encoding="UTF-8",
            xml_declaration=True,
        ).replace(
            b"<?xml version='1.0' encoding='UTF-8'?>",
            b'<?xml version="1.0" encoding="UTF-8"?>',
        )

    @property
    def content_string(
        self,
    ) -> str:
        """A document content in string format.

        Returns
        -------
        str
            A document's content in string format
        """
        return self.content_bytes.decode("utf-8")


class TextDocument(Document):
    """A Document implementation representing a single MarkLogic TEXT document.

    This implementation stores content in a string format.
    """

    def __init__(
        self,
        content: str,
        uri: str | None = None,
        metadata: Metadata | None = None,
        temporal_collection: str | None = None,
    ):
        """Initialize TextDocument instance.

        Parameters
        ----------
        content : str
            A document content
        uri : str
            A document URI
        metadata : Metadata
            A document metadata
        temporal_collection : bool
            The temporal colllection
        """
        super().__init__(uri, DocumentType.TEXT, metadata, temporal_collection)
        self._content = content

    @property
    def content(
        self,
    ) -> str:
        """A document content.

        Returns
        -------
        str
            A document's content
        """
        return self._content

    @property
    def content_bytes(
        self,
    ) -> bytes:
        """A document content bytes.

        Returns
        -------
        bytes
            A document's content bytes
        """
        return self._content.encode("utf-8")

    @property
    def content_string(
        self,
    ) -> str:
        """A document content in string format.

        Returns
        -------
        str
            A document's content in string format
        """
        return self.content


class BinaryDocument(Document):
    """A Document implementation representing a single MarkLogic BINARY document.

    This implementation stores content in bytes format.
    """

    def __init__(
        self,
        content: bytes,
        uri: str | None = None,
        metadata: Metadata | None = None,
        temporal_collection: str | None = None,
    ):
        """Initialize BinaryDocument instance.

        Parameters
        ----------
        content : bytes
            A document content
        uri : str
            A document URI
        metadata : Metadata
            A document metadata
        temporal_collection : bool
            The temporal colllection
        """
        super().__init__(uri, DocumentType.BINARY, metadata, temporal_collection)
        self._content = content

    @property
    def content(
        self,
    ) -> bytes:
        """A document content.

        Returns
        -------
        bytes
            A document's content
        """
        return self._content

    @property
    def content_bytes(
        self,
    ) -> bytes:
        """A document content bytes.

        Returns
        -------
        bytes
            A document's content bytes
        """
        return self.content

    @property
    def content_string(
        self,
    ) -> str:
        """A document content bytes.

        Returns
        -------
        str
            A document's content bytes
        """
        return self._content.decode("utf-8")


class RawDocument(Document):
    """A Document implementation representing a single MarkLogic document.

    This implementation stores content in bytes format.
    """

    def __init__(
        self,
        content: bytes,
        uri: str | None = None,
        doc_type: DocumentType | None = DocumentType.XML,
        metadata: bytes | None = None,
        temporal_collection: str | None = None,
    ):
        """Initialize RawDocument instance.

        Parameters
        ----------
        content : bytes
            A document content
        uri : str
            A document URI
        doc_type : DocumentType | None
            A document type
        metadata : bytes
            A document metadata
        temporal_collection : bool
            The temporal colllection
        """
        super().__init__(uri, doc_type, metadata, temporal_collection)
        self._content = content

    @property
    def content(
        self,
    ) -> bytes:
        """A document content.

        Returns
        -------
        bytes
            A document's content
        """
        return self._content

    @property
    def content_bytes(
        self,
    ) -> bytes:
        """A document content bytes.

        Returns
        -------
        bytes
            A document's content bytes
        """
        return self.content

    @property
    def content_string(
        self,
    ) -> str:
        """A document content in string format.

        Returns
        -------
        str
            A document's content in string format
        """
        return self._content.decode("utf-8")


class RawStringDocument(Document):
    """A Document implementation representing a single MarkLogic document.

    This implementation stores content in a string format.
    """

    def __init__(
        self,
        content: str,
        uri: str | None = None,
        doc_type: DocumentType | None = DocumentType.XML,
        metadata: str | None = None,
        temporal_collection: str | None = None,
    ):
        """Initialize RawStringDocument instance.

        Parameters
        ----------
        content : str
            A document content
        uri : str
            A document URI
        doc_type : DocumentType | None
            A document type
        metadata : str
            A document metadata
        temporal_collection : bool
            The temporal colllection
        """
        super().__init__(uri, doc_type, metadata, temporal_collection)
        self._content = content

    @property
    def content(
        self,
    ) -> str:
        """A document content.

        Returns
        -------
        str
            A document's content
        """
        return self._content

    @property
    def content_bytes(
        self,
    ) -> bytes:
        """A document content bytes.

        Returns
        -------
        bytes
            A document's content bytes
        """
        return self._content.encode("utf-8")

    @property
    def content_string(
        self,
    ) -> str:
        """A document content in string format.

        Returns
        -------
        str
            A document's content in string format
        """
        return self.content


class MetadataDocument(Document):
    """A Document implementation representing a single MarkLogic document's metadata.

    This implementation does not store any content.
    """

    def __init__(
        self,
        uri: str,
        metadata: Metadata,
    ):
        """Initialize RawStringDocument instance.

        Parameters
        ----------
        uri : str
            A document URI
        metadata : Metadata
            A document metadata
        """
        super().__init__(uri, doc_type=None, metadata=metadata)

    @property
    def content(
        self,
    ) -> None:
        """A document content.

        Returns
        -------
        None
            A document's content
        """
        return

    @property
    def content_bytes(
        self,
    ) -> None:
        """A document content bytes.

        Returns
        -------
        None
            A document's content bytes
        """
        return

    @property
    def content_string(
        self,
    ) -> None:
        """A document content in string format.

        Returns
        -------
        None
            A document's content in string format
        """
        return


class DocumentFactory:
    """A factory class instantiating a Document implementation classes."""

    @classmethod
    def build_document(
        cls,
        content: ElemTree.Element | dict | str | bytes | None = None,
        doc_type: DocumentType | str | None = None,
        uri: str | None = None,
        metadata: Metadata | None = None,
        temporal_collection: str | None = None,
    ) -> Document:
        """Instantiate Document based on the document or content type.

        Parameters
        ----------
        content : ElemTree.Element | dict | str | bytes | None, default None
            A document content
        doc_type : DocumentType | str | None, default None
            A document type
        uri : str | None, default None
            A document URI
        metadata : Metadata | None, default None
            A document metadata
        temporal_collection : str | None, default None
            The temporal collection

        Returns
        -------
        Document
            A Document implementation instance
        """
        if isinstance(doc_type, str):
            doc_type = DocumentType(doc_type)

        if content is None and doc_type is None:
            return MetadataDocument(uri=uri, metadata=metadata)

        impl = cls._get_impl(content, doc_type)
        return impl(
            content=content,
            uri=uri,
            metadata=metadata,
            temporal_collection=temporal_collection,
        )

    @classmethod
    def build_raw_document(
        cls,
        content: bytes | str,
        doc_type: DocumentType | str,
        uri: str | None = None,
        metadata: bytes | str | None = None,
        temporal_collection: str | None = None,
    ) -> Document:
        """Instantiate Document based on the document type.

        Parameters
        ----------
        content : bytes | str
            A document content
        doc_type : DocumentType | str
            A document type
        uri : str | None, default None
            A document URI
        metadata : bytes | str | None, default None
            A document metadata
        temporal_collection : str | None, default None
            The temporal collection

        Returns
        -------
        Document
            A raw Document implementation instance

        Raises
        ------
        NotImplementedError
            If content type is neither bytes nor str
        """
        if isinstance(doc_type, str):
            doc_type = DocumentType(doc_type)

        if isinstance(content, bytes):
            impl = RawDocument
        elif isinstance(content, str):
            impl = RawStringDocument
        else:
            msg = "Raw document can store content only in [bytes] or [str] format!"
            raise NotImplementedError(msg)

        return impl(
            content=content,
            doc_type=doc_type,
            uri=uri,
            metadata=metadata,
            temporal_collection=temporal_collection,
        )

    @classmethod
    def _get_impl(
        cls,
        content: ElemTree.Element | dict | str | bytes | None,
        doc_type: DocumentType | None,
    ):
        """Return Document's implementation based on document type or content.

        Parameters
        ----------
        content : ElemTree.Element | dict | str | bytes | None
            A document content
        doc_type : DocumentType | None
            A document type

        Returns
        -------
        Document
            A Document's subclass reference
        """
        if doc_type == DocumentType.XML:
            impl = XMLDocument
        elif doc_type == DocumentType.JSON:
            impl = JSONDocument
        elif doc_type == DocumentType.TEXT:
            impl = TextDocument
        elif doc_type == DocumentType.BINARY:
            impl = BinaryDocument
        elif isinstance(content, ElemTree.Element):
            impl = XMLDocument
        elif isinstance(content, dict):
            impl = JSONDocument
        elif isinstance(content, str):
            impl = TextDocument
        elif isinstance(content, bytes):
            impl = BinaryDocument
        else:
            msg = (
                "Unsupported document type! "
                "Document types are: XML, JSON, TEXT, BINARY!"
            )
            raise NotImplementedError(msg)
        return impl


class MetadataFactory:
    """A factory class instantiating a Metadata class from a file."""

    _XML_MAPPINGS: ClassVar[dict] = {
        "collections": "collection",
        "permissions": "permission",
        "metadata-values": "metadata-value",
    }

    @classmethod
    def from_file(
        cls,
        file_path: str,
    ) -> Metadata:
        """Initialize a Metadata instance from a file.

        Parameters
        ----------
        file_path : str
            A metadata file path

        Returns
        -------
        Metadata
            A Metadata instance
        """
        file_path = Path(file_path)
        with file_path.open() as file:
            if file_path.suffix == ".json":
                return cls._from_json_file(file)
            return cls._from_xml_file(file)

    @classmethod
    def _from_json_file(
        cls,
        file: TextIO,
    ) -> Metadata:
        """Initialize a Metadata instance from a JSON file."""
        raw_metadata = json.load(file)
        if "permissions" in raw_metadata:
            permissions = []
            for permission in raw_metadata["permissions"]:
                role_name = permission["role-name"]
                capabilities = permission["capabilities"]
                permissions.append(Permission(role_name, set(capabilities)))
            raw_metadata["permissions"] = permissions
        if "metadataValues" in raw_metadata:
            raw_metadata["metadata_values"] = raw_metadata["metadataValues"]
            del raw_metadata["metadataValues"]
        return Metadata(**raw_metadata)

    @classmethod
    def _from_xml_file(
        cls,
        file: TextIO,
    ) -> Metadata:
        """Initialize a Metadata instance from an XML file."""
        raw_metadata = xmltodict.parse(
            file.read(),
            process_namespaces=True,
            namespaces={
                "http://marklogic.com/rest-api": None,
                "http://marklogic.com/xdmp/property": None,
            },
        ).get("metadata")
        for items, item in cls._XML_MAPPINGS.items():
            if items in raw_metadata:
                values = raw_metadata[items][item]
                if not isinstance(values, list):
                    values = [values]
                raw_metadata[items] = values
        if "permissions" in raw_metadata:
            permissions = []
            for permission in raw_metadata["permissions"]:
                role_name = permission["role-name"]
                capability = permission["capability"]
                existing_perm = next(
                    (p for p in permissions if p.role_name() == role_name),
                    None,
                )
                if existing_perm is None:
                    permissions.append(Permission(role_name, {capability}))
                else:
                    existing_perm.add_capability(capability)
            raw_metadata["permissions"] = permissions
        if "metadata-values" in raw_metadata:
            metadata_values = {}
            for metadata_value in raw_metadata["metadata-values"]:
                key = metadata_value["@key"]
                value = metadata_value["#text"]
                metadata_values[key] = value
            raw_metadata["metadata_values"] = metadata_values
            del raw_metadata["metadata-values"]
        if "quality" in raw_metadata:
            raw_metadata["quality"] = int(raw_metadata["quality"])
        return Metadata(**raw_metadata)


class Metadata:
    """A class representing MarkLogic's document metadata."""

    _COLLECTIONS_KEY: str = "collections"
    _PERMISSIONS_KEY: str = "permissions"
    _PROPERTIES_KEY: str = "properties"
    _QUALITY_KEY: str = "quality"
    _METADATA_VALUES_KEY: str = "metadataValues"

    _METADATA_TAG: str = "rapi:metadata"
    _COLLECTIONS_TAG: str = "rapi:collections"
    _COLLECTION_TAG: str = "rapi:collection"
    _PERMISSIONS_TAG: str = "rapi:permissions"
    _PERMISSION_TAG: str = "rapi:permission"
    _ROLE_NAME_TAG: str = "rapi:role-name"
    _CAPABILITY_TAG: str = "rapi:capability"
    _PROPERTIES_TAG: str = "prop:properties"
    _QUALITY_TAG: str = "rapi:quality"
    _METADATA_VALUES_TAG: str = "rapi:metadata-values"
    _METADATA_VALUE_TAG: str = "rapi:metadata-value"
    _KEY_ATTR: str = "key"

    _RAPI_NS_PREFIX: str = "xmlns:rapi"
    _PROP_NS_PREFIX: str = "xmlns:prop"
    _RAPI_NS_URI: str = "http://marklogic.com/rest-api"
    _PROP_NS_URI: str = "http://marklogic.com/xdmp/property"

    def __init__(
        self,
        collections: list | None = None,
        permissions: list | None = None,
        properties: dict | None = None,
        quality: int = 0,
        metadata_values: dict | None = None,
    ):
        """Initialize Metadata instance.

        Parameters
        ----------
        collections : list | None
            Document collections' list
        permissions : list | None
            Document permissions' list
        properties : dict | None
            Document's properties
        quality : int
            Document's quality
        metadata_values : dict | None
            Document's metadata values
        """
        self._collections = list(set(collections)) if collections else []
        self._permissions = self._get_clean_permissions(permissions)
        self._properties = self._get_clean_dict(properties)
        self._quality = quality
        self._metadata_values = self._get_clean_dict(metadata_values)

    def __eq__(
        self,
        other: Metadata,
    ) -> bool:
        """Verify if Metadata instances are equal.

        Parameters
        ----------
        other : Metadata
            A Metadata instance to compare

        Returns
        -------
        bool
            True if there's no difference between internal Metadata fields.
            Otherwise, False.
        """
        collections_diff = set(self._collections).difference(set(other.collections()))
        permissions_diff = set(self._permissions).difference(set(other.permissions()))
        return (
            isinstance(other, Metadata)
            and collections_diff == set()
            and permissions_diff == set()
            and self._properties == other.properties()
            and self._quality == other.quality()
            and self._metadata_values == other.metadata_values()
        )

    def __hash__(
        self,
    ) -> int:
        """Generate a hash value of a Metadata instance.

        Returns
        -------
        int
            A hash value generated using all internal Metadata fields.
        """
        items = self.collections()
        items.extend(self.permissions())
        items.append(self.quality())
        items.append(frozenset(self.properties().items()))
        items.append(frozenset(self.metadata_values().items()))
        return hash(tuple(items))

    def __copy__(
        self,
    ) -> Metadata:
        """Copy Metadata instance."""
        return Metadata(
            collections=self.collections(),
            permissions=self.permissions(),
            properties=self.properties(),
            quality=self.quality(),
            metadata_values=self.metadata_values(),
        )

    def collections(
        self,
    ) -> list:
        """Return document's collections."""
        return self._collections.copy()

    def permissions(
        self,
    ) -> list:
        """Return document's permissions."""
        return [copy.copy(perm) for perm in self._permissions]

    def properties(
        self,
    ) -> dict:
        """Return document's properties."""
        return self._properties.copy()

    def quality(
        self,
    ) -> int:
        """Return document's quality."""
        return self._quality

    def metadata_values(
        self,
    ) -> dict:
        """Return document's metadata values."""
        return self._metadata_values.copy()

    def set_quality(
        self,
        quality: int,
    ) -> bool:
        """Set document's quality.

        Parameters
        ----------
        quality : int
            A document's new quality

        Returns
        -------
        allow : bool
            True if value provided is an integer. Otherwise, False.
        """
        allow = isinstance(quality, int)
        if allow:
            self._quality = quality
        return allow

    def add_collection(
        self,
        collection: str,
    ) -> bool:
        """Assign a new collection to document.

        Parameters
        ----------
        collection : str
            A document's new collection

        Returns
        -------
        allow : bool
            True if the collection is non-blank value, and it does not appear already
            in document's collections. Otherwise, False.
        """
        allow = (
            collection is not None
            and not re.search("^\\s*$", collection)
            and collection not in self.collections()
        )
        if allow:
            self._collections.append(collection)
        return allow

    def add_permission(
        self,
        role_name: str,
        capability: str,
    ) -> bool:
        """Assign a new permission to document.

        Parameters
        ----------
        role_name : str
            a permission's role name
        capability : str
            a permission's capability

        Returns
        -------
        bool
            True if there's no such capability assigned to this role already, and it is
            a correct one. Otherwise, False.
        """
        allow = role_name is not None and capability is not None
        if allow:
            permission = self._get_permission_for_role(self._permissions, role_name)
            if permission is not None:
                return permission.add_capability(capability)

            self._permissions.append(Permission(role_name, {capability}))
            return True
        return allow

    def put_property(
        self,
        name: str,
        value: str,
    ):
        """Assign a new property to document.

        Parameters
        ----------
        name : str
            A property name
        value : str
            A property value
        """
        if name and value:
            self._properties[name] = value

    def put_metadata_value(
        self,
        name: str,
        value: str,
    ):
        """Assign a new metadata value to document.

        Parameters
        ----------
        name : str
            A metadata name
        value : str
            A metadata value
        """
        if name and value:
            self._metadata_values[name] = value

    def remove_collection(
        self,
        collection: str,
    ) -> bool:
        """Remove a collection from document.

        Parameters
        ----------
        collection : str
            A document's collection

        Returns
        -------
        allow : bool
            True if the collection is assigned to the document. Otherwise, False.
        """
        allow = collection is not None and collection in self.collections()
        if allow:
            self._collections.remove(collection)
        return allow

    def remove_permission(
        self,
        role_name: str,
        capability: str,
    ) -> bool:
        """Remove a permission from document.

        Parameters
        ----------
        role_name : str
            A permission's role name
        capability : str
            A permission's capability

        Returns
        -------
        bool
            True if the capability is assigned to the role for a document.
            Otherwise, False.
        """
        allow = role_name is not None and capability is not None
        if allow:
            permission = self._get_permission_for_role(self._permissions, role_name)
            allow = permission is not None
            if allow:
                success = permission.remove_capability(capability)
                if len(permission.capabilities()) == 0:
                    self._permissions.remove(permission)
                return success
            return allow
        return allow

    def remove_property(
        self,
        name: str,
    ) -> bool:
        """Remove a property from document.

        Parameters
        ----------
        name : str
            A property name

        Returns
        -------
        bool
            True if the document has a property with such name. Otherwise, False.
        """
        return self._properties.pop(name, None) is not None

    def remove_metadata_value(
        self,
        name: str,
    ) -> bool:
        """Remove a metadata value from document.

        Parameters
        ----------
        name : str
            A metadata name

        Returns
        -------
        bool
            True if the document has a metadata with such name. Otherwise, False.
        """
        return self._metadata_values.pop(name, None) is not None

    def to_json_string(
        self,
        indent: int | None = None,
    ) -> str:
        """Return a stringified JSON representation of the Metadata instance.

        Parameters
        ----------
        indent : int | None
            A number of spaces per indent level

        Returns
        -------
        str
            Metadata in a stringified JSON representation
        """
        return json.dumps(self.to_json(), indent=indent)

    def to_json(
        self,
    ) -> dict:
        """Return a JSON representation of the Metadata instance."""
        return {
            self._COLLECTIONS_KEY: self.collections(),
            self._PERMISSIONS_KEY: [p.to_json() for p in self._permissions],
            self._PROPERTIES_KEY: self.properties(),
            self._QUALITY_KEY: self.quality(),
            self._METADATA_VALUES_KEY: self._metadata_values,
        }

    def to_xml_string(
        self,
        indent: int | None = None,
    ) -> str:
        """Return a stringified XML representation of the Metadata instance.

        Parameters
        ----------
        indent : int | None
            A number of spaces per indent level

        Returns
        -------
        str
            Metadata in a stringified XML representation
        """
        metadata_xml = self.to_xml().getroot()
        if indent is None:
            metadata_str = ElemTree.tostring(
                metadata_xml,
                encoding="utf-8",
                method="xml",
                xml_declaration=True,
            )
        else:
            metadata_xml_string = ElemTree.tostring(metadata_xml)
            metadata_xml_minidom = minidom.parseString(metadata_xml_string)
            metadata_str = metadata_xml_minidom.toprettyxml(
                indent=" " * indent,
                encoding="utf-8",
            )
        return metadata_str.decode("ascii")

    def to_xml(
        self,
    ) -> ElemTree.ElementTree:
        """Return an XML representation of the Metadata instance."""
        attrs = {self._RAPI_NS_PREFIX: self._RAPI_NS_URI}
        root = ElemTree.Element(self._METADATA_TAG, attrib=attrs)

        self._to_xml_collections(root)
        self._to_xml_permissions(root)
        self._to_xml_properties(root)
        self._to_xml_quality(root)
        self._to_xml_metadata_values(root)
        return ElemTree.ElementTree(root)

    def _to_xml_collections(
        self,
        root: ElemTree.Element,
    ):
        """Add collections node to Metadata root."""
        parent = ElemTree.SubElement(root, self._COLLECTIONS_TAG)
        for collection in self.collections():
            child = ElemTree.SubElement(parent, self._COLLECTION_TAG)
            child.text = collection

    def _to_xml_permissions(
        self,
        root: ElemTree.Element,
    ):
        """Add permissions node to Metadata root."""
        permissions = ElemTree.SubElement(root, self._PERMISSIONS_TAG)
        for perm in self._permissions:
            for cap in perm.capabilities():
                permission = ElemTree.SubElement(permissions, self._PERMISSION_TAG)
                role_name = ElemTree.SubElement(permission, self._ROLE_NAME_TAG)
                capability = ElemTree.SubElement(permission, self._CAPABILITY_TAG)
                role_name.text = perm.role_name()
                capability.text = cap

    def _to_xml_properties(
        self,
        root: ElemTree.Element,
    ):
        """Add properties node to Metadata root."""
        attrs = {self._PROP_NS_PREFIX: self._PROP_NS_URI}
        properties = ElemTree.SubElement(root, self._PROPERTIES_TAG, attrib=attrs)
        for prop_name, prop_value in self.properties().items():
            property_ = ElemTree.SubElement(properties, prop_name)
            property_.text = prop_value

    def _to_xml_quality(
        self,
        root: ElemTree.Element,
    ):
        """Add quality node to Metadata root."""
        quality = ElemTree.SubElement(root, self._QUALITY_TAG)
        quality.text = str(self.quality())

    def _to_xml_metadata_values(
        self,
        root: ElemTree.Element,
    ):
        """Add metadata values node to Metadata root."""
        values = ElemTree.SubElement(root, self._METADATA_VALUES_TAG)
        for metadata_name, metadata_value in self.metadata_values().items():
            attrs = {self._KEY_ATTR: metadata_name}
            child = ElemTree.SubElement(values, self._METADATA_VALUE_TAG, attrib=attrs)
            child.text = metadata_value

    @classmethod
    def _get_clean_permissions(
        cls,
        source_permissions: list | None,
    ) -> list:
        """Return permissions list without duplicates.

        If source permissions are None, it returns an empty list.

        Parameters
        ----------
        source_permissions : list | None
            Source permissions to clean out.

        Returns
        -------
        permissions : list
            A clean permissions list
        """
        permissions = []
        if source_permissions is None:
            return permissions

        for permission in source_permissions:
            role_name = permission.role_name()
            existing_perm = cls._get_permission_for_role(permissions, role_name)
            if existing_perm is None:
                permissions.append(permission)
            else:
                logger.warning(
                    "Ignoring permission [%s]: role [%s] is already used in [%s]",
                    permission,
                    role_name,
                    existing_perm,
                )
        return permissions

    @staticmethod
    def _get_permission_for_role(
        permissions: list,
        role_name: str,
    ) -> Permission | None:
        """Return permissions assigned to the role provided.

        Parameters
        ----------
        permissions : list
            A permissions list
        role_name : str
            A role name

        Returns
        -------
        Permission | None
            A role's permission if exists. Otherwise, None.
        """
        return next(filter(lambda p: p.role_name() == role_name, permissions), None)

    @staticmethod
    def _get_clean_dict(
        source_dict: dict | None,
    ) -> dict:
        """Return a dictionary with stringified values and removed None values.

        If source dictionary are None, it returns an empty one.

        Parameters
        ----------
        source_dict : dict | None
            A source dictionary to clean out.

        Returns
        -------
        dict
            A clean dictionary
        """
        if not source_dict:
            return {}
        return {k: str(v) for k, v in source_dict.items() if v is not None}


class Permission:
    """A class representing MarkLogic's document permission."""

    READ: str = "read"
    INSERT: str = "insert"
    UPDATE: str = "update"
    UPDATE_NODE: str = "update-node"
    EXECUTE: str = "execute"

    _CAPABILITIES: ClassVar[tuple] = {READ, INSERT, UPDATE, UPDATE_NODE, EXECUTE}

    def __init__(
        self,
        role_name: str,
        capabilities: set,
    ):
        """Initialize a Permission instance.

        Parameters
        ----------
        role_name : str
            A role name
        capabilities : set
            Capabilities set
        """
        self._role_name = role_name
        self._capabilities = {cap for cap in capabilities if cap in self._CAPABILITIES}

    def __eq__(
        self,
        other: Permission,
    ) -> bool:
        """Verify if Permission instances are equal.

        Parameters
        ----------
        other : Permission
            A Permission instance to compare

        Returns
        -------
        bool
            True if there's no difference between internal Permission fields.
            Otherwise, False.
        """
        return (
            isinstance(other, Permission)
            and self._role_name == other._role_name
            and self._capabilities == other._capabilities
        )

    def __hash__(
        self,
    ) -> int:
        """Generate a hash value of a Permission instance.

        Returns
        -------
        int
            A hash value generated using all internal Permission fields.
        """
        items = list(self._capabilities)
        items.append(self._role_name)
        return hash(tuple(items))

    def __repr__(
        self,
    ) -> str:
        """Return a string representation of the Permission instance."""
        return (
            f"Permission("
            f"role_name='{self._role_name}', "
            f"capabilities={self._capabilities})"
        )

    def role_name(
        self,
    ) -> str:
        """Return permission's role name."""
        return self._role_name

    def capabilities(
        self,
    ) -> set:
        """Return permission's capabilities."""
        return self._capabilities.copy()

    def add_capability(
        self,
        capability: str,
    ) -> bool:
        """Assign a new capability to the role.

        Parameters
        ----------
        capability : str
            a permission's capability

        Returns
        -------
        allow : bool
            True if there's no such capability assigned to this role already, and it is
            a correct one. Otherwise, False.
        """
        allow = (
            capability is not None
            and capability in self._CAPABILITIES
            and capability not in self.capabilities()
        )
        if allow:
            self._capabilities.add(capability)
        return allow

    def remove_capability(
        self,
        capability: str,
    ) -> bool:
        """Remove a capability from the role.

        Parameters
        ----------
        capability : str
            a permission's capability

        Returns
        -------
        allow : bool
            True if the capability is assigned to the role.
            Otherwise, False.
        """
        allow = capability is not None and capability in self.capabilities()
        if allow:
            self._capabilities.remove(capability)
        return allow

    def to_json(
        self,
    ) -> dict:
        """Return a JSON representation of the Permission instance."""
        return {
            "role-name": self.role_name(),
            "capabilities": list(self.capabilities()),
        }


class Mimetype(BaseModel):
    """A class representing a mime type."""

    mime_type: str = Field(alias="mime-type")
    extensions: List[str]
    document_type: DocumentType = Field(alias="doc-type")
