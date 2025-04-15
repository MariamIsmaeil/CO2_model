import streamlit as st
import pickle
with open('fuel_model.pkl','wb') as f:
  pickle.dump(model,f)
st.title('Fuel Consumption')
ENGINESIZE=st.number_input('Enter Engine Size',min_value=0,max_value=100,value=10)
CYLINDERS=st.number_input('Enter Cylinders',min_value=0,max_value=100,value=10)
FUELCONSUMPTION_CITY=st.number_input('Enter Fuel Consumption City',min_value=0,max_value=100,value=10)
FUELCONSUMPTION_HWY=st.number_input('Enter Fuel Consumption Highway',min_value=0,max_value=100,value=10)
FUELCONSUMPTION_COMB=st.number_input('Enter Fuel Consumption Comb',min_value=0,max_value=100,value=10)
FUELCONSUMPTION_COMB_MPG=st.number_input('Enter Fuel Consumption Comb MPG',min_value=0,max_value=100,value=10)
out=model.predict([[ENGINESIZE,CYLINDERS,FUELCONSUMPTION_CITY,FUELCONSUMPTION_HWY,FUELCONSUMPTION_COMB,FUELCONSUMPTION_COMB_MPG]])
st.write(out)
