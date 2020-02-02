# Pixelated-Image
Lets pixelate our image!

- This code is created by Anilcan Bulut for fun.
It returns you a pixelated image of the provided input image.
There are some parameters like kernel size, image height and width.

- Kernel size: It should be an odd number like 3,5,7... 
Image dimentions: Both height and width should be dividable by kernel size. 


- Algorithm: We create a kernel at first. Let say 3 by 3. Then we find the center pixel of the kernel,
and create a new square that has smaller dimension than the original one. 

- After creating the square that contains center pixels with some for loops, we take only the center
pixel coordinates and their corresponding pixel value. 

- At the end, we loop through the original image and find which region of the image the current
pixel coordinate is. Then give the center pixel's pixel value to the current pixel.

Have fun with the code. It's slow I know, maybe I can change the algorithm to make it fast in the future.

![alt text](https://github.com/anilcanbulut/Pixelated-Image/blob/master/pixelated-image.png "How It Works?")
