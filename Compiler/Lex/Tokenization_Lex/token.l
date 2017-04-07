%{
#include<stdio.h>
int chars,word,digit;
%}

%%
[a-zA-Z]        {printf("Character is %s\n",yytext);chars++;}
[0-9]+"."[0-9]? {printf("Digit is %s\n",yytext);digit++;}
[_a-zA-Z0-9]+   {printf("Identifier is %s\n",yytext); word++;}
"\n"                  ;
.                      ;
%%

int yywwrap(void)
{
	return 1;
}

void main(void)
{
yylex();
printf("%d %d %d",chars,word,digit);
}