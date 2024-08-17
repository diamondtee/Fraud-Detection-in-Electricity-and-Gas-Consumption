import streamlit as st
from model import prediction


District_map = {
    60:60,
    62:62,
    63:63,
    69:69
}

client_catg_map = {
    11 : 11,
    12 : 12,
    51 : 51
}

region_map = {
      101.0 : 101.0,    
      104.0  :104.0,
      311.0  : 311.0, 
      107.0  : 107.0,  
      301.0  : 301.0,  
      103.0  : 103.0,  
      306.0  : 306.0,   
      303.0  : 303.0,   
      310.0  : 310.0,  
      312.0  : 312.0,  
      302.0  : 302.0, 
      304.0  : 304.0,
      309.0  : 309.0,
      307.0  : 307.0,
      305.0  : 305.0,
      313.0  : 313.0,
      371.0  : 371.0,
      105.0  : 105.0,
      308.0  : 308.0,
      106.0  : 106.0,
      372.0  : 372.0,
      379.0  : 379.0,
      399.0  : 399.0,
      206.0  : 206.0,
      199.0  : 199.0
}



def main():
    st.title("Fraud Detection In Electricity Model Deployment")

    st.image("../electric_fraud.jfif", caption="electric Fraud detection image", use_column_width=True)

District = st.selectbox("Select the District", (i for i in District_map.keys()), placeholder="District")
client_catg = st.selectbox("Select CLient Category",(i for i in client_catg_map.keys()), placeholder="client_catg")
region = st.selectbox("Select region", (i for i in region_map.keys()), placeholder="region")
tarif_type = st.text_input("tarif_type :  ")
tarif_type = st.text_input("Enter integer values between 0 and 40: ")
counter_number = st.text_input("Enter 5 digits number: ")
counter_code = st.text_input("Enter integer values between 100 and 415: ")
reading_remarque = st.text_input("Enter integer values between 5 and 9: ")
counter_coefficient = st.text_input("Enter integer values between 0 and 50: ")
consommation_level_1 = st.text_input("Enter integer values between 0 and 1200: ")
consommation_level_2 = st.text_input("Enter integer values between 0 and 400: ")
consommation_level_3 = st.text_input("Enter integer values between 0 and 800: ")
consommation_level_4 = st.text_input("Enter integer values between 0 and 2403: ")
old_index = st.text_input("Enter integer values between 0 and 98850: ")
new_index = st.text_input("Enter integer values between 0 and 13769: ")
months_number = st.text_input("Enter integer values between 1 and 12: ")
counter_type = st.text_input(" Enter either 0 or 1 ")
    
District = District_map[District]
client_catg = client_catg_map[client_catg]
region = region_map[region]

result = ''

if st.button("Predict"):
    result = prediction(int(District),int(client_catg),int(region),int(tarif_type), int(counter_number), 
                           int(counter_code), int(reading_remarque), int(counter_coefficient),int(consommation_level_1),
                            int(consommation_level_2), int(consommation_level_3),int(consommation_level_4),int(old_index), int(new_index),
                             int(months_number),  int(counter_type))
        
if result[0] == 0:
           st.success('This doesn"t look like a fraud case')
else:
            st.error('This looks like a fraud case')


if __name__=='__main__':
     main()