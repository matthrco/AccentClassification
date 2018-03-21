import os
import csv
import zipfile

path = "C:/Users/Matt/Documents/common-voice/"

training_files = {}

for root, dirs, files in os.walk(path):
        for file_ in files:
            if file_.endswith("train.csv"):
                with open(os.path.join(root, file_)) as csv_file:
                    csv_reader = csv.reader(csv_file)
                    next(csv_reader)
                    for row in csv_reader:
                        if row[6]:
                            training_files[row[0]] = row[6]

data_path = os.path.join(path, "data")

if not os.path.exists(data_path):
    os.makedirs(data_path)


def unzip_audio(path_to_zip):
    with open(os.path.join(path, path_to_zip), "rb") as zip_file:
        z = zipfile.ZipFile(zip_file)
        for name in z.namelist():
            if name in training_files:
                parts = os.path.split(name)
                with open(os.path.join(data_path, parts[0] + "-" + parts[1]), "wb") as f:
                    f.write(z.read(name))

unzip_audio("cv-valid-train.zip")
unzip_audio("cv-other-train.zip")
