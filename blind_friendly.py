from image_processing import online_image 
import matplotlib.pyplot as plt
from daltonize import daltonize

i = 2
url = f"http://ty-ty.fr/assets/img/{i}.jpg"

def blind_friendly(url, output_name):
    # Image loading
    online_img = online_image(url)  # Changed variable name to avoid conflict
    preprocessed_image = online_img.preprocess()

    # Image processing to blind friendly
    fig, ax = plt.subplots()
    ax.imshow(preprocessed_image)
    ax.axis('off') 
    daltonized_fig = daltonize.daltonize_mpl(fig, copy=True)
    daltonized_fig.savefig(f"{output_name}.png", bbox_inches='tight', pad_inches=0)

    return "Image enregistrée !"

blind_friendly(url, "image_2")