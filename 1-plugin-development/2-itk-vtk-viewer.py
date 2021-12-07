import numpy as np
from imjoy import api

async def setup():
    image_array = np.random.randint(0, 255, [10,10,10], dtype='uint8')
    viewer = await api.createWindow(
        src="https://oeway.github.io/itk-vtk-viewer/",
        fullscreen=True
    )
    await viewer.setImage(image_array)

api.export({"setup": setup})