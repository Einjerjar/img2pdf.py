import glob
import os

from PIL import Image
from util import s2b


def gen_pdf(source, quality=80, optimize=True, out=None):
    # * Allowed file extensions
    img_exts = ['jpg', 'jpeg', 'png', 'webp', 'tiff']
    # * File list
    img_sources = []

    # TODO #1 optimize
    for i in img_exts:
        img_sources.extend(glob.glob(os.path.join(source, '*.{}'.format(i))))

    # * Sort images (will be removed when TODO #1 is done)
    img_sources.sort()

    # * Check for filecount, abort if 0
    print('Found {} files'.format(len(img_sources)))
    if len(img_sources) == 0:
        print('No files found, aborting')
        return

    # * Pillow images
    img_list = []

    # * Settings
    quality = quality
    optimize = optimize
    out_file = out

    # * Make sure an outfile is available
    if out_file is None:
        out_file = os.path.join(os.path.dirname(img_sources[0]), os.path.splitext(
            os.path.basename(img_sources[0]))[0] + '.pdf')
    elif os.path.splitext(out_file)[1].strip().lower() != '.pdf.':
        out_file = os.path.splitext(out_file)[0] + '.pdf'

    # * Load images to memory
    print('Preparing images')
    for i in img_sources:
        img = Image.open(i)
        img.convert('RGB')

        img_list.append(img)

    # * Get first image (for saving purposes)
    root = img_list.pop(0)

    # * Save file
    print('Saving to [{}] :: quality: {} :: optimized: {}'.format(out_file, quality, optimize))
    root.save(out_file, save_all=True, append_images=img_list, optimize=optimize, quality=quality)

    # * Done
    print('Saved pdf as [{}]'.format(out_file))


if __name__ == "__main__":
    # * Only import if ran directly
    import argparse

    d = {'quality': 80, 'optimize': True}

    parser = argparse.ArgumentParser(
        description='Convert group of images to pdf')
    parser.add_argument('source', type=str,
                        help='the folder containing the images')
    parser.add_argument('-o', '--out', metavar='PATH',
                        default=None, help='the file to output to [default: [sourcedir]/[first_file_name].pdf]')
    parser.add_argument('-q', '--quality', metavar='INT', type=int, default=d['quality'],
                        help='the final output quality [default: {}]'.format(d['quality']))
    parser.add_argument('-p', '--optimize', metavar='BOOL', type=s2b, default=d['optimize'],
                        help='whether to try and optimize the images [default: {}]'.format(d['optimize']))

    args = parser.parse_args()

    # * Do magic
    gen_pdf(args.source, quality=args.quality, optomize=args.optimize, out=args.out)
