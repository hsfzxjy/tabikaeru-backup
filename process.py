#!/usr/bin/env python3

import time
import os
import shutil
import subprocess
import tempfile
from os import path
from glob import glob

from PIL import Image, ImageChops
import numpy as np


current_path = path.dirname(__file__)


def resolve(*parts):
    return path.join(current_path, *parts)


storage_dir = resolve('storage')


def get_database():

    db = []
    for fname in glob(storage_dir + '/*.png'):
        db.append(Image.open(fname))

    return db


if __name__ == '__main__':

    np.set_printoptions(threshold=np.nan)

    print('Loading database...')
    database = get_database()
    print('Database loaded.')

    archive_dir = resolve('archives')

    if not path.isdir(storage_dir):
        os.mkdir(storage_dir)

    for tar_file_name in glob(archive_dir + '/*.tgz'):

        temp_dir = tempfile.mkdtemp()
        print('Extracting', tar_file_name, '...')
        subprocess.run(['tar', 'xvzf', tar_file_name, '-C', temp_dir], stdout=subprocess.DEVNULL)
        print('Extracted', tar_file_name)

        picture_dir = temp_dir
        for fname in glob(picture_dir + '/album_*.sav'):

            new_name = fname.replace('.sav.back', '.bak.png').replace('.sav', '.sav.png')
            with open(fname, 'rb') as f, open(new_name, 'wb') as fout:
                f.seek(4)
                fout.write(f.read())

            image = Image.open(new_name)

            for stored_image in database:
                diff = ImageChops.difference(stored_image, image)
                box = diff.getbbox()

                if box is None:
                    size = 0
                else:
                    size = (box[2] - box[0]) * (box[3] - box[1])

                if size < 20:
                    print(new_name, 'duplicated')
                    break
            else:
                print('New photo detected:', new_name)
                database.append(image)

                shutil.copy(new_name, path.join(storage_dir, '{}.png'.format(int(time.time() * 100000))))

        shutil.rmtree(temp_dir)
        os.remove(tar_file_name)
