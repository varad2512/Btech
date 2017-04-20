yacc -d $1
flex $2
gcc lex.yy.c y.tab.c -ll -lm -o output
./output
