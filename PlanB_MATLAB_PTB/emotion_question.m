%PlanB: play the video on any player, then run the script
clc;clear;
rng('default')
rng shuffle
Base_dir=pwd;
Data_dir=[Base_dir '/Data'];
[ID age Cond]=getSubjInfo; %% get subj info
datafile=init_data_file(Data_dir, ID);  %% initialize the data files
Stimuli_dir=[Base_dir '/stimulus'];
%% design
% debug: change the filepath in 'emotion_ques.xlsx'
[~, ~, Design3]=xlsread('emotion_ques.xlsx','A2:C13');
Design=Design3;
Design=Design(randperm(size(Design,1))',:);
cd (Stimuli_dir)
rowNum=size(Design,1);
Design(:,4)=num2cell(1:rowNum);
for i = 1:rowNum
    Design{i,5}=imread(Design{i,2});
end
cd(Base_dir);
%% exp
%introduction
figure;set(gcf,'color',[255,255,255]/255);

axis off

for block=1:4
    intro1=imread('intro1.jpg');
    imshow(intro1);
    waitforbuttonpress;
for Trial=1:rowNum
    imshow=Design{Trial,5};
    pause(0.1);
    Keypressfcn
    tic
    [~,~,button]=ginput(1);
    RT=toc;
    Design(Trial,6)=button;
    Design(Trial,7)=RT;
    fprintf(datafile,'%d %d %d %d %d\n',Design(Trial,3:7));
end
    endintro=imread('endintro.png');
    imshow(endintro);
    waitforbuttonpress;
end
%% end
save([Data_dir '/' ID],'Design');
fclose(datafile);%close the data file
close all
