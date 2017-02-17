%final code for the ANPR BASED SECCURITY SYTEM USING ALR
%******ANPR*****SECURTIY SYSTEM ******ALR*****%
clc,close all;
%vid = videoinput('winvideo',1);    %input the video from webcam
%preview(vid);       %preview the webcam

%Parallel Port interfacing using parllel port
open = daqhwinfo('parallel');
DIO1 = digitalio('parallel','LPT1');
DIO2 = digitalio('parallel','LPT1');
outreg = addline(DIO1, 0:7, 0, 'out');
inreg = addline(DIO2, 0:4, 1, 'in');
putvalue(DIO1,253);       %initialize the parllel port
a=getvalue(DIO2);          %take input from parallel port

img = imread('image1.jpg');
img = rgb2gray(img);
level = graythresh(img);
img = im2bw(img,level);
imwrite('image1.jpg',img);
ocr;
