import os
import re
import shutil
from pathlib import Path

main_path = os.getcwd()
folder_name = 'my_folder'
folder_path = os.path.join(main_path, folder_name)
if os.path.exists(folder_path):
    print('The folder exists.')
else:
    print('The folder does not exist.')

extensions = {

    'video': ['mp4', 'mov', 'avi', 'mkv'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl', 'cda'],

    'images': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 'tiff'],

    'archives': ['zip', 'gz', 'tar'],

    'documents': ['pdf', 'txt', 'doc', 'docx', 'xlsx', 'pptx', 'djvu']

}


def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')


def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]

    # print(subfolder_paths)
    return subfolder_paths


def sort_files(main_path):
    for root, dirs, files in os.walk(main_path):
        for file_path in files:
            extension = file_path.split('.')[-1]
            file_name = file_path.split('\\')[-1]
            try:
                for dict_key_int in range(len(list(extensions.items()))):
                    if extension in list(extensions.items())[dict_key_int][1]:
                        path_obj = Path(root) / file_path

                        print(
                            f'Moving {file_name} in {list(extensions.items())[dict_key_int][0]} folder\n')
                        os.rename(
                            path_obj, f'{main_path}\\{list(extensions.items())[dict_key_int][0]}\\{file_name}')

            except:
                pass


def unpack(f, directory):
    directory = './archives'
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and filename.endswith('.zip'):

            shutil.unpack_archive(
                f, directory+f'{f[0:-len(path_obj.suffix)]}')
            os.remove(f)


def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)
    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name_path):

    t_name = name_path.translate(TRANS)
    t_name = re.sub(r'\W', '_', t_name)
    return t_name


for root, dirs, files in os.walk(main_path):
    for name in files:
        try:
            path_obj = Path(root) / name
            path_obj.rename(Path(
                root) / f"{normalize(path_obj.name[0:-len(path_obj.suffix)])}{path_obj.suffix}")
        except:
            print(f'{name} not a file')

    for dir in dirs:
        if not os.path.exists(str(extensions.keys())):
            try:
                path_obj = Path(root) / dir
                path_obj.rename(Path(
                    root) / f"{normalize(path_obj.name)}")
            except:
                print(f'{dir} - not a folder')

if __name__ == "__main__":
    create_folders_from_list(main_path, extensions)
    sort_files(main_path)
    remove_empty_folders(main_path)
    normalize(main_path)
    unpack(main_path, extensions)
