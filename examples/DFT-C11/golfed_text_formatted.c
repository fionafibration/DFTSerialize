#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#define w(h)copysign(1,h)
#define R return
#define P pow
#define T typedef
T int D;T float I;struct _{I a;I b;};T struct _ F;D

                                  f(D p){                                               if(p                                          <1){R
                                 1;}else{R                                              p*f(p-                                      1);}}I u
                                (D s){I z=                                           0;for(D k=0                                   ;k<s;k++){
                                z+=P(-1,k)                                          *(f(6*k))/(                                    (P(f(k),3))
                                *(f(3*k)))                                          *(13591409                                      +545140134*
                                 k)/(P/**/                                         (640320,(3                                        *k)));}R P(
        (z*P(10005,.5                           )/(96715l      *44160)            ),-1);}I e(      D n){I j=2         ;for(D i=2      ;i<n;i++){
     j+=1/f(i);}R j;}I r        (I h,I g){      if(h>1||h  <-1){R-r(1/h,g         )+w(h)*g/2       ;}if(h==1||       h==-1){R g/       4;}I j=0;;
   for(D z=0;z<100;z++){j       +=P(-1,(I)      z)*(P(h,(2*(I)z+1))/(2*(I)       z+1));}R j          ;}F s(I n,I     g,I a[]){         if(n<-g/2||
  n>g/2){F j;if(n<0){j=s(n      +g,g,a);}       else{j=s(n-g,g,a);}I x=j.a;      I y=j.b;F            v={-x,-y};R   v;}I x=1,y          =0;for(D i
  =0;i<50;i++){I d=w(n);I       u=x,v=y;x=      u-(d*P(2,-i)*v);y=(d*P(2,-i      )*u)+v;n=n            -(d*a[i]);}I k=/****/            .607252935
  ;F V={x*k       ,y*k};R V     ;}I h(I a,      I b){I u,x;D v,  y;u=frexp(a    ,&v); *&x=              frexp(b,&y);I h=u*x             ;I j=v+y;R
  ldexp(h,j);}D    t(D s){D      k=0;while      (s>0){k++;        s>>=1;}R k    ;}D j(D e,                D h){if(e<10||h<              10){R e*h;
  }D y=(t(e)>t(h)?t(e):         t(h))/2;D       l=P(2,y);D         a=e/l;D b    =e%l;D c=h                 /l;D d=h%l;D u               =j(a,c);D
   v=j(b,d);D z=j(a+b,c+d       )-u-v;R u*      P(2,(y*2))        +(z*l)+v;}    I m(I a,I                   b){double x,                y,u,v;x=/*
    */modf(a,&y);u=modf(b,      &v);R h(x,      u)+h(y,u)+        h(x,v)+j(y    ,v);}F o(F                   a,F b){I x=                a.a,y=a.b;
      I u=b.a,v=b.b;F r={m(     x,u)-m(y,v      ),m(x,v)+m        (y,u)};R r     ;}F k(F p,                I g,I b,I a[])               {I q=P(b,p
 .a);F v=     s(p.b,g,a);F      r={v.a*q,v      .b*q};R r;        }void/***/     dark_magic              (I*c,size_t f,D l             ){I g=u(5);
 I b=e(30)        ;I a[50];     for(D i=0;      i<50;i++){        a[i]=r(P(2     ,-i),g);}/*            */for(D i=0;i<l;i++            ){I s[f/2]
 ;for(D j=0;j  <f;j+=2){F z     ={c[j],c[j      +1]};F x={        0,2};F v={      g*j*i/f,0}           ;s[j/2]=o(z,k(o(v,x),          g,b,a)).a;}
 I O=0;for(D j=0;j<f/2;j++)     {O+=s[j];}      putchar(0+        round(O/(f       /2)));}}D          main(){I c[  ]={1129,0.,        23.497200,
  22.2116,-179.723000000,-      157.50370,      7.80620000        ,20.79880,       4.2757000,-       116.59630,-    3.9410000,-      17.579200,
   51.585,-6.9775,51.585,       6.977500,-      3.9410000,        17.579200,        4.27570000,    116.5963000,      7.8062000,-    20.79880,-
      179.723,157.5037          ,23.4972,-      22.2116};D         l=13;/**/         dark_magic(   c,sizeof(c)        /sizeof(c[   0]),l);}//
