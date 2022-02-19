import numpy as np
import cv2


def rotateImage(rotateImage, angle):

    # Taking image height and width
    imgHeight = rotateImage.shape[0]
    imgWidth = rotateImage.shape[1]

    # Computing the centre x,y coordinates
    # of an image
    centreY = imgHeight/2
    centreX = imgWidth/2

    # Computing 2D rotation Matrix to rotate an image
    rotationMatrix = cv2.getRotationMatrix2D((centreY, centreX), angle, 1.0)

    # Now will take out sin and cos values from rotationMatrix
    # Also used numpy absolute function to make positive value
    cosOfRotationMatrix = np.abs(rotationMatrix[0][0])
    sinOfRotationMatrix = np.abs(rotationMatrix[0][1])

    # Now will compute new height & width of
    # an image so that we can use it in
    # warpAffine function to prevent cropping of image sides
    newImageHeight = int((imgHeight * sinOfRotationMatrix) +
                         (imgWidth * cosOfRotationMatrix))
    newImageWidth = int((imgHeight * cosOfRotationMatrix) +
                        (imgWidth * sinOfRotationMatrix))

    # After computing the new height & width of an image
    # we also need to update the values of rotation matrix
    rotationMatrix[0][2] += (newImageHeight/2) - centreY
    rotationMatrix[1][2] += (newImageWidth/2) - centreX

    # Now, we will perform actual image rotation
    rotatedImage = cv2.warpAffine(
        rotateImage, rotationMatrix, (newImageWidth, newImageHeight))

    return rotatedImage
