%{
#include<stdio.h>
#include<stdlib.h>
char addSymbol(char,char,char);
void yyerror(char*);
void address();

struct set
{
	char op1;
	char operator;
	char op2;
}s;

%}

%union {char sym;}
%start str
%token <sym> letter number
%type  <sym> expr
%left '+''-'
%right '*''/'

%%
str:letter'='expr';' {addSymbol((char)$1,(char)$3,'=');}
	|expr';'
	
expr:expr'+'expr {$$=addSymbol((char)$1,(char)$3,'+');}
	|expr'-'expr {$$=addSymbol((char)$1,(char)$3,'-');}
	|expr'*'expr {$$=addSymbol((char)$1,(char)$3,'*');}
	|expr'/'expr {$$=addSymbol((char)$1,(char)$3,'/');}
	|letter		{$$=(char)$1}
	|number		{$$=(char)$1}
	
%%

char temp = 'A';

int ind = 0;
struct set sarr[50];

void yyerror(char* s)
{
	fprintf(stderr,"%s",s);
}

char addSymbol(char a,char b,char c)
{	
	printf("inside");
	sarr[ind].op1 = a;
	sarr[ind].op2 = b;
	sarr[ind].operator = c;
	ind++;
	temp++;
	return temp;
}

void address()
{
	//temp++;
	int count = 0;

	while(count<ind)
	{
	
	printf("%c = ",temp);
	if(isalpha(sarr[count].op1))
		printf("%c ",sarr[count].op1);
	else
		printf("%c ",temp);

	printf("%c ",sarr[count].operator);

	if(isalpha(sarr[count].op2))
		printf("%c ",sarr[count].op2);
	else
		printf("%c ",temp);

	temp++;
	count++;


	}


}

void main(void)
{
	yyparse();
	address();
}