from enum import Enum
from typing import Optional, Tuple

from rdflib import Graph
from rdflib.term import Node

_Triple = Tuple[Node, Node, Node]
_Quad = Tuple[Node, Node, Node, Graph]
_TriplePattern = Tuple[Optional[Node], Optional[Node], Optional[Node]]


class RDFSerialization(Enum):
    OxNTriple = "application/n-triples"
    OxTurtle = "text/turtle"
    OxRDFXML = "application/rdf+xml"
    OxTriG = "application/trig"
    OxNQuads = "application/n-quads"


def mime_types_mapping() -> dict[str, str]:
    return {
        "oxNTriples": "application/n-triples",
        "oxNQuads": "application/n-quads",
        "oxTurtle": "text/turtle",
        "oxTriG": "application/trig",
        "oxRdfXml": "application/rdf+xml",
    }


def get_mime_type(format: str) -> str:
    return mime_types_mapping().get(format, "text/turtle")