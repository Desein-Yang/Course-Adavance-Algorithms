% readxls
mark = xlsread('RandSampleOfStudentMarks.xls')

%analysis
m = mean(mark)
variance = var(mark)
standard = std(mark)
str1=['std = ',num2str(standard)]
str2=['mean = ',num2str(m)]
str3=['var = ',num2str(variance)]


%histogram
%[N,edges] = histcounts(mark)
figure
h1 = histogram(mark)
h1.BinWidth=5
h1.FaceColor=[0 0.5 0.5]
ylim([0,20])
text(5,12,str1)
text(5,11,str2)
text(5,10,str3)
title('Distribution of Student Marks')
xlabel('Mark bins')
ylabel('Student numbers')
savefig('h1.fig')


% random sample n=10
N = 1000
size = 10
SampleMean = zeros(1,N)

for i = 1:N
    sample = randsample(mark,size)
    SampleMean(i) = mean(sample)
end
str4=['std = ',num2str(std(SampleMean))]
str5=['mean = ',num2str(mean(SampleMean))]
figure
h2 = histogram(SampleMean)
text(60,70,str4)
text(60,80,str5)
h2.BinWidth=1
h2.FaceColor=[0 0.5 0.5]
title('Sample distribution of Student Marks(n=10)')
xlabel('Mark bins')
ylabel('Sample Mean')
savefig('h2.fig')

% random sample n=40
size = 40
for i = 1:N
    sample = randsample(mark,size)
    SampleMean(i) = mean(sample)
end

str6=['std = ',num2str(std(SampleMean))]
str7=['mean = ',num2str(mean(SampleMean))]
figure
h3 = histogram(SampleMean)
text(65,70,str6)
text(65,80,str7)
h3.BinWidth=1
h3.FaceColor=[0 0.5 0.5]
title('Sample distribution of Student Marks(n=40)')
xlabel('Mark bins')
ylabel('Sample Mean')
savefig('h3.fig')


% hypothesis test

u=64
t = (mean(mark) - u)/(std(mark)/sqrt(81))
df = 80







