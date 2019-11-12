% create large linear programming problem
m = 40;% produce cities
n = 25;% demand cities
weight = rand(m,n);% cost of wach line
yield = 100*rand(m,1);
d=rand(n,1);
demand=d*sum(yield)/sum(d);% output = input
c = 30;% max capability

% problem formulation
t0 = cputime;
A1 = zeros(m ,m * n);
A2 = [];
A3 = -1 * diag(ones(n,1));
j = 1;
f = [];
for i = 1:m
    A1(i,j:j+n-1)=1;% out < yield
    j = j + n;
    A2 = horzcat(A2,A3);% in > demand
    f = vertcat(f,weight(i,:)');
end
A = vertcat(A1,A2);
b = vertcat(yield,-1 * demand);
lb = zeros(m * n ,1);
ub = c * ones(m * n,1);


% large scale linear programming
[x,fval,exitflag,output]= linprog(f,A,b,zeros(size(A)),zeros(size(b)),lb,ub);
X = [];
for i = 1:m
    X = horzcat(X,x( (i-1) * n + 1: i * n ));
end
time = cputime - t0;
disp(['Time=',num2str(time)]);



            


