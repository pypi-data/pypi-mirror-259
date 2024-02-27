w  = 1e-5;
cl = 1e-6;

xl = 0.0;
xh = w;
yl = 0.0;
yh = w;
zl = 0.0;
zh = w;

Point(1) = {xl, yl, zl, cl};
Point(2) = {xh, yl, zl, cl};
Point(3) = {xh, yh, zl, cl};
Point(4) = {xl, yh, zl, cl};
Point(5) = {xl, yl, zh, cl};
Point(6) = {xh, yl, zh, cl};
Point(7) = {xh, yh, zh, cl};
Point(8) = {xl, yh, zh, cl};

Line(1) = {3,7};
Line(2) = {6,2};
Line(3) = {6,7};
Line(4) = {3,2};
Line(5) = {8,7};
Line(6) = {8,4};
Line(7) = {3,4};
Line(8) = {8,5};
Line(9) = {5,1};
Line(10) = {4,1};
Line(11) = {1,2};
Line(12) = {5,6};
Line Loop(13) = {1,-3,2,-4};
Plane Surface(14) = {13};
Line Loop(15) = {5,-3,-12,-8};
Plane Surface(16) = {15};
Line Loop(17) = {12,2,-11,-9};
Plane Surface(18) = {17};
Line Loop(19) = {11,-4,7,10};
Plane Surface(20) = {19};
Line Loop(21) = {7,-6,5,-1};
Plane Surface(22) = {21};
Line Loop(23) = {10,-9,-8,6};
Plane Surface(24) = {23};
Surface Loop(25) = {22,20,18,16,14,24};
Volume(26) = {25};
Physical Surface("top") = {20};
Physical Surface("bot") = {16};
Physical Volume("bulk") = {26};
