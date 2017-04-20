
%{
#include "y.tab.h"
extern char yyval;
%}

%%
[a-zA-Z]+ {yylval.sym = (char)yytext[0]; return letter;}
[0-9]+    {yylval.sym = (char)yytext[0]; return number;}
\n ;
.          {return yytext[0];}		
%%

int yywrap()
{
	return 1;
}
