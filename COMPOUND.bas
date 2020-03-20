DIM P, R, T, CI, A AS _INTEGER64
SCREEN 12
_FULLSCREEN
DIM B$
CLEAR
PRINT "P is for Principal"
PRINT "R is for Rate %"
PRINT "T is for Time"
PRINT "CI is for Compound Interest"
PRINT "A is for Amount"
PRINT "PA is for calulating Principal with Amount"
INPUT "ENTER CALULATE FOR:", B$
B$ = UCASE$(B$)
IF B$ = "P" THEN
    CLS
    INPUT "ENTER RATE %:", R
    INPUT "ENTER TIME IN YEARS:", T
    INPUT "ENTER CI:", CI
    CLS
    PRINT "PRINCIPAL:", CI / (((1 + (R / 100)) ^ T) - 1)
    PRINT "RATE %:", R
    PRINT "TIME:", T
    PRINT "COMPOUND INTEREST:", CI
    PRINT "AMOUNT:", (CI / (((1 + (R / 100)) ^ T) - 1)) + CI
END IF
IF B$ = "R" THEN
    CLS
    INPUT "ENTER PRINCIPAL:", P
    INPUT "ENTER TIME IN YEARS:", T
    INPUT "ENTER AMOUNT:", A
    CLS
    PRINT "PRINCIPAL:", P
    PRINT "RATE %:", ((A / P) ^ (1 / T) - 1) * 100; "%"
    PRINT "TIME:", T
    PRINT "COMPOUND INTEREST:", A - P
    PRINT "AMOUNT", A

END IF
IF B$ = "T" THEN
    CLS
    INPUT "ENTER RATE %:", R
    INPUT "ENTER PRINCIPAL:", P
    INPUT "ENTER AMOUNT:", A
    CLS
    PRINT "PRINCIPAL:", P
    PRINT "RATE %:", R
    PRINT "TIME:", LOG(A / P) / LOG(1 + R / 100)
    PRINT "COMPOUND INTEREST:", A - P
    PRINT "AMOUNT", A

END IF
IF B$ = "CI" THEN
    CLS
    INPUT "ENTER RATE %:", R
    INPUT "ENTER PRINCIPAL:", P
    INPUT "ENTER TIME IN YEARS:", T
    CLS
    PRINT "PRINCIPAL:", P
    PRINT "RATE %:", R
    PRINT "TIME:", T
    PRINT "COMPOUND INTEREST:", P * (((1 + R / 100) ^ T) - 1)
    PRINT "AMOUNT:", P * (1 + (((1 + R / 100) ^ T) - 1))

END IF
IF B$ = "A" THEN
    CLS
    INPUT "ENTER RATE %:", R
    INPUT "ENTER PRINCIPAL:", P
    INPUT "ENTER TIME IN YEARS:", T
    CLS
    PRINT "PRINCIPAL:", P
    PRINT "RATE %:", R
    PRINT "TIME:", T
    PRINT "COMPOUND INTEREST:", P * (((1 + R / 100) ^ T) - 1)
    PRINT "AMOUNT:", P * (1 + (((1 + R / 100) ^ T) - 1))

END IF
IF B$ = "PA" THEN
    CLS
    INPUT "ENTER AMOUNT:", A
    INPUT "ENTER RATE %:", R
    INPUT "ENTER TIME IN YEARS:", T
    CLS
    PRINT "PRINCIPAL:", A / ((1 + R / 100) ^ T)
    PRINT "RATE %:", R
    PRINT "TIME:", T
    PRINT "COMPOUND INTEREST:", A - A / ((1 + R / 100) ^ T)
    PRINT "AMOUNT:", A
END IF
CLEAR
SLEEP 50
SYSTEM






