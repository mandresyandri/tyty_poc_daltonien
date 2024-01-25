from image_processing import online_image 
import os
import matplotlib.pyplot as plt
from daltonize import daltonize

i = 1
url = f"http://ty-ty.fr/assets/img/{i}.jpg"

online_image = online_image(url)
preprocessed_image = online_image.preprocess()

fig = plt.imshow(preprocessed_image)


fig, ax = plt.subplots()
ax.imshow(preprocessed_image)
daltonized_fig = daltonize.daltonize_mpl(fig, copy=True)


daltonized_fig.savefig("output.png")