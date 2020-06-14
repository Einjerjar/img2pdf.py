import fitz

from PIL import Image


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
    pass


if __name__ == '__main__':
    parse_images('outTest/asd.pdf', output_folder='imgSet/b', quality=10)
