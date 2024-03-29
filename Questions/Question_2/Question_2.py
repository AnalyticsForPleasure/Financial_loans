import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import squarify    # You need to install this library using pip: pip install squarify
import seaborn as sns

#import dataframe_image as dfi
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap #


## Source: https://www.kaggle.com/datasets/nezukokamaado/auto-loan-dataset?select=financial_loan.csv
# **************************************************************************************************************
# Function  name: retrieving_the_amount_of_loan_taken_by_each_state
# input:
# return value:
# ***************************************************************************************************************
def retrieving_the_total_cash_loan_taken_by_each_state(df):
    list_of_states = []
    total_amount_cash_loans_for_specific_state_list = []


    groups_by_state = df.groupby('address_state')
    for state_name, mini_df_per_state in groups_by_state:
        # print("The state name is: ", state_name)
        # print(mini_df_per_state)

        total_amount_cash_loans_for_specific_state = mini_df_per_state['loan_amount'].sum()
        total_amount_cash_loans_for_specific_state_list.append(total_amount_cash_loans_for_specific_state)
        list_of_states.append(state_name)

    list_of_full_names_states = ['Alaska', 'Alabama', 'Arkansas', 'Arizona', 'California', 'Colorado', 'Connecticut',
                                 'District of Columbia', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Iowa', 'Idaho',
                                 'Illinois', 'Indiana', 'Kansas', 'Kentucky', 'Louisiana',
                                 'Massachusetts', 'Maryland', 'Maine', 'Michigan', 'Minnesota', 'Missouri',
                                 'Mississippi', 'Montana', 'North Carolina', 'Nebraska', 'New Hampshire', 'New Jersey',
                                 'New Mexico', 'Nevada', 'New York', 'Ohio', 'Oklahoma', 'Oregon',
                                 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
                                 'Utah', 'Virginia', 'Vermont', 'Washington', 'Wisconsin', 'West Virginia', 'Wyoming']

    df_starting = {'States': list_of_full_names_states,
                   'State_abbreviations': list_of_states,
                   'Total_amount_of_cash_loans_for_a_specific_state': total_amount_cash_loans_for_specific_state_list}

    final_table = pd.DataFrame(df_starting,
                               columns=['States', 'State_abbreviations', 'Total_amount_of_cash_loans_for_a_specific_state'])

    final_table = final_table.sort_values(by = 'Total_amount_of_cash_loans_for_a_specific_state', ascending=False)
    # let's present only the states with more than 100 taken loans !!!

    output_data =final_table.loc[(final_table['Total_amount_of_cash_loans_for_a_specific_state'] > 1000000)]

    print('*')

    return output_data


# **************************************************************************************************************
# Function  name: creating_a_treemap_count_for_each_state
# input:
# return value:
# ***************************************************************************************************************
def creating_a_treemap_count_for_each_state(result_table):
    plt.figure(figsize=(20, 9.5), facecolor='#f6f5f5')

    # Concatenate state labels with their respective sizes (number of loans)
    labels_with_sizes = [f'{state}\n({"{:,.0f}".format(size)})' for state, size in zip(result_table['States'], result_table['Total_amount_of_cash_loans_for_a_specific_state'])]  # TODO: Need to ask about this line

    #labels = list(result_table.loc[:,'States'])
    sizes =list(result_table.loc[:,'Total_amount_of_cash_loans_for_a_specific_state'])

    # Define a colormap with different shades of blue
    cmap = plt.cm.get_cmap('Blues', len(labels_with_sizes))

    # Generate a list of blue color strings
    blue_colors = [cmap(i) for i in reversed(range(len(labels_with_sizes)))]

    # Plotting
    #plt.figure(figsize=(8, 6))
    squarify.plot(sizes=sizes, label=labels_with_sizes, color=blue_colors, alpha=0.7,pad=True,  text_kwargs={'fontsize':10,'fontname':'Franklin Gothic Medium Cond'})
    # Adding title and axis labels
    plt.title("Example Treemap")
    plt.axis('off')  # Turn off axis
    # Display the plot
    plt.title('Total Sum of Cash Loans in Each State (Exceeding $1,000,000)' ,fontsize=30, weight='bold',fontname='Franklin Gothic Medium Cond', color = 'dimgrey')
    plt.savefig('treemap_sum_of_loans_for_each_state.jpg', dpi=250, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':

    pd.set_option('display.max_rows', 5000)
    df = pd.read_csv('/home/shay_diy/PycharmProjects/Financial_loans/Data/financial_loan.csv')
    print('*')

# **************************************************************************************************************
# Starting with getting a short glance information about the data
# ***************************************************************************************************************
    unique_application_type = pd.unique(df['application_type'])
    unique_emp_length = pd.unique(df['emp_length']) #  emp_length = Number of years in the job
    unique_loan_status = pd.unique(df['loan_status']) # unique_loan_status : Charged Off , Fully Paid , Current
    unique_purpose =  pd.unique(df['purpose']) # purpose : car , credit card , Debt consolidation , educational , home improvement , house , major purchase , medical , other , small business , vacation , wedding
    unique_home_ownership = pd.unique(df['home_ownership']) # home_ownership : 'Rent' , 'Own' , 'Mortgage'
    unique_address_state = pd.unique(df['address_state'])

    purpose_his = df['purpose'].value_counts()
    emp_length_his = df['emp_length'].value_counts()
    id_his = df['id'].value_counts()

    loan_amount_his  = df['loan_amount'].value_counts().reset_index()
    loan_size_info = loan_amount_his.sort_values(by=['loan_amount'])
    print('*')
# ***************************************************************************************************************



    res = retrieving_the_total_cash_loan_taken_by_each_state(df)
    creating_a_treemap_count_for_each_state(res)
    print('*')