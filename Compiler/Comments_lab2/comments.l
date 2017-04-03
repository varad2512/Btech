
%{
#include<stdio.h>
int c=0;
%}
START "/*"
END "*/"
SIMPLE [^*]

COMPLEX "*"[^/]
%s newstate
%%
"//"(.*[ \t]*.*)*[\n]+    {c++; fprintf(yyout," ");}
{START}                    {yymore();BEGIN newstate;}
 <newstate>{SIMPLE}        {yymore();BEGIN newstate;}
 <newstate>{COMPLEX}      {yymore();BEGIN newstate;}

 <newstate>{END}  {c++;fprintf(yyout," ");BEGIN 0;}
%%

int yywrap()
{
return 1;
}

void main()
{//program to remove comment lines
yyin=fopen("file4","r");
yyout=fopen("fileout4","w");system("cat file4");
yylex();system("cat fileout4");
printf("no.of comments=%d",c);
fclose(yyin);
fclose(yyout);
}

