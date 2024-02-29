# Python-TAWNYAPI

## Documentation

- Find documentation under [docs.tawny.ai](https://docs.tawny.ai/api/pythonsdk.html#installation)
- More information about tawny.ai under [info@tawny.ai](mailto:info@tawny.ai)


#### Simple Example with OpenCV

```python
import cv2
from tawnyapi.vision.client import TawnyVisionApiClient
 
VIDEO_PATH = "<PATH TO YOUR VIDEO FILE>"
API_KEY = "<YOUR TAWNY API KEY>"
 
client = TawnyVisionApiClient(api_key=API_KEY)
cap = cv2.VideoCapture(VIDEO_PATH)
 
while True:
 
    ret, frame = cap.read()
    if not ret:
        break
 
    # Analyzing images already in memory:
    result = client.analyze_images(
        images=[frame],
        max_results=1,
        resize=None,
        features=[
            apitypes.ImageAnnotationFeatures.FACE_DETECTION,
            apitypes.ImageAnnotationFeatures.FACE_EMOTION,
            apitypes.ImageAnnotationFeatures.FACE_DESCRIPTOR,
            apitypes.ImageAnnotationFeatures.HEAD_POSE,
            apitypes.ImageAnnotationFeatures.FACE_LANDMARKS,
            apitypes.ImageAnnotationFeatures.ATTENTION,
            apitypes.ImageAnnotationFeatures.POSE
        ])
 
    print(result)
```