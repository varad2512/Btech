%{
#include "y.tab.h"
%}

%%
[0-9]  {yylval.num = atoi(yytext); return identifier;}
[-+*/=;] {return yytext[0];}
[ \n\t]  ;
.       {ECHO,yyerror("Unexpected error");}
%%

int yywrap(void)
{
	return 1;
}