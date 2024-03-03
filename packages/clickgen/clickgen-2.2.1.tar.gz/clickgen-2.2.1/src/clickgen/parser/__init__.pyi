from clickgen.parser.base import BaseParser
from clickgen.parser.png import MultiPNGParser as MultiPNGParser, SinglePNGParser as SinglePNGParser
from typing import List, Optional, Tuple, Union

__all__ = ['SinglePNGParser', 'MultiPNGParser', 'open_blob']

def open_blob(blob: Union[bytes, List[bytes]], hotspot: Tuple[int, int], sizes: Optional[List[int]] = None, delay: Optional[int] = None) -> BaseParser: ...
