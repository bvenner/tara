I had this rough ML idea for how to turn 3d photos into a labeled 3d map that represents real world infrastructure and had a super rough first order idea.

So for starters you have a ton of 3d photos of a scene along with positional camera data. You take all of those photos and plug them into 2 models:

a A Joint embedding model for the photos.

b A gaussian splatt model.

Then you take the 2 pieces of data, you have for each pixel in your image,

An associator that break's out how a list of gaussian splats influence the color of a final pixel in an image.

A interpretabilikty relation showing how each image is associate

