"""
Crop PDFs to half page
"""

import os
import sys

from typing import List

from loguru import logger
from PyPDF2 import PdfWriter, PdfReader


SRC = 'src4/Questions.pdf'
DST = 'src4/DP203_Questions.pdf'


def main() -> None:
    """Concatenate a list of pdf files into a single PDF."""
    output = PdfWriter()
    reader = PdfReader(SRC)
    for page in reader.pages:
        output.add_page(page)
        output.add_blank_page()
    logger.info(f'Writing to {DST}')
    with open(DST, 'wb') as f:
        output.write(f)
    return None


if __name__ == '__main__':
    main()
