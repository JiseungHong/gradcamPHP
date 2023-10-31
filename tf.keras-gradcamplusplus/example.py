# Copyright 2020 Samson Woof

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

# %%
from utils import vgg16_mura_model, preprocess_image, show_imgwithheat
from gradcam import grad_cam, grad_cam_plus
import sys, os, imghdr

# %% load the model
model = vgg16_mura_model()
model.summary()

# %%
# img_path = './tf.keras-gradcamplusplus/images/4320878114_30a836d428_z.jpg'
if len(sys.argv) < 3:
    print("Usage: python python_script.py [img_path] [labels]")
    sys.exit(1)

img_path = sys.argv[1]
user_labels = []
for i, label in enumerate(sys.argv):
    if i < 2:
        continue
    user_labels.append(label)

# print(user_labels, type(user_labels))

path_of_imgs = []
preprocessed_imgs = []
for entry in os.listdir(img_path):
    path = os.path.join(img_path, entry)
    if os.path.isfile(path):
        if imghdr.what(path) in ['jpg', 'jpeg', 'png']:
            path_of_imgs.append(path)
            preprocessed_imgs.append(preprocess_image(path))
        else:
            print(f"{path}: Not an image file.")
            sys.exit(1)
    else:
        print(f"{path}: Not a valid file.")
        sys.exit(1)

# %% result of grad cam
# heatmap = grad_cam(model, img,
#                    label_name = ['WRIST', 'ELBOW', 'SHOULDER'],
#                    #category_id = 0,
#                    )
# show_imgwithheat(img_path, heatmap)

# %% result of grad cam++
for i, img in enumerate(preprocessed_imgs):
    heatmap_plus = grad_cam_plus(model, img,
                                label_name=user_labels)
    show_imgwithheat(path_of_imgs[i], heatmap_plus)