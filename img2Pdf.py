import glob
import os

from PIL import Image

d = {'quality': 90, 'optimize': True}


def genPDF(source, quality=90, optimize=True, out=None):
    imgExts = ['jpg', 'jpeg', 'png', 'webp']
    imgSources = []

    for i in imgExts:
        imgSources.extend(glob.glob(os.path.join(source, '*.{}'.format(i))))

    print('Found {} files'.format(len(imgSources)))
    if (len(imgSources) == 0):
        print('No files found, aborting')
        return

    imgList = []

    quality = quality
    optimize = optimize

    outFile = out

    if outFile is None:
        outFile = os.path.join(os.path.dirname(imgSources[0]), os.path.splitext(
            os.path.basename(imgSources[0]))[0] + '.pdf')
    elif os.path.splitext(outFile)[1].strip().lower() != '.pdf.':
        outFile = os.path.splitext(outFile)[0] + '.pdf'

    print('Preparing images')
    for i in imgSources:
        img = Image.open(i)
        img.convert('RGB')

        imgList.append(img)

    root = imgList.pop(0)

    print('Saving to [{}] :: quality: {} :: optimized: {}'. format(
        outFile, quality, optimize))
    root.save(outFile, save_all=True, append_images=imgList,
              optimize=optimize, quality=quality)

    print('Saved pdf as [{}]'.format(outFile))


def s2b(v):
    if isinstance(v, bool):
        return v
    elif v.lower() in ['f', 'n', '0', 'false']:
        return False
    return True


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Convert group of images to pdf')
    parser.add_argument('source', type=str,
                        help='the folder containing the images')
    parser.add_argument('-o', '--out', metavar='PATH',
                        default=None, help='the file to output to [default: [sourcedir]/[first_file_name].pdf]')
    parser.add_argument('-q', '--quality', metavar='INT', type=int, default=d['quality'],
                        help='the final output quality [default: {}]'.format(d['quality']))
    parser.add_argument('-p', '--optimize', metavar='BOOL', type=s2b, default=d['optimize'],
                        help='wether to try and optimize the images [default: {}]'.format(d['optimize']))

    args = parser.parse_args()

    genPDF(args.source, args.quality, args.optimize, args.out)
