import pprint
import numpy as np
# def custom_reshape(data, num_images, num_channels, height, width):
#     """
#     Reshape a 1D array into a 4D array representing images.

#     Parameters:
#     - data: 1D array representing pixel values
#     - num_images: Number of images in the dataset
#     - num_channels: Number of color channels (e.g., 3 for RGB)
#     - height: Height of each image in pixels
#     - width: Width of each image in pixels

#     Returns:
#     - Reshaped 4D array
#     """
#     reshaped_data = []

#     # Iterate over the number of images
#     for i in range(num_images):
#         image = []

#         # Iterate over the number of color channels
#         for j in range(num_channels):
#             channel = []

#             # Iterate over the height of the image
#             for h in range(height):
#                 # Extract a slice of data representing a row in the image
#                 start_index = i * (num_channels * height * width) + j * (height * width) + h * width
#                 print(start_index)
#                 end_index = start_index + width
#                 print(end_index)
#                 channel.append(data[start_index:end_index])
                

#             # Append the channel to the image
#             image.append(channel)


#         # Append the image to the reshaped data
#         reshaped_data.append(image)
        

#     return reshaped_data

# Example usage (same as before):
image_data = list(range(1,181))  # Example 1D array with sequential numbers
image_array = np.array(image_data)
num_images=10
num_channels = 2
height = 3
width = 3

reshaped_data = image_array.reshape(num_images, num_channels, height, width)
transpose_data = reshaped_data.transpose(0, 2, 3, 1)

num_training = 5
train_data = transpose_data[:num_training]

pprint.pprint("Train Data[0]")
pprint.pprint(train_data[:1])
print(f'Shape of Train Data before Flatten: {train_data.shape}')


train_data = np.reshape(train_data, (train_data.shape[0], -1))
# does the same as before. depends, which one you want to use
# train_data = train_data.reshape(train_data.shape[0], train_data.shape[1]*train_data.shape[2]*train_data.shape[3])



print(f'Shape of Train Data after Flatten: {train_data.shape}')
pprint.pprint(train_data)


train_data = train_data.reshape(5, 3, 3, 2)
print(f'Shape of Train Data after restored: {train_data.shape}')
pprint.pprint(train_data)

train_data = np.reshape(train_data,(90,))
print(f'Shape of Train Data after restored: {train_data.shape}')
pprint.pprint(train_data)


no_of_images = 5
# pixel dimention: hxw
height = 3
width = 2
# no. of color channel
color_channel = 3 #RGB images

shape = no_of_images * height * width * color_channel

image_data = list(range(shape))
print(f'type: {type(image_data)} and shape/len: {len(image_data)}')

# print(image_array)
image_array = np.array(image_data)
print(f'type: {type(image_array)} and shape: {image_array.shape}')

image = image_array.reshape(no_of_images, color_channel, height, width)
print(f'type: {type(image)} and shape: {image.shape}')
flatten_image = np.reshape(image, (image.shape[0], -1))
print(f'type: {type(flatten_image)} and shape: {flatten_image.shape}')
# pprint.pprint(flatten_image)



original_shape = np.reshape(flatten_image, (flatten_image.size, ))
print(f'type: {type(original_shape)} and shape: {original_shape.shape}')

dists = np.sqrt(
                    np.sum(X**2, axis=1, keepdims=True) 
                        - 
                        
                        2*X.dot(self.X_train.T) 
                        
                        + 
                        
                        np.sum(self.X_train**2, axis=1)
                    
                )


# # shape = (5, 3, 3, 2)

# [
#     [
#         [
#             [ 1, 10], 
#             [ 2, 11], 
#             [ 3, 12]
#         ],

#         [
#             [ 4, 13], 
#             [ 5, 14], 
#             [ 6, 15]
#         ],

#         [
#             [ 7, 16],
#             [ 8, 17],
#             [ 9, 18]
#         ]
#     ],


#     [   
#         [[19, 28],
#          [20, 29],
#          [21, 30]],

#         [[22, 31],
#          [23, 32],
#          [24, 33]],

#         [[25, 34],
#          [26, 35],
#          [27, 36]]
#     ],


#     [    
#         [[37, 46],
#          [38, 47],
#          [39, 48]],

#         [[40, 49],
#          [41, 50],
#          [42, 51]],

#         [[43, 52],
#          [44, 53],
#          [45, 54]]
#     ],


#     [    
#         [[55, 64],
#          [56, 65],
#          [57, 66]],

#         [[58, 67],
#          [59, 68],
#          [60, 69]],

#         [[61, 70],
#          [62, 71],
#          [63, 72]]
#     ],


#     [    
#         [[73, 82],
#          [74, 83],
#          [75, 84]],

#         [[76, 85],
#          [77, 86],
#          [78, 87]],

#         [[79, 88],
#          [80, 89],
#          [81, 90]]
#     ]
    
# ]

# # shape = (5, 18)

# [
#     [   1, 10,  2, 11,  3, 12,  4, 13,  5, 14,  6, 15,  7, 16,  8, 17, 9, 18   ],
       
#     [   19, 28, 20, 29, 21, 30, 22, 31, 23, 32, 24, 33, 25, 34, 26, 35, 27, 36  ],
       
#     [   37, 46, 38, 47, 39, 48, 40, 49, 41, 50, 42, 51, 43, 52, 44, 53, 45, 54  ],
       
#     [   55, 64, 56, 65, 57, 66, 58, 67, 59, 68, 60, 69, 61, 70, 62, 71, 63, 72  ],
       
#     [   73, 82, 74, 83, 75, 84, 76, 85, 77, 86, 78, 87, 79, 88, 80, 89, 81, 90  ]
        
# ]