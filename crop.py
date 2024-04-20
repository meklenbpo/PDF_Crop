"""
Crop PDFs to half page
"""

import os
import sys

from typing import List

from loguru import logger
from PyPDF2 import PdfWriter, PdfReader


SRC_DIR = 'src3/math_workbook_7/appendix'
DEST_FN = 'dst/maths7_appendix.pdf'


def collect_pdf_list(src_dir: str) -> List[str]:
    """Collect applicable pdfs in a directory."""
    pdf_list = os.listdir(src_dir)
    pdf_list = [x for x in pdf_list if x.endswith('.pdf')]
    pdf_list = [os.path.join(src_dir, x) for x in pdf_list]
    pdf_list.sort()
    return pdf_list


def concat_pdf_files(fn_list: List[str], dest_fn: str) -> None:
    """Concatenate a list of pdf files into a single PDF."""
    output = PdfWriter()
    for pdf_fn in fn_list:
        logger.debug(pdf_fn)
        reader = PdfReader(pdf_fn)
        page = reader.pages[0]
        page.cropbox.upper_left = (0, 0)
        page.cropbox.lower_right = (620, 792)
        output.add_page(page)
    logger.info(f'Writing to {dest_fn}')
    with open(dest_fn, 'wb') as f:
        output.write(f)
    return None


def main() -> int:
    """Run the script."""
    logger.info('Starting...')
    pdf_list = collect_pdf_list(SRC_DIR)
    concat_pdf_files(pdf_list, DEST_FN)
    logger.success('Done.')
    return 0


if __name__ == '__main__':
    main()
