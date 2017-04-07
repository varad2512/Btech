%{
void yyerror(char* );
#include<stdio.h>
#include<stdlib.h>
%}

%union {int num;}
%start line
%token <num> identifier

%%

line:identifier'*'identifier';' {printf("%d",$1*$3);}
	|identifier'-'identifier';' {printf("%d",$1-$3);}

%%

void main(void)
{
	
	yyparse();
}

void yyerror(char* s)
{
	fprintf(stderr,"%s",s);
}