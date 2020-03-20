SCREEN 12
_FULLSCREEN
DIM P, R, T, SI, A AS _INTEGER64
DIM B$
CLEAR
PRINT "P is for Principal."
PRINT "R is for Rate %."
PRINT "T is for Time."
PRINT "SI is for Simple Interest."
PRINT "A is for Amount."
PRINT "PA is for calulating Principal with Amount."
INPUT "ENTER CALULATE FOR:", B$
B$ = UCASE$(B$)
IF B$ = "P" THEN
    CLS
    INPUT "ENTER RATE %:", R
    INPUT "ENTER TIME IN YEARS:", T
    INPUT "ENTER SI:", SI
    CLS
    PRINT "PRINCIPAL:", (100 * SI) / (T * R)
    PRINT "RATE %:", R
    PRINT "TIME:", T
    PRINT "SIMPLE INTEREST:", SI
    PRINT "AMOUNT", ((100 * SI) / (T * R)) + SI
END IF
IF B$ = "R" THEN
    CLS
    INPUT "ENTER PRINCIPAL:", P
    INPUT "ENTER TIME IN YEARS:", T
    INPUT "ENTER SI:", SI
    CLS
    PRINT "PRINCIPAL:", P
    PRINT "RATE %:", (100 * SI) / (T * P)
    PRINT "TIME:", T
    PRINT "SIMPLE INTEREST:", SI
    PRINT "AMOUNT", P + SI

END IF
IF B$ = "T" THEN
    CLS
    INPUT "ENTER RATE %:", R
    INPUT "ENTER PRINCIPAL:", P
    INPUT "ENTER SI:", SI
    CLS
    PRINT "PRINCIPAL:", P
    PRINT "RATE %:", R
    PRINT "TIME:", (100 * SI) / (P * R)
    PRINT "SIMPLE INTEREST:", SI
    PRINT "AMOUNT", P + SI

END IF
IF B$ = "SI" THEN
    CLS
    INPUT "ENTER RATE %:", R
    INPUT "ENTER PRINCIPAL:", P
    INPUT "ENTER TIME IN YEARS:", T
    CLS
    PRINT "PRINCIPAL:", P
    PRINT "RATE %:", R
    PRINT "TIME:", T
    PRINT "SIMPLE INTEREST:", P * R * T / 100
    PRINT "AMOUNT:", P + P * R * T / 100

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
    PRINT "SIMPLE INTEREST:", P * R * T / 100
    PRINT "AMOUNT:", P + P * R * T / 100

END IF
IF B$ = "PA" THEN
    CLS
    INPUT "ENTER AMOUNT:", A
    INPUT "ENTER RATE %:", R
    INPUT "ENTER TIME IN YEARS:", T
    CLS
    PRINT "PRINCIPAL:", A / (1 + R * T / 100)
    PRINT "RATE %:", R
    PRINT "TIME:", T
    PRINT "SIMPLE INTEREST:", A - (A / (1 + R * T / 100))
    PRINT "AMOUNT:", A
END IF
CLEAR
SLEEP 50
SYSTEM






