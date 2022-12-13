import numpy as np
from io import BytesIO
from PIL import Image
import PIL, requests
from io import BytesIO
from PIL import Image
import PIL, requests
# Import image from URL
URL = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
response = requests.get(URL)
# Read it as Image
I = Image.open(BytesIO(response.content))
# Optionally resize
I = I.resize([150,150])
# Convert to numpy array
arr = np.asarray(I)
# Optionaly Convert it back to an image and show
#im = PIL.Image.fromarray(np.uint8(arr))
#Image.Image.show(im)
print(arr) #each number is the rgb colour code at the position of the arraied image

"""
numpy.asarray(a, dtype=None, order=None, *, like=None)
Convert the input to an array.
"""