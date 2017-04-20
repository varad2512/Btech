symptom(k,chills).

symptom(k,fever).

symptom(k,headache).

symptom(k,swollen_glands).



symptom(amit,fever).

symptom(amit,rash).

symptom(amit,headache).

symptom(amit,runny_nose).

symptom(dipen,runny_nose).

symptom(dipen,rash).

symptom(dipen,flu).

symptom(rahul,fever).

symptom(rahul,rash).

symptom(rahul,headache).

symptom(rahul,runny_nose).

hypothesis(Patient,measles):-

symptom(Patient,fever),

symptom(Patient,cough),

symptom(Patient,conjunctivitis),

symptom(Patient,rash).

hypothesis(Patient,german_measles) :-

symptom(Patient,fever),

symptom(Patient,headache),

symptom(Patient,runny_nose),

symptom(Patient,rash).

hypothesis(Patient,flu) :-

symptom(Patient,fever),

symptom(Patient,headache),

symptom(Patient,body_ache),

symptom(Patient,chills).



hypothesis(Patient,common_cold) :-

symptom(Patient,headache),

symptom(Patient,sneezing),

symptom(Patient,sore_throat),

symptom(Patient,chills),

symptom(Patient,runny_nose).

hypothesis(Patient,mumps) :-

symptom(Patient,fever),

symptom(Patient,swollen_glands).

hypothesis(Patient,chicken_pox) :-

symptom(Patient,fever),

symptom(Patient,rash),

symptom(Patient,body_ache),

symptom(Patient,chills).