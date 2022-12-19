# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
import kaitaistruct
from kaitaistruct import KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum
import zlib


if parse_version(kaitaistruct.__version__) < parse_version("0.9"):
    raise Exception(
        "Kaitai struct Python API incompatible: 0.9 or later is required, but you have %s" % (kaitaistruct.__version__)
    )


class Png(KaitaiStruct):
    class ColorType(Enum):
        greyscale = 0
        truecolor = 2
        indexed = 3
        greyscale_alpha = 4
        truecolor_alpha = 6

    class PhysUnit(Enum):
        unknown = 0
        meter = 1

    class CompressionMethods(Enum):
        zlib = 0

    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.magic = self._io.read_bytes(8)
        if not self.magic == b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A":
            raise kaitaistruct.ValidationNotEqualError(
                b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A", self.magic, self._io, "/seq/0"
            )
        self.ihdr_len = self._io.read_bytes(4)
        if not self.ihdr_len == b"\x00\x00\x00\x0D":
            raise kaitaistruct.ValidationNotEqualError(b"\x00\x00\x00\x0D", self.ihdr_len, self._io, "/seq/1")
        self.ihdr_type = self._io.read_bytes(4)
        if not self.ihdr_type == b"\x49\x48\x44\x52":
            raise kaitaistruct.ValidationNotEqualError(b"\x49\x48\x44\x52", self.ihdr_type, self._io, "/seq/2")
        self.ihdr = Png.IhdrChunk(self._io, self, self._root)
        self.ihdr_crc = self._io.read_bytes(4)
        self.chunks = []
        i = 0
        while True:
            _ = Png.Chunk(self._io, self, self._root)
            self.chunks.append(_)
            if (_.type == "IEND") or (self._io.is_eof()):
                break
            i += 1

    class Rgb(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.r = self._io.read_u1()
            self.g = self._io.read_u1()
            self.b = self._io.read_u1()

    class Chunk(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.len = self._io.read_u4be()
            self.type = (self._io.read_bytes(4)).decode("UTF-8")
            _on = self.type
            if _on == "iTXt":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.InternationalTextChunk(_io__raw_body, self, self._root)
            elif _on == "gAMA":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.GamaChunk(_io__raw_body, self, self._root)
            elif _on == "tIME":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.TimeChunk(_io__raw_body, self, self._root)
            elif _on == "PLTE":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.PlteChunk(_io__raw_body, self, self._root)
            elif _on == "bKGD":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.BkgdChunk(_io__raw_body, self, self._root)
            elif _on == "pHYs":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.PhysChunk(_io__raw_body, self, self._root)
            elif _on == "tEXt":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.TextChunk(_io__raw_body, self, self._root)
            elif _on == "cHRM":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.ChrmChunk(_io__raw_body, self, self._root)
            elif _on == "sRGB":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.SrgbChunk(_io__raw_body, self, self._root)
            elif _on == "zTXt":
                self._raw_body = self._io.read_bytes(self.len)
                _io__raw_body = KaitaiStream(BytesIO(self._raw_body))
                self.body = Png.CompressedTextChunk(_io__raw_body, self, self._root)
            else:
                self.body = self._io.read_bytes(self.len)
            self.crc = self._io.read_bytes(4)

    class BkgdIndexed(KaitaiStruct):
        """Background chunk for images with indexed palette."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.palette_index = self._io.read_u1()

    class Point(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.x_int = self._io.read_u4be()
            self.y_int = self._io.read_u4be()

        @property
        def x(self):
            if hasattr(self, "_m_x"):
                return self._m_x if hasattr(self, "_m_x") else None

            self._m_x = self.x_int / 100000.0
            return self._m_x if hasattr(self, "_m_x") else None

        @property
        def y(self):
            if hasattr(self, "_m_y"):
                return self._m_y if hasattr(self, "_m_y") else None

            self._m_y = self.y_int / 100000.0
            return self._m_y if hasattr(self, "_m_y") else None

    class BkgdGreyscale(KaitaiStruct):
        """Background chunk for greyscale images."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.value = self._io.read_u2be()

    class ChrmChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11cHRM
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.white_point = Png.Point(self._io, self, self._root)
            self.red = Png.Point(self._io, self, self._root)
            self.green = Png.Point(self._io, self, self._root)
            self.blue = Png.Point(self._io, self, self._root)

    class IhdrChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11IHDR
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.width = self._io.read_u4be()
            self.height = self._io.read_u4be()
            self.bit_depth = self._io.read_u1()
            self.color_type = KaitaiStream.resolve_enum(Png.ColorType, self._io.read_u1())
            self.compression_method = self._io.read_u1()
            self.filter_method = self._io.read_u1()
            self.interlace_method = self._io.read_u1()

    class PlteChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11PLTE
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.entries = []
            i = 0
            while not self._io.is_eof():
                self.entries.append(Png.Rgb(self._io, self, self._root))
                i += 1

    class SrgbChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11sRGB
        """

        class Intent(Enum):
            perceptual = 0
            relative_colorimetric = 1
            saturation = 2
            absolute_colorimetric = 3

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.render_intent = KaitaiStream.resolve_enum(Png.SrgbChunk.Intent, self._io.read_u1())

    class CompressedTextChunk(KaitaiStruct):
        """Compressed text chunk effectively allows to store key-value
        string pairs in PNG container, compressing "value" part (which
        can be quite lengthy) with zlib compression.

        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11zTXt
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.keyword = (self._io.read_bytes_term(0, False, True, True)).decode("UTF-8")
            self.compression_method = KaitaiStream.resolve_enum(Png.CompressionMethods, self._io.read_u1())
            self._raw_text_datastream = self._io.read_bytes_full()
            self.text_datastream = zlib.decompress(self._raw_text_datastream)

    class BkgdTruecolor(KaitaiStruct):
        """Background chunk for truecolor images."""

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.red = self._io.read_u2be()
            self.green = self._io.read_u2be()
            self.blue = self._io.read_u2be()

    class GamaChunk(KaitaiStruct):
        """
        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11gAMA
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.gamma_int = self._io.read_u4be()

        @property
        def gamma_ratio(self):
            if hasattr(self, "_m_gamma_ratio"):
                return self._m_gamma_ratio if hasattr(self, "_m_gamma_ratio") else None

            self._m_gamma_ratio = 100000.0 / self.gamma_int
            return self._m_gamma_ratio if hasattr(self, "_m_gamma_ratio") else None

    class BkgdChunk(KaitaiStruct):
        """Background chunk stores default background color to display this
        image against. Contents depend on `color_type` of the image.

        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11bKGD
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            _on = self._root.ihdr.color_type
            if _on == Png.ColorType.indexed:
                self.bkgd = Png.BkgdIndexed(self._io, self, self._root)
            elif _on == Png.ColorType.truecolor_alpha:
                self.bkgd = Png.BkgdTruecolor(self._io, self, self._root)
            elif _on == Png.ColorType.greyscale_alpha:
                self.bkgd = Png.BkgdGreyscale(self._io, self, self._root)
            elif _on == Png.ColorType.truecolor:
                self.bkgd = Png.BkgdTruecolor(self._io, self, self._root)
            elif _on == Png.ColorType.greyscale:
                self.bkgd = Png.BkgdGreyscale(self._io, self, self._root)

    class PhysChunk(KaitaiStruct):
        """ "Physical size" chunk stores data that allows to translate
        logical pixels into physical units (meters, etc) and vice-versa.

        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11pHYs
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.pixels_per_unit_x = self._io.read_u4be()
            self.pixels_per_unit_y = self._io.read_u4be()
            self.unit = KaitaiStream.resolve_enum(Png.PhysUnit, self._io.read_u1())

    class InternationalTextChunk(KaitaiStruct):
        """International text chunk effectively allows to store key-value string pairs in
        PNG container. Both "key" (keyword) and "value" (text) parts are
        given in pre-defined subset of iso8859-1 without control
        characters.

        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11iTXt
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.keyword = (self._io.read_bytes_term(0, False, True, True)).decode("UTF-8")
            self.compression_flag = self._io.read_u1()
            self.compression_method = KaitaiStream.resolve_enum(Png.CompressionMethods, self._io.read_u1())
            self.language_tag = (self._io.read_bytes_term(0, False, True, True)).decode("ASCII")
            self.translated_keyword = (self._io.read_bytes_term(0, False, True, True)).decode("UTF-8")
            self.text = (self._io.read_bytes_full()).decode("UTF-8")

    class TextChunk(KaitaiStruct):
        """Text chunk effectively allows to store key-value string pairs in
        PNG container. Both "key" (keyword) and "value" (text) parts are
        given in pre-defined subset of iso8859-1 without control
        characters.

        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11tEXt
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.keyword = (self._io.read_bytes_term(0, False, True, True)).decode("iso8859-1")
            self.text = (self._io.read_bytes_full()).decode("iso8859-1")

    class TimeChunk(KaitaiStruct):
        """Time chunk stores time stamp of last modification of this image,
        up to 1 second precision in UTC timezone.

        .. seealso::
           Source - https://www.w3.org/TR/PNG/#11tIME
        """

        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.year = self._io.read_u2be()
            self.month = self._io.read_u1()
            self.day = self._io.read_u1()
            self.hour = self._io.read_u1()
            self.minute = self._io.read_u1()
            self.second = self._io.read_u1()
