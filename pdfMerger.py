from glob import glob
from os import path
from PyPDF2 import PdfFileReader, PdfFileMerger


def merge_pdf(i_dir='', o_dir=None):
    """
    Merges pdf files inside a selected folder (current folder if not set)
    :param i_dir: the folder containing the pdfs to use
    :param o_dir: the file to save the output to (i_dir/[dirname].pdf if not set)
    :return:
    """

    files = None

    # For future : so we can pass list of stuff instead of just folders
    if type(i_dir) == 'list':
        files = i_dir
        if o_dir is None:
            o_dir = 'merge_output.pdf'

    # Does tha magic for the output file
    if o_dir is None:
        o_dir = i_dir
        if o_dir[-1:] == '/':
            o_dir = o_dir[:-1]
        o_dir = path.join(o_dir, '{}.pdf'.format(path.split(o_dir)[1]))
    elif path.splitext(o_dir)[1] != '.pdf':
        o_dir += '.pdf'

    # Prepares the i_dir for globbing
    i_dir = path.join(i_dir, '*.pdf')

    # Get list of pdf files in dir
    if files is None:
        files = glob(i_dir)

    # Create a PdfFileMerger Object
    merger = PdfFileMerger()

    # Append all the pdf files to the merger
    for i in range(len(files)):
        merger.append(PdfFileReader(files[i], 'rb'))

    # Save the pdf files
    merger.write(o_dir)


if __name__ == '__main__':
    # * Only import if ran directly
    import argparse

    parser = argparse.ArgumentParser(
        description='Merge a group of pdfs into one')
    parser.add_argument('source', type=str,
                        help='the folder containing the pdf files')
    parser.add_argument('-o', '--out', metavar='PATH',
                        default=None, help='the file to output to [default: [sourcedir]/[dirname].pdf]')

    args = parser.parse_args()

    # * Do magic
    merge_pdf(args.source, args.out)
