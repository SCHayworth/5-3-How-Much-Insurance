# 5-3 How Much Insurance
# Shaun Hayworth
# CIS 2
# 10-28-2019
# Original source code and revision history can be found at https://github.com/SCHayworth/5-3-How-Much-Insurance

# Calculates the minimum recommended insurance amount based on a 80% of the replacement cost of a building.

# Define the main function
# Mainline program logic
def main():

    # Prompt user for the replacement amount of a building in dollars
    replacement_amount = int(input('Enter the  replacement amount: '))

    # Prompt user for the percentage of insurance
    print('Percent insured: 80%')

    # Call the min_insurance function and pass replacement_amount to it.
    min_insurance(replacement_amount)

# Define the min_insurance function
# Calculates the minimum amount of insurance recommended.
def min_insurance(replacement_amount):

    # Calculate insurance recommendation
    ins_rec = replacement_amount * 0.8

    # Display the recommended amount of insurance
    print(f'Minimum Insurance: ${ins_rec:.2f}')

# Call the main function to execute program
main()
