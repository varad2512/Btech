father(sam,john).
mother(sam,alice).

parents(X,Y,Z):-
		father(Z,X),mother(Z,Y).

siblings(X,Y):-
		father(X,Z),father(Y,Z).

grandfather(X,Y):-
		father(X,Z),father(Z,Y).

grandmother(X,Y):-
		mother(X,Z),mother(Z,Y).
