import os
import rawpy
import imageio
import shutil
from Utils.logger import Logger
from Utils.config import INPUT_FOLDER

supported_extensions = ('.cr2', '.nef', '.arw', '.rw2', '.dng')
log = Logger()


class RawProcessor:
    def __init__(self, input_folder, temp_folder, output_folder):
        self.input_folder = input_folder
        self.temp_folder = temp_folder
        self.output_folder = output_folder
        self.logger = Logger()

        os.makedirs(self.input_folder, exist_ok=True)
        os.makedirs(self.temp_folder, exist_ok=True)
        os.makedirs(self.output_folder, exist_ok=True)

    def clean_temp_and_output(self):
        # neteja carpetes TEMP i OUTPUT
        for folder in [self.temp_folder, self.output_folder]:
            for f in os.listdir(folder):
                path = os.path.join(folder, f)
                try:
                    if os.path.isfile(path):
                        os.remove(path)
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                except Exception as e:
                    self.logger.log("Error netejant", path, result=str(e))
        print(f"🧹 Carpetes netejades.")

    def clean_temp(self):
        # neteja carpetes TEMP i OUTPUT
        for folder in [self.temp_folder]:
            for f in os.listdir(folder):
                path = os.path.join(folder, f)
                try:
                    if os.path.isfile(path):
                        os.remove(path)
                    elif os.path.isdir(path):
                        shutil.rmtree(path)
                except Exception as e:
                    self.logger.log("Error netejant", path, result=str(e))
        print(f"🧹 Carpetes netejades.")

    def raw_to_jpg(self, input_folder, temp_folder):
        self.raw_to_jpg_map = {}  # Fem el diccionari

        for filename in os.listdir(input_folder):
            if filename.lower().endswith((".cr2", ".cr3", ".nef", ".arw", ".dng")):

                raw_path = os.path.join(input_folder, filename)

                # Crear JPG temporal amb el mateix nom base
                jpg_name = os.path.splitext(filename)[0] + ".jpg"
                jpg_path = os.path.join(temp_folder, jpg_name)

                self.convert_raw_single(raw_path, jpg_path)

                # GUARDEM MAPPING RAW → JPG
                self.raw_to_jpg_map[jpg_name] = raw_path

                print(f"RAW → JPG: {filename} → {jpg_name}")
                log.log(f"RAW → JPG: {filename} → {jpg_name}")
                
    def convert_raw_single(self, raw_path, jpg_path):
        image = rawpy.imread(raw_path)
        rgb = image.postprocess()
        imageio.imwrite(jpg_path, rgb)

    def raw_files_found(self):
        """Retorna el nombre d'arxius RAW a la carpeta d'entrada"""
        count = 0
        for count in os.listdir(INPUT_FOLDER):
            
                count += 1
        return count