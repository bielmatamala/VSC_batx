import cv2
import numpy as np

class ImageQualityAnalyzer:
    def __init__(self, blur_threshold=100, brightness_low=50, brightness_high=200, contrast_threshold=30):
        self.blur_threshold = blur_threshold
        self.brightness_low = brightness_low
        self.brightness_high = brightness_high
        self.contrast_threshold = contrast_threshold

    def analyze(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            return {"result": "error", "reason": "no s'ha pogut llegir la imatge"}

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()
        blur_status = "borrosa" if sharpness < self.blur_threshold else "enfocada"

        brightness = np.mean(gray)
        if brightness < self.brightness_low:
            light_status = "fosca"
        elif brightness > self.brightness_high:
            light_status = "clara"
        else:
            light_status = "correcta"

        contrast = gray.std()
        contrast_status = "baix contrast" if contrast < self.contrast_threshold else "bo contrast"
        
        if blur_status == "enfocada" and light_status == "correcta" and contrast_status == "bo contrast":
            overall = "bona"
        elif light_status in ("fosca", "clara") or contrast_status in ("baix contrast", "alt contrast bo") and not(blur_status == "borrosa"):
            overall = "millorable"
        elif blur_status == "borrosa":
            overall = "dolenta"

        return {
            "result": overall,
            "nitidesa": round(sharpness, 2),
            "lluminositat": round(brightness, 2),
            "contrast": round(contrast, 2),
            "detalls": [blur_status, light_status, contrast_status]
        }