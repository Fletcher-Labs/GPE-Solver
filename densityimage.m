% Looking at n(x,y)
clear all; close all; clc;

%import xy data
filename='lattice.txt';
fileID=fopen(filename,'r');
formatSpec='%f %f %f';
size=[3 Inf];
data=fscanf(fileID,formatSpec,size).';

%parse
L=length(data);
l=sqrt(L);
xi=data(1,1);
xf=data(end,1);
x=linspace(xi,xf,l);
y=x;
density=reshape(data(:,3),[l,l]);

%plot
surf(x,y,density)
xlabel('x'), ylabel('y'), zlabel('density')
title(filename(1:end-4))