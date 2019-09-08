
import os
from UnpackParser import UnpackParser
from bangmedia import unpack_pdf

class PdfUnpackParser(UnpackParser):
    extensions = []
    signatures = [
        (0, b'%PDF-')
    ]
    pretty_name = 'pdf'

    def parse_and_unpack(self, fileresult, scan_environment, offset, unpack_dir):
        return unpack_pdf(fileresult, scan_environment, offset, unpack_dir)
