# code to load PCA information about face pairs from a .mat file
# and render and save the corresponding face images
from IPython import get_ipython
import os
import numpy as np

#Clear all variables    
get_ipython().magic("reset -sf")

info_file = 'facepair_info_set_A.bin'

# need to create folder for images to be saved to: 
save_dir = 'pwd' + '\\facepair_images_set_A\\'

# following directory should be wherever BFM is installed,
# which can be downloaded from here: 
# https://faces.dmi.unibas.ch/bfm/index.php?nav=1-2&id=downloads
bfm_dir = 'D:\HOME\coding\MATLAB\BaselFaceModel\matlab'

desired_size = 144; # width and height of square images

home = os.getcwd() #get current folder
np.fromfile(info_file) # loads as "p"


# navigate to BFM directory and load model
os.chdir(bfm_dir)

[model,msz] = load_model()   
rp = defrp; # default rendering parameters
rp.phi = 0; # front view

for i in range(1,np.size(p,1)):
    # get pca info
    pca1 = p[i,:,1]
    pca2 = p[i,:,2]
    
    # create faces in BFM and get mesh info     #STOPPED HERE
    mesh1  = coef2object(p(i,1:199,1)', model.shapeMU, model.shapePC, model.shapeEV ); # Convert into vertex space
    tex1 = coef2object(p(i,200:398,1)', model.texMU,  model.texPC,   model.texEV); # Convert into texture RGB space
    mesh2  = coef2object(p(i,1:199,2)', model.shapeMU, model.shapePC, model.shapeEV ); # Convert into vertex space
    tex2 = coef2object(p(i,200:398,2)', model.texMU,  model.texPC,   model.texEV); # Convert into texture RGB space
    
    # render and get image info
    h = figure(1);
    rp.width=desired_size;
    rp.height=desired_size;
    display_face(mesh1,tex1,model.tl,rp)
    set(gcf, 'Color', [ 1 1 1 ])
    f1 = getframe;
    img1 = f1.cdata;
    img1 = imresize(img1,[desired_size desired_size]);
    
    h = figure(2);
    rp.width=desired_size;
    rp.height=desired_size;
    display_face(mesh2,tex2,model.tl,rp)
    set(gcf, 'Color', [ 1 1 1 ])
    f2 = getframe;
    img2 = f2.cdata;
    img2 = imresize(img2,[desired_size desired_size]);
    
    # now save both images for this pair
    imwrite(img1, strcat(save_dir,'pair',num2str(i,'%06.f'),'face1.png'))
    imwrite(img2, strcat(save_dir,'pair',num2str(i,'%06.f'),'face2.png'))
    
    close all
end

cd(home)
