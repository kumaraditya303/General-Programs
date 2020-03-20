_TITLE "CONTROL"
SCREEN 12
_FULLSCREEN
DO
    DIM A AS STRING * 2
    DIM I AS STRING * 1
    LOCATE 1, 20
    PRINT "SIMPLE , COMPOUND INTEREST CALCULATOR."
    PRINT "SI is for Simple Interest."
    PRINT "CI is for Compound Interest."
    PRINT "DF is for Difference between SI and CI."

    INPUT "ENTER CALCULATE FOR:", A
    A = UCASE$(A)
    IF A = "SI" THEN SHELL "Simple.exe"
    IF A = "CI" THEN SHELL "Compound.exe"
    IF A = "DF" THEN SHELL "Difference.exe"

    CLS
    INPUT "DO YOU WANT TO CALULATE MORE Y/N:", I
    I = UCASE$(I)
    IF I = "Y" THEN
        CLS

    END IF
    IF I <> "Y" THEN
        CLS
        LOCATE 10, 27
        PRINT "THANK YOU HAVE A NICE DAY"
        SLEEP 3
        SYSTEM
    END IF
LOOP
SYSTEM
