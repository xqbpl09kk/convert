import os

engine_path = "./webp/bin/cwebp"
export = ".webp"
support_suffix = "png jpg"



def convert(folder , file):
    file_path = folder + "/" + file
    is_dir = os.path.isdir(file_path)
    if is_dir:
        convert_folder(file_path)
    else:
        convert_file(file_path)
    # os.system("%s 1.png -o 1.webp" % (engine_path))


def convert_folder(folder_path):
    sub_files = os.listdir(folder_path)
    for file in sub_files:
        convert(folder_path , file)


def convert_file(file_path):
    file_path_split = file_path.split(".")
    path_len = len(file_path_split)
    if path_len != 3:
        return
    if file_path_split[2] not in support_suffix:
        return
    out_file = file_path_split[1] + export
    print("source file : " + file_path + " out file :" + out_file)

    # os.system("%s %s -o %s" % (engine_path, file_path, out_file))


convert("./source" , "")
