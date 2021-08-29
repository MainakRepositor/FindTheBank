
import streamlit as st
import requests
import pandas as pd

def Bank_Data_Finder(IFSC_Code):
    try:
        url = 'https://ifsc.razorpay.com/' + IFSC_Code
        bank_info = requests.get(url).json()
        all_details = []
        bank_name = bank_info['BANK']
        branch = bank_info['BRANCH']
        address = bank_info['ADDRESS']
        city = bank_info['CITY']
        state = bank_info['STATE']
        ifsc = bank_info['IFSC']
        contact = bank_info['CONTACT']
        upi = 'UPI: ' + 'Available' if bank_info['UPI'] == True else 'Not Available'
        rtgs = 'RTGS: ' + 'Available' if bank_info['RTGS'] == True else 'Not Available'
        neft = "NEFT: " + 'Available' if bank_info['NEFT'] == True else 'Not Available'
        imps = 'IMPS: ' + 'Available' if bank_info['IMPS'] == True else 'Not Available'

        all_details.append(bank_name)
        all_details.append(branch)
        all_details.append(address)
        all_details.append(city)
        all_details.append(state)
        all_details.append(ifsc)
        all_details.append(contact)
        all_details.append(upi)
        all_details.append(rtgs)
        all_details.append(neft)
        all_details.append(imps)
        return all_details
    except Exception as e:
        print(e)

def run():
    ## Putting Logo of bank
   # img1 = Image.open('bank.png')
   # img1 = img1.resize((156,145))
    #st.image(img1,use_column_width=False)
    st.title("FIND THE BANK")
    
    ## Textbox for getting IFSC from the user
    ifsc = st.text_input('Enter your Bank IFSC Code Eg: SBIN0000001')
    if st.button("Search"):
        bank_data = Bank_Data_Finder(ifsc)
        # data = pd.DataFrame(bank_data)
        if bank_data:
            index_name = ['Bank Name','Branch','Address','City','State','IFSC','Contact','UPI','RTGS','NEFT','IMPS']
            df = pd.DataFrame({'Info': bank_data},index = index_name)
            st.dataframe(df)
        else:
            st.warning("Check your IFSC code!!!")
run()
