#!/usr/bin/python3

from PIL import Image
import numpy as np
import os
import random

# get path
dirname = os.path.dirname(os.path.abspath(__file__))

# set final dimensions
dimensions = 480, 480

# preset background color options
backgrounds = [(128, 197, 204), (242, 212, 73), (161, 182, 248),
            (134, 226, 241), (247, 177, 22), (104, 205, 58), 
            (240, 232, 205), (253, 202, 162), (252, 169, 133),
            (255, 237, 81), (191, 228, 118), (133, 202, 93),
            (181, 225, 172), (140, 210, 144), (134, 207, 190),
            (72, 181, 163), (143, 206, 223), (111, 183, 214),
            (148, 168, 208), (117, 137, 191), (193, 179, 215),
            (165, 137, 193), (251, 182, 209), (249, 140, 182)
]

# keep track of which images have red eyes, poop, fart, santa hats, leprechaun hats, traffic cone, fire, mask
tracker = {}
tracker['redeye'], tracker['poop'], tracker['fart'], tracker['santa'], tracker['leprechaun'], tracker['cone'], tracker['fire'], tracker['mask'], tracker['candycane'], tracker['rotate'] = ({} for _ in range(10))
tracker['redeye']['list'], tracker['poop']['list'], tracker['fart']['list'], tracker['santa']['list'], tracker['leprechaun']['list'], tracker['cone']['list'], tracker['fire']['list'], tracker['mask']['list'], tracker['candycane']['list'], tracker['rotate']['list'] = ([] for _ in range(10))

# keep track of percentages for each item tracked (note this is not set here, but further down in the code)
tracker['redeye']['percent'] = 0.5
tracker['fart']['percent'] = 2.5
tracker['poop']['percent'] = 2.5
tracker['santa']['percent'] = 2.9
tracker['leprechaun']['percent'] = 2.9
tracker['cone']['percent'] = 2.9
tracker['fire']['percent'] = 2.5
tracker['mask']['percent'] = 2.5
tracker['candycane']['percent'] = 2.5
tracker['rotate']['percent'] = 0.25

# read in  hat choices
hatchoices = ['santahat', 'bluehair', 'brownhair', 'greenhair', 'littlebrownhair', 'littlegrayhair', 'redhair', 'redponytail', 'elvishair', 'cowboyhat', 'leprechaunhat', 'redcap', 'backwardsredcap', 'bluecap', 'trafficcone', 'horns1', 'horns2']
hats = {}
for hat in hatchoices:
    hatpath = dirname + "/parts/head/" + str(hat) + ".png"
    hats[hat] = Image.open(hatpath)

# read in butt choices
buttchoices = ['fart', 'poop']
butts = {}
for butt in buttchoices:
    buttpath = dirname + "/parts/butt/" + str(butt) + ".png"
    butts[butt] = Image.open(buttpath)

# read in mouth choices
mouthchoices = ['pipe', 'tongue', 'fire', 'mask', 'buckteeth']
mouths = {}
for mouth in mouthchoices:
    mouthpath = dirname + "/parts/mouth/" + str(mouth) + ".png"
    mouths[mouth] = Image.open(mouthpath)

# read in hand choices
handchoices = ['candycane', 'cane', 'teacup', 'beer']
hands = {}
for hand in handchoices:
    handpath = dirname + "/parts/hand/" + str(hand) + ".png"
    hands[hand] = Image.open(handpath)

# open file to write rare characteristics in ascending order
filename2 = dirname + '/all_feature_list_numerical_order.txt'
f2 = open(filename2, 'w')
f2.write("Filename\tName\tEye\tHead\tButt\tMouth\tHand\tFlip\tUpsideDown\n")

# set name
name = 'NFT-Rexx'

# set number of iterations (i.e. number of dinos)
num_iters = 2500
for x in range (0, num_iters):

# set seed
    epoch = 286 # current cardano epoch when feature added
    random.seed(x + epoch)

# print name to file
    f2.write("trex" + str(x) + ".png\t" + name + str(x) + "\t")

# select preset background color at random (equal weight)
###    bg_int = random.randrange(1, len(backgrounds) + 1, 1) - 1
###    b = backgrounds[bg_int]
# or select randomly generated background color at random
    b = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))


# select eye color (0.5% are red, 99.5% white)
    eye_int = random.randint(0, 1000)
    if eye_int <= 5:
        e = (255, 0, 0) # red
        f2.write("red\t")
    else:
        e = (255, 255, 255) # white
        f2.write("white\t")

# set dino color to black
    d = (0, 0, 0) # dino

# set basic trex image (b = background, d = dino)
    trex = [
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, e, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, d, b, b, b, b, b, b, b, b, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, d, b, b, b, b, b, b, b, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, d, d, b, b, b, b, d, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, d, d, d, b, b, d, d, d, d, d, d, d, d, d, b, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, d, d, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, d, b, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, b, b, b, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, b, b, b, b, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, d, d, b, b, b, d, d, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
        [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]
    ]

# make head choice
    hatchoices.append("none")
    hd = random.choices(hatchoices, weights = [5,10,10,10,10,10,10,10,10,7.5,5,10,10,10,5,7.5,7.5,25], k = 1)[0]
    hatchoices.pop()
    f2.write(hd + "\t")

# make butt choice
    buttchoices.append("none")
    bt = random.choices(buttchoices, weights = [2.5,2.5,95], k = 1)[0]
    buttchoices.pop()
    f2.write(bt + "\t")

# make mouth choice
    mouthchoices.append("none")
    mt = random.choices(mouthchoices, weights = [10,30,2.5,2.5,5,50], k = 1)[0]
    mouthchoices.pop()
    f2.write(mt + "\t")

# make hand choice
    handchoices.append("none")
    ha = random.choices(handchoices, weights = [2.5, 7.5, 10, 10, 70], k = 1)[0]
    handchoices.pop()
    f2.write(ha + "\t")

# convert pixels into array using numpy
    array = np.array(trex, dtype = np.uint8)

# use PIL to create image from array of pixels
    new_image = Image.fromarray(array).convert('RGBA')

# add in butt choice
    if bt == "none":
        pass
    else:
        new_image = Image.alpha_composite(new_image, butts[bt])

# add in mouth choice
    if mt == "none":
        pass
    else:
        new_image = Image.alpha_composite(new_image, mouths[mt])

# add in head choice
    if hd == "none":
        pass
    else:
        new_image = Image.alpha_composite(new_image, hats[hd])

# add in hand choice
    if ha == "none":
        pass
    else:
        new_image = Image.alpha_composite(new_image, hands[ha])

# choose whether to flip from right to left
    flip = random.choices([True, False], weights = [15, 85], k = 1)[0]
    new_image = new_image.transpose(method=Image.FLIP_LEFT_RIGHT) if flip == True else new_image
    f2.write(str(flip) + "\t")

# choose whether to rotate 180 degrees
    rotate = random.choices([True, False], weights = [2.5, 997.5], k = 1)[0]
    new_image = new_image.transpose(method=Image.ROTATE_180) if rotate == True else new_image
    f2.write(str(rotate) + "\n")

# update trackers as needed
    tracker['redeye']['list'].append(x) if e == (255, 0, 0) else None
    tracker['fart']['list'].append(x) if bt == 'fart' else None
    tracker['poop']['list'].append(x) if bt == 'poop' else None
    tracker['santa']['list'].append(x) if hd == 'santahat' else None
    tracker['leprechaun']['list'].append(x) if hd == 'leprechaunhat' else None
    tracker['cone']['list'].append(x) if hd == 'trafficcone' else None
    tracker['fire']['list'].append(x) if mt == 'fire' else None
    tracker['mask']['list'].append(x) if mt == 'mask' else None
    tracker['candycane']['list'].append(x) if ha == 'candycane' else None
    tracker['rotate']['list'].append(x) if rotate == True else None

# resize image to specified dimensions
    new_image = new_image.resize(dimensions)

# specify output path and file name
    imgname = dirname + '/image_output/' + 'trex' + str(x) + '.png'

# print output
    new_image.save(imgname)

# close f2 file
f2.close()

# print out which images have which tracker features as well as save to file
filename = dirname + '/rare_feature_stats.txt'
with open(filename, 'w') as f:
    for key in tracker:
        percent = round(len(tracker[key]['list'])/num_iters*100, 3)
        outline = str(key) + ' (' + str(tracker[key]['percent']) + '%) => ' + str(tracker[key]['list']) + ' ' + str(percent) + '%'
        print(outline)
        f.write(outline + "\n")
