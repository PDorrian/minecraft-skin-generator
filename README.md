# Minecraft Skin Generation
This is a quick and dirty method of generating valid Minecraft skins from random noise.

## Usage
1. Download the skins folder.
2. Run `python preprocess_crop_skins.py`
3. Wait for the image to crop.
4. Open `main.ipynb`.
5. Run the models.
6. Open Minecraft and enjoy your new skin!

## Dataset
### Description of Chosen Dataset
The chosen dataset is 960,000 player skins from the video game Minecraft. The appearance of a Minecraft player's avatar is determined by a 64x64 RGBA image which maps to a 3D player model. The upper half of the image is the base player skin and the bottom half is an optional second layer, which allows a layer of depth to be added to the model. I chose to crop the skins so that only the top half is used, reducing the size of the image while losing very little detail as the optional second layer is seldom utilised anyway.

### How to Download Dataset
This dataset is made available by Reddit user u/SHA65536.

https://www.reddit.com/r/datasets/comments/cmccb8/minecraft_skins_image_dataset/

## Results
Overall the generated skins were not of particularly high quality, although I do believe there were high quality elements within. For example, the AE/VAE images had very clear structure to them but without detail and the GAN images had some highly detailed elements but little overall structure. I was surprised to see that the Auto-Encoder performed the best in image generation, as the VAE and GAN are more specialised for the task.

One idea that I would implement if I had more time would be to convert the images to HSV or a similar format. I think this would help reduce noise in the GAN as it appeared that sometimes the correct structure was there but the RGB colour channels simply weren't lining up. A loss function better designed for multichannel images such as SSIM may also be worth investigation.

### Auto-encoder
![Auto-encoder](https://github.com/PDorrian/minecraft-skin-generator/blob/main/figures/ae_generation.png)

### Variational Auto-encoder
![Variational auto-encoder](https://github.com/PDorrian/minecraft-skin-generator/blob/main/figures/vae_generation.png)

### Generative Adversarial Network
![Generative adversarial network](https://github.com/PDorrian/minecraft-skin-generator/blob/main/figures/gan_generation.png)

## Future Features
- Improve quality of generated skins.
- Better support for generating more human-like skins.
- Support for generating skins with custom patterns.
- Support for generating skins with custom gear.