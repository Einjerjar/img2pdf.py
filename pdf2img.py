import fitz

from PIL import Image
from util import s2b


def parse_images(pdf_source, quality=80, optimize=True, output_folder='/', preferred_extension='jpg'):
    o_file_format = '{}{:05d}.{}'
    valid_extensions = [
        'jpg',
        'png',
        'jpeg',
        'webm',
        'tiff',
    ]

    if preferred_extension not in valid_extensions:
        preferred_extension = valid_extensions[0]

    if output_folder[-1] != '/':
        output_folder += '/'

    pdf = fitz.open(pdf_source)

    for i in range(pdf.pageCount):
        print('Processing Page {} of {}'.format(i + 1, pdf.pageCount))

        # * Get Page
        page = pdf.loadPage(i)
        pix = page.getPixmap()

        # * File name
        o_name = o_file_format.format(output_folder, i, preferred_extension)

        # * Save Page
        a = Image.frombytes('RGB', [pix.width, pix.height], pix.samples)
        a.save(o_name, quality=quality, optimize=optimize)

        print(' >Saved image to {}'.format(o_name))


if __name__ == '__main__':
    # * Only import if ran directly
    import argparse

    d = {'quality': 80, 'optimize': True, 'ext': 'jpg'}

    parser = argparse.ArgumentParser(
        description='Convert pdf pages to images')
    parser.add_argument('source', type=str,
                        help='the source pdf file')
    parser.add_argument('-o', '--out', metavar='PATH',
                        default=None, help='the folder to output to [default: this_folder/####.jpg]')
    parser.add_argument('-q', '--quality', metavar='INT', type=int, default=d['quality'],
                        help='the image output quality [default: {}]'.format(d['quality']))
    parser.add_argument('-p', '--optimize', metavar='BOOL', type=s2b, default=d['optimize'],
                        help='whether to try and optimize the images [default: {}]'.format(d['optimize']))
    parser.add_argument('-e', '--extension', metavar='EXT', type=int, default=d['quality'],
                        help='preferred file extension'.format(d['ext']))

    args = parser.parse_args()

    # * Do magic
    parse_images(args.source, args.quality, args.optimize, args.out, args.extension)
