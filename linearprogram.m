% problem
weight = [3,1,2;
          4,3,2;
          4,3,3;
];
yield = [4,5,7];
demand = [6,6,4];
c=4;


%linear programming
f = [3;1;2;4;3;2;4;3;3];
A = [1,1,1,0,0,0,0,0,0;
    0,0,0,1,1,1,0,0,0;
    0,0,0,0,0,0,1,1,1;
    -1,0,0,-1,0,0,-1,0,0;
    0,-1,0,0,-1,0,0,-1,0;
    0,0,-1,0,0,-1,0,0,-1;];
b = [4,5,7,-6,-6,-4];
lb = zeros(9,1);
ub = c * ones(9,1);
[x,fval,exitflag,output]= linprog(f,A,b,zeros(size(A)),zeros(size(b)),lb,ub);
X = horzcat(x(1:3),x(4:6),x(7:9));
