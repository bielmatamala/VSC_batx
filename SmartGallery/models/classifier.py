# IA MobileNetV2 pre-trained model for image classification
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from keras.preprocessing import image
from keras.models import load_model
import numpy as np
import os

# Opcional: defineix aquí la ruta per defecte al model entrenat.
# IMPORTANT: usa una raw string (prefix `r`) o dobles \ per evitar escapes inesperats.
DEFAULT_MODEL_PATH = r"D:\visual situdio code general\SmartGallery\models\mobilenetv2_cifar10.h5"

class ImageClassifier:
    def __init__(self, model_path: str = None, target_size=(224, 224)):
        """Inicialitza el classificador.

        - If `model_path` is provided, loads the saved Keras model from that path.
        - Otherwise, loads MobileNetV2 pre-trained on ImageNet.
        `target_size` sets the image resize dimensions for prediction.
        """
        self.target_size = tuple(target_size)

        # Si no s'ha passat `model_path`, provem la constant de mòdul `DEFAULT_MODEL_PATH`
        if model_path is None and DEFAULT_MODEL_PATH:
            # comprova que el fitxer existeix
            if os.path.exists(DEFAULT_MODEL_PATH):
                model_path = DEFAULT_MODEL_PATH

        if model_path:
            print(f"Carregant model des de fitxer: {model_path} ...")
            self.model = load_model(model_path)
            self.is_custom = True
            # Default simple preprocessing for custom models: scale to [0,1]
            self.preprocess_fn = lambda x: x / 255.0
            print("Model carregat des del fitxer correctament.")
        else:
            print("Carregant model de classificació d'imatges MobileNetV2...")
            self.model = MobileNetV2(weights='imagenet')
            self.is_custom = False
            self.preprocess_fn = preprocess_input
            print("Model MobileNetV2 carregat correctament.")
    
    def predict_category(self, img_path):
        #Rep una imatge i retorna la categoria adient
        if not os.path.exists(img_path):
            raise FileNotFoundError(f"No s'ha trobat la imatge: {img_path}")
        
        # processament de la imatge
        img = image.load_img(img_path, target_size=self.target_size)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = self.preprocess_fn(x)

        #predicció
        preds = self.model.predict(x)

        if not self.is_custom:
            # decode_predictions funciona només per models entrenats sobre ImageNet
            decoded = decode_predictions(preds, top=1)[0][0]
            category = decoded[1]
            confidence = float(decoded[2])
            print(f"Prediccio: {category}, amb una confiança de {confidence:.2%}")
            return category, confidence
        else:
            # Per models personalitzats retornem la classe (índex) i la probabilitat
            if preds.ndim == 2:
                idx = int(np.argmax(preds[0]))
                confidence = float(np.max(preds[0]))
                
                # Carregar etiquetes si existeix un fitxer class_labels.txt
                class_labels_path = os.path.join(os.path.dirname(__file__), "class_labels.txt")
                if os.path.exists(class_labels_path):
                    try:
                        with open(class_labels_path, "r") as f:
                            labels = [line.strip() for line in f.readlines()]
                        if idx < len(labels):
                            category = labels[idx]  # Agafar el nom en lloc del número
                        else:
                            category = f"class_{idx}"  # Fallback si l'índex està fora de rang
                    except Exception as e:
                        print(f"⚠️ Error llegint etiquetes: {e}")
                        category = str(idx)
                else:
                    # Si no hi ha fitxer, retornar l'índex com a string
                    category = str(idx)
                
                print(f"Prediccio (model personalitzat): {category} (índex {idx}), probabilitat {confidence:.2%}")
                return category, confidence
            else:
                # Si la sortida té una forma inesperada, retornem la matriu de prediccions
                print("Prediccio retornada com a matriu (format no estàndard per a classificació).")
                return preds, None