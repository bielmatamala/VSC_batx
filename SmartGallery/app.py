from models.image_quality import ImageQualityAnalyzer
from Utils.raw_handler import RawProcessor
from Utils.config import INPUT_FOLDER, TEMP_FOLDER, OUTPUT_FOLDER
from Utils.sorter import ImageSorter, escriure_exif
from Utils.logger import Logger
from models.classifier import ImageClassifier
from collections import Counter
from datetime import datetime
from Utils.sorter import escriure_exif
from Utils.metadata_writer import write_metadata_exiftool, generate_xmp_sidecar
import os
import traceback
log = Logger()
srt = ImageSorter(OUTPUT_FOLDER)
processor = RawProcessor(INPUT_FOLDER, TEMP_FOLDER, OUTPUT_FOLDER)
clf = ImageClassifier()
log = Logger()
resultats = []

log.log("=" * 150)
log.log("=" * 150)
log.log("Iniciant SmartGallery")

#Comprovar si les carpetes existeixen
try: 
    os.path.exists(INPUT_FOLDER)
    os.path.exists(OUTPUT_FOLDER)
    os.path.exists(TEMP_FOLDER)
    log.log("Carpetes d'entrada, sortida i temporal obertes correctament")
    print("\nCarpetes d'entrada, sortida i temporal obertes correctament\n")
    check = True

except Exception as e:
    log.log("Error en obrir les carpetes", e)
    print(f"Error en obrir les carpetes: {e}")
    check = False

opcio_raw = input("\nPer iniciar tot el porces 0 o ''\nPer només netejar carpetes 1 o no\nQuè vols fer? ")

# normalitzem l'entrada a string minúscula sense espais
opcio = opcio_raw.strip().lower()



try:
    if opcio in ("0", ""):
        processor.clean_temp_and_output()
        log.log("Carpetes temporals i de sortida netejades")
        processor.raw_to_jpg(INPUT_FOLDER, TEMP_FOLDER)
        log.log("Conversió RAW → JPG", result="Completada")
        resultats = []


        for filename in os.listdir(TEMP_FOLDER):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(TEMP_FOLDER, filename)
                print(f"\n🔍 Classificant {filename}...")

                try:
                    # Predicció amb la IA
                    categories, confidence = clf.predict_category(img_path)
                    print(f"📸 {filename} → {categories} ({confidence:.2f})")
                    log.log(f"📸 {filename} → {categories} ({confidence:.2f})")
                    
                    # Analizar qualitat
                    quality_analyzer = ImageQualityAnalyzer()
                    quality_result = quality_analyzer.analyze(img_path)
                    quality = quality_result.get("result", "desconeguda")
                    
                    # 1. TROBAR EL RAW ORIGINAL
                    raw_path = processor.raw_to_jpg_map.get(filename)
                    if not raw_path:
                        print(f"⚠️ No s'ha trobat RAW original per {filename}")
                        continue

                    # 2. ESCRIURE METADADES DINS EL RAW (contingut + qualitat, sense XMP)
                    ok = write_metadata_exiftool(raw_path, categories, quality)
                    if not ok:
                        # Registrar l'error en el log i crear un XMP sidecar com a fallback
                        msg = f"escriptura metadades FALLIDA per {os.path.basename(raw_path)}; creant XMP sidecar"
                        print(f"⚠️ {msg}")
                        log.log("Metadades RAW ERROR", os.path.basename(raw_path), result=msg)
                        # Intentem crear un XMP sidecar perquè Lightroom i altres gestors puguin llegir les etiquetes
                        try:
                            side_ok = generate_xmp_sidecar(raw_path, categories, quality)
                            if side_ok:
                                log.log("XMP sidecar creat (fallback)", os.path.basename(raw_path), result="✅")
                            else:
                                log.log("XMP sidecar ERROR (fallback)", os.path.basename(raw_path), result="❌")
                        except Exception as e:
                            log.log("XMP sidecar ERROR (exception)", os.path.basename(raw_path), result=str(e))

                    # 3. MOURE RAW A LA CARPETA DE CATEGORIA
                    category_principal = categories[0] if categories else "desconegut"
                    srt.sort_image(raw_path, category_principal)
                    
                    resultats.append(category_principal)
                    log.log("Classificació IA", filename, result=f"{categories} ({confidence:.2f}) | {quality}")
                    
                
                except Exception as e:
                    log.log("⚠️ Error classificant", filename, result=str(e))
                    print(f"❌ Error classificant {filename}: {e}")

        log.log("Procés complet", result="✅")
    
        if resultats:
            categories_mes_freq = [cat for cat, _ in Counter(resultats).most_common(3)]
            data_str = datetime.now().strftime("%y%m%d")
            nom_general = f"{data_str} Fotos {' '.join(categories_mes_freq)}"
            carpeta_general = os.path.join(OUTPUT_FOLDER, nom_general)
            os.makedirs(carpeta_general, exist_ok=True)
            print(f"📂 Carpeta general creada: {carpeta_general}")
            log.log("Carpeta general creada", result=nom_general)
            srt.moure_a_carp_fin(carpeta_general, 1)
            processor.clean_temp()

    elif opcio in ("1", "no"):
        print(f"❌ No s'ha iniciat el procés principal. Només netejar carpetes.")
        log.log("Procés principal no iniciat", result="Neteja carpetes")
        processor.clean_temp_and_output()
        log.log("Carpetes temporals i de sortida netejades", result="✅")

        log.log("Procés complet (Qualitat)", result="✅")

except Exception as e:
    log.log("❌ Error global", result=str(e))
    print(f"\n🚨 Error global:\n{traceback.format_exc()}")

finally:
    print("\n📘 SmartGallery finalitzat.")
