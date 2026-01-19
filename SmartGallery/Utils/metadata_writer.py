import subprocess
import os

def write_metadata_exiftool(raw_path, keywords, quality):
    """ Escriu metadades dins del RAW (contingut + qualitat).
        NO genera XMP. Usa exiftool per escriure directament.
        
        Args:
            raw_path: Camí al fitxer RAW
            keywords: Categoria (p.ex. "wing", "volcano")
            quality: Qualitat (p.ex. "bona", "acceptable", "dolenta")
    """
    
    if not os.path.exists(raw_path):
        print(f"❌ Fitxer no trobat: {raw_path}")
        return False
    
    try:
        # Preparem els dos valors: contingut (categoria) i qualitat
        content_str = ", ".join(keywords) if isinstance(keywords, list) else keywords
        quality_str = str(quality)
        
        # Rating segons qualitat
        if quality.lower() == "bona":
            rating = "5"
        elif quality.lower() == "millorable":
            rating = "3"
        elif quality.lower() == "dolenta":
            rating = "1"
        
        # Tags que escriurem DINS el RAW: XMP + IPTC + EXIF per millorar compatibilitat amb Windows
        tags = [
            # Escrivim explícitament el Title (Títol) i el Label (Etiqueta)
            f"-XMP:Title={content_str}",
            f"-Title={content_str}",
            # XMP
            f"-XMP:Subject={content_str}",
            f"-XMP:Description=Qualitat: {quality_str}",
            f"-XMP:Label={quality_str}",
            f"-XMP:Rating={rating}",
            # IPTC (Keywords i Caption-Abstract)
            f"-IPTC:Keywords={content_str}",
            f"-IPTC:Caption-Abstract=Qualitat: {quality_str}",
            # EXIF ImageDescription (alguns visualitzadors i Windows ho llegeixen)
            f"-ImageDescription=Categoria: {content_str} | Qualitat: {quality_str}",
            # també afegim Subject i Keywords per compatibilitat
            f"-Subject={content_str}"
        ]

        # Escriure directament dins del RAW sense generar XMP sidecar
        cmd = ["exiftool", "-overwrite_original", *tags, raw_path]
        print(f"✍ Escrivent metadades dins RAW: {os.path.basename(raw_path)}")
        print(f"   → Contingut: {content_str}")
        print(f"   → Qualitat: {quality_str}")
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✔ Metadades escrites correctament dins el RAW.")
            return True
        else:
            print(f"❌ Error amb exiftool: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ exiftool no està instal·lat o no es pot trobar al PATH")
        return False
    except Exception as e:
        print(f"❌ Error inespetat escrivint metadades: {e}")
        return False


def generate_xmp_sidecar(raw_path, keywords, quality):
    """ Genera un fitxer XMP sidecar (opcional, separat del RAW).
        Útil si vols tenir metadades externes sense modificar el RAW original.
        Args:
            raw_path: Camí al fitxer RAW
            keywords: Categoria
            quality: Qualitat
    """
    if not os.path.exists(raw_path):
        print(f"❌ Fitxer no trobat: {raw_path}")
        return False
    
    try:
        content_str = ", ".join(keywords) if isinstance(keywords, list) else keywords
        quality_str = str(quality)
        
        if quality.lower() == "bona":
            rating = "5"
        elif quality.lower() == "acceptable":
            rating = "3"
        else:
            rating = "1"
        
        xmp_tags = [
            f"-XMP:Subject={content_str}",
            f"-XMP:Description=Qualitat: {quality_str}",
            f"-XMP:Label={quality_str}",
            f"-XMP:Rating={rating}"
        ]

        # Generar XMP sidecar (fitxer separat)
        xmp_file = raw_path + ".xmp"
        cmd = ["exiftool", "-o", xmp_file, *xmp_tags, raw_path]
        print(f"📄 Creant XMP sidecar per: {os.path.basename(raw_path)}")
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✔ XMP creat: {xmp_file}")
            return True
        else:
            print(f"❌ Error generant XMP: {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ exiftool no està instal·lat")
        return False
    except Exception as e:
        print(f"❌ Error inespetat generant XMP: {e}")
        return False

