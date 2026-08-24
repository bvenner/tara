I had this rough ML idea for how to turn 3d photos into a labeled 3d map that represents real world infrastructure and had a super rough first order idea.

So for starters you have a ton of 3d photos of a scene along with positional camera data. You take all of those photos and plug them into 2 models:

a A Joint embedding model for the photos.

b A gaussian splatt model.

Then you take the 2 pieces of data, you have for each pixel in your image,

An associator that break's out how a list of gaussian splats influence the color of a final pixel in an image.

A interpretabilikty relation showing how each pixel's values influence the final """meaning""" embedding vector, with the goal of associating each pixel with a """meaning vector"""

Then you just flow and average that meaning vector back to each blob, and the idea for this is that if you want to select the power lines you can just search for meaning blobs that are nearest and this should hopefully segment out individual objects, and hopefully all objects that are in a similar class

