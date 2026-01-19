import os
import shutil
import json
import piexif
import traceback
import subprocess
from PIL import Image
from Utils.logger import Logger
log = Logger()

# Ruta a les traduccions
TRANSLATIONS_PATH = os.path.join(os.path.dirname(__file__), "../Utils/translations_extended.json")
with open(TRANSLATIONS_PATH, "r", encoding="utf-8") as f:
    TRANSLATIONS = json.load(f)


class ImageSorter:
    def __init__(self, output_folder):
        self.output_folder = output_folder

    def sort_image(self, img_path, category):
        """Mètode principal que s'encarrega de moure una imatge a la carpeta traduïda."""
        try:
            self.move_to_category(img_path, category)
        except Exception as e:
            print(f"❌ Error movent {img_path}: {e}")

    def move_to_category(self, original_path, category):
        """Traducció automàtica i còpia/moviment de la imatge al directori corresponent."""
        try:
            # Traduir al català si existeix (encara ho guardem per registre o usos futurs)
            category_ca = TRANSLATIONS.get(category, category)

            # L'usuari ha indicat que NO es toqui el nom del fitxer.
            # Per tant, movem el RAW original directament a la carpeta OUTPUT
            # arrel, mantenint el mateix nom de fitxer.

            base_name = os.path.basename(original_path)
            dst_path = os.path.join(self.output_folder, base_name)

            # Moure el fitxer (no copiar) per evitar duplicats i estalviar espai.
            # Si en algun moment vols conservar l'original, canvia a shutil.copy2.
            shutil.move(original_path, dst_path)

            print(f"📦 Mogut original a: {dst_path}")

        except Exception as e:
            print(f"❌ Error movent {original_path} → {category}: {e}")
    
    def moure_a_carp_fin(self, final_folder, saltar):
        """Mou tots els fitxers de les subcarpetes a la carpeta final.
        
        Args:
            final_folder: Ruta de la carpeta final on moure els fitxers
            saltar: 1 per moure només imatges, 0 per moure tot
        """
        try:
            os.makedirs(final_folder, exist_ok=True)
            
            # Llistar tot el que hi ha a output_folder
            for item_name in os.listdir(self.output_folder):
                src_path = os.path.join(self.output_folder, item_name)
                
                # Saltar la pròpia carpeta final
                if os.path.basename(src_path) == os.path.basename(final_folder):
                    print(f"⏭️ Saltant carpeta final: {item_name}")
                    continue
                
                # Si és una carpeta (categoria), moure tots els fitxers dins
                if os.path.isdir(src_path):
                    print(f"📁 Processant subcarpeta (per compatibilitat): {item_name}/")
                    for filename in os.listdir(src_path):
                        file_src = os.path.join(src_path, filename)
                        
                        # Si és fitxer
                        if os.path.isfile(file_src):
                            # Filtrar per extensions si saltar == 1
                            if saltar == 1:
                                if not filename.lower().endswith((".jpg", ".jpeg", ".png", ".cr2", ".nef", ".arw", ".dng", ".rw2")):
                                    print(f"⏭️ Saltant: {filename}")
                                    continue
                            
                            # Moure fitxer a carpeta final
                            dst_path = os.path.join(final_folder, filename)
                            shutil.move(file_src, dst_path)
                            print(f"📤 {filename} → carpeta final")
                    
                    # Netejar carpeta buida si està buit
                    if not os.listdir(src_path):
                        shutil.rmtree(src_path)
                        print(f"🗑️ Carpeta buida eliminada: {item_name}/")
                
                # Si és un fitxer directament a output_folder
                elif os.path.isfile(src_path):
                    if saltar == 1:
                        if not src_path.lower().endswith((".jpg", ".jpeg", ".png", ".cr2", ".nef", ".arw", ".dng", ".rw2")):
                            print(f"⏭️ Saltant: {item_name}")
                            continue
                    
                    dst_path = os.path.join(final_folder, item_name)
                    shutil.move(src_path, dst_path)
                    print(f"📤 {item_name} → carpeta final")
            
            print(f"✅ Tots els fitxers moguts a: {final_folder}")
            log.log("Moviment a carpeta final", "moure_a_carp_fin", result="✅ Completat")
        
        except Exception as e:
            print(f"❌ Error movent fitxers cap a carpeta final: {e}")
            log.log("Error carpeta final", "moure_a_carp_fin", result=str(e))


# ---------------  FUNCIÓ GLOBAL (Fora de Classe) -----------------

def escriure_exif(image_path, category, quality):
    """
    Escriu les metadades amb la categoria i qualitat detectades.
    Usa exiftool per escriure directament als RAW (CR2, NEF, etc).
    Per JPG/PNG: Escriu EXIF directament amb piexif.
    Compatible amb Lightroom Classic. Registra logs de cada operació.
    """
    try:
        description = f"Categoria: {category} | Qualitat: {quality}"
        file_ext = os.path.splitext(image_path)[1].lower()
        filename = os.path.basename(image_path)
        
        # RAW formats - usar exiftool per escriure directament
        if file_ext in ['.cr2', '.nef', '.arw', '.dng', '.rw2']:
            try:
                # Escriure descripcio i comentaris amb exiftool
                result = subprocess.run([
                    'exiftool',
                    f'-ImageDescription={description}',
                    f'-Comments={description}',
                    f'-Subject={category}',
                    '-overwrite_original',
                    image_path
                ], capture_output=True, check=True, text=True)
                
                print(f"📝 Metadades escrites al RAW: {filename} → {description}")
                log.log("Metadades RAW (exiftool)", filename, result=f"{category} | {quality} ✅")
            
            except FileNotFoundError:
                msg = "exiftool no està instal·lat"
                print(f"⚠️ {msg}")
                log.log("Metadades RAW ERROR", filename, result=msg)
            except Exception as e:
                print(f"⚠️ Error amb exiftool: {e}")
                log.log("Metadades RAW ERROR", filename, result=str(e))
        
        # JPG/PNG - escriure EXIF directament
        elif file_ext in ['.jpg', '.jpeg', '.png']:
            image = Image.open(image_path)

            # Carregar EXIF existent
            try:
                exif_dict = piexif.load(image.info.get("exif", b""))
            except Exception:
                exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}

            # 1. ImageDescription (visible a Lightroom)
            exif_dict["0th"][piexif.ImageIFD.ImageDescription] = description.encode("utf-8")
            
            # 2. UserComment a Exif
            user_comment = ("ASCII\x00" + description).encode("utf-8")
            exif_dict["Exif"][piexif.ExifIFD.UserComment] = user_comment
            
            # 3. Software
            exif_dict["0th"][piexif.ImageIFD.Software] = b"SmartGallery AI"

            # Guardar amb EXIF
            exif_bytes = piexif.dump(exif_dict)
            image.save(image_path, "jpeg", exif=exif_bytes, quality=95)

            print(f"📝 Metadades EXIF escrites: {filename} → {description}")
            log.log("Metadades JPG (EXIF)", filename, result=f"{category} | {quality} ✅")

    except Exception as e:
        print(f"⚠️ Error escrivint metadades a {image_path}: {e}")
        log.log("Metadades ERROR", os.path.basename(image_path), result=str(e))
        traceback.print_exc()
    
