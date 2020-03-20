SCREEN 12
_FULLSCREEN
DIM A AS STRING * 1
DIM B AS STRING * 1
DIM R AS DOUBLE
DIM P AS DOUBLE
DIM D AS DOUBLE

PRINT "2 is for calculating difference between CI and SI for 2 years."
PRINT "3 is for calculating difference between CI and SI for 3 years."
PRINT "D is for calculating Difference between CI and SI for N years."
INPUT "ENTER CALCULATE FOR:", A
A = UCASE$(A)
CLS
IF A = "D" THEN
    INPUT "PRINCIPAL:", P
    INPUT "RATE%:", R
    INPUT "TIME:", T
    CLS
    PRINT "PRINCIPAL:", P
    PRINT "RATE%:", R
    PRINT "TIME:", T
    PRINT "DIFFERENCE:", (P * (((1 + R / 100) ^ 3) - 1)) - ((P * R * 3) / 100)
    PRINT "SI:", ((P * R * 3) / 100)
    PRINT "CI:", (P * (((1 + R / 100) ^ 3) - 1))
    GOTO ENDA
END IF
PRINT "P is for calculating Principal."
PRINT "R is for calculating Rate%."

INPUT "ENTER CALCULATE FOR:", B
B = UCASE$(B)
IF A = "2" THEN
    IF B = "P" THEN
        CLS
        INPUT "ENTER RATE%:", R
        INPUT "ENTER DIFFERENCE:", D
        CLS
        PRINT "PRINCIPAL:", (D / (R ^ 2)) * 10000
        PRINT "RATE%", R
        PRINT "DIFFERENCE:", D
    END IF
    IF B = "R" THEN
        CLS
        INPUT "ENTER PRINCIPAL:", P
        INPUT "ENTER DIFFERENCE:", D
        CLS
        PRINT "PRINCIPAL:", P
        PRINT "RATE%", (D / P * 10000) ^ (0.5)
        PRINT "DIFFERENCE:", D
    END IF
END IF
IF A = "3" THEN
    IF B = "P" THEN
        CLS
        INPUT "ENTER RATE%:", R
        INPUT "ENTER DIFFERENCE:", D
        CLS
        PRINT "PRINCIPAL:", (D * (100 ^ 3)) / ((300 * (R ^ 2)) + (R ^ 3))
        PRINT "RATE%", R
        PRINT "DIFFERENCE:", D
    END IF
    IF B = "R" THEN
        CLS
        INPUT "ENTER PRINCIPAL:", P
        INPUT "ENTER DIFFERENCE:", D
        CLS

        PRINT "PRINCIPAL:", P
        FOR R = 0 TO 100 STEP 0.0000001490116119384765625
            IF (P * (((1 + R / 100) ^ 3) - 1)) - ((P * R * 3) / 100) = D THEN
                PRINT "RATE%:", R
                C = 0
                C = C + 1
                IF C > 0 THEN EXIT FOR
            END IF

        NEXT R

        PRINT "DIFFERENCE:", D

    END IF
END IF
ENDA:
CLEAR
SLEEP 50
SYSTEM


