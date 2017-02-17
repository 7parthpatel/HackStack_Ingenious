%%clear all the variable and other data
clc,clear,clear all;                      %clear all variable,figures
%%read input from the image
if ~exist('gabor.mat','file')
    fprintf ('Creating Gabor Filters ...');
    create_gabor;
end
vid = videoinput('winvideo',1);
while (1==1)
    a=menu('ANPR Based Security System Using ALR',...
				'preview',...
                'Capture',...
                'Identify',...
				'Display Number',...
                'Exit');
    if (a == 1)
		preview(vid);
    end  
	
    if(a == 2)
        testpic = getsnapshot(vid);
		imwrite(testpic,'image1.jpg');
        imshow(testpic);
    end
	
    if (a == 3)
         ocr;
    end
    
    if (a == 4)
        winopen('text.txt');    %Open 'text.txt' file
    end
    
    if (a == 5)
        clear all;
        clc;
        close all;
        return;
    end    
end

