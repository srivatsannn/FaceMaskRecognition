def plot_example_images(plt):
    import os
    from tensorflow.keras.preprocessing.image import load_img, img_to_array 
    img_size = 48
    plt.figure(0, figsize=(12,20))
    ctr = 0

    for expression in os.listdir("dataset/"):
        for i in range(1,6):
            ctr += 1
            plt.subplot(7,5,ctr)
            img = load_img("dataset/" + expression + "/" +os.listdir("dataset/" + expression)[i], target_size=(img_size, img_size))
            plt.imshow(img, cmap="gray")

    plt.tight_layout()
    return plt
