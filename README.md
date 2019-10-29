# 5-3 How Much Insurance?
Calculates the minimum amount of insurance for a building using a function.

## Scope
Many financial experts advise that property owners should insure their homes or buildings for at least 80 percent of the amount it would cost to replace the structure. Write a program that asks the user to enter the replacement cost of a building, then use a function to calculate and display the minimum amount of insurance he or she should buy for that building.

### Sample Run
    Enter the replacement amount: 100000
    Percent insured: 80%
    Minimum insurance: $80,000.00

### Pseudocode
    START
    INPUT replacement amount in dollars
    CALL minimum insurance function
    END

    FUNCTION minimum insurance
      Pass In: replacement amount
      OUTPUT 80% insured
      Calculate the minimum insurance needed:
        minimum = replacement amount * 0.8
      OUTPUT minimum insurance
    END FUNCTION
