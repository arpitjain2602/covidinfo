import streamlit as st
import pandas as pd
import numpy as np
import category_wise_hospitals

def color_selector(score):
	if score >= 66.67 and score <= 100:
		return 'green'
	elif score < 66.67 and score >= 33.33:
		return '#ff9900'
	elif score < 33.33 and score >= 0:
		return '#cc0000'

@st.cache
def fetching_data():
	df = pd.read_html('https://docs.google.com/spreadsheets/d/e/2PACX-1vTpjIMDZNYJPCvVkhS_XSSFMr7Qyxhmf9a3m8ajPUuVXnEQBlOJbRCzPYSqSIfwaX-A_hhhjXuMWkm-/pubhtml?gid=0&single=true')[0]
	del df['Unnamed: 0']
	df.columns = df.iloc[0]
	df.drop(df.index[0], inplace=True)
	df['gen-avail'] = df['gen-avail'].astype(int)
	df['oxy-avail'] = df['oxy-avail'].astype(int)
	df['icu-gen'] = df['icu-gen'].astype(int)
	df['icu-ventilator'] = df['icu-ventilator'].astype(int)
	return df

def main():

	st.markdown('<style>html {scroll-behavior: smooth;}</style>', unsafe_allow_html=True)
	Head = st.sidebar.markdown('<H1><center style="position:relative; color: #404040; font: Arial Black; width: 100%; background-color: white; border-style: solid; border-width:10px 0px 10px 0px; border-color: white; box-shadow: 0px 5px 5px #ddd">COVID HELP</center></h1>',unsafe_allow_html=True)

	#Navigate
	# selection = st.sidebar.radio("", list(PAGES.keys())[:4])

	# df = pd.read_csv('upload.csv')
	# df.reset_index(inplace=True, drop=True)

	
	# df = pd.read_html('https://docs.google.com/spreadsheets/d/e/2PACX-1vTpjIMDZNYJPCvVkhS_XSSFMr7Qyxhmf9a3m8ajPUuVXnEQBlOJbRCzPYSqSIfwaX-A_hhhjXuMWkm-/pubhtml?gid=0&single=true')[0]
	# del df['Unnamed: 0']
	# df.columns = df.iloc[0]
	# df.drop(df.index[0], inplace=True)
	# df['gen-avail'] = df['gen-avail'].astype(int)
	# df['oxy-avail'] = df['oxy-avail'].astype(int)
	# df['icu-gen'] = df['icu-gen'].astype(int)
	# df['icu-ventilator'] = df['icu-ventilator'].astype(int)

	df = fetching_data()

	option = st.multiselect('District',list(df['district'].value_counts().index))

	# Checkbox
	# general_bed = st.checkbox('Show me General Bed')
	# oxygen_bed = st.checkbox('Show me Oxygen Bed')
	# icu_general_bed = st.checkbox('Show me ICU General Bed')
	# icu_ventilator_bed = st.checkbox('Show me ICU Ventilator Bed')

	# if general_bed:
	# 	temp_df = df[df['gen-avail'] > 0]
	# 	if len(option)>0:
	# 		temp_df = temp_df[temp_df['district'].isin(option)]
	# 	temp_df.reset_index(inplace=True, drop=True)
	# 	st.write('Total {} beds available in {} hospitals'.format(temp_df['gen-avail'].sum(), len(temp_df)))
	# 	st.table(temp_df[['name', 'gen-avail', 'number', 'district']])

	# if oxygen_bed:
	# 	temp_df = df[df['oxy-avail'] > 0]
	# 	if len(option)>0:
	# 		temp_df = temp_df[temp_df['district'].isin(option)]
	# 	temp_df.reset_index(inplace=True, drop=True)
	# 	st.write('Total {} beds available in {} hospitals'.format(temp_df['oxy-avail'].sum(), len(temp_df)))
	# 	st.table(temp_df[['name', 'oxy-avail', 'number', 'district']])

	# if icu_general_bed:
	# 	temp_df = df[df['icu-gen'] > 0]
	# 	if len(option)>0:
	# 		temp_df = temp_df[temp_df['district'].isin(option)]
	# 	temp_df.reset_index(inplace=True, drop=True)
	# 	st.write('Total {} beds available in {} hospitals'.format(temp_df['icu-gen'].sum(), len(temp_df)))
	# 	st.table(temp_df[['name', 'icu-gen', 'number', 'district']])

	# if icu_ventilator_bed:
	# 	temp_df = df[df['icu-ventilator'] > 0]
	# 	if len(option)>0:
	# 		temp_df = temp_df[temp_df['district'].isin(option)]
	# 	temp_df.reset_index(inplace=True, drop=True)
	# 	st.write('Total {} beds available in {} hospitals'.format(temp_df['icu-ventilator'].sum(), len(temp_df)))
	# 	st.table(temp_df[['name', 'icu-ventilator', 'number', 'district']])


	counter=0
	avg_grade = 75
	temp_df = df[df['gen-avail'] > 0]
	if len(option)>0:
		temp_df = temp_df[temp_df['district'].isin(option)]
	st.markdown('<div id="topic_'+str(counter)+'" style="position:relative; left:0%; width:100%; border-style: solid; border-color: #fefeff; box-shadow: 0px 1px 3px #aaa; padding: 5px 2px; margin-bottom: 5px; background-color: #fefeff; border-radius: 3px">		<div style="position: absolute; top: 0%; width:50%; height: 100%; color: #5d5d5d; padding-left: 4px; display: flex; align-items: center; font-size: 17px"><span><b>'+'General Beds'+'</b><br><span style="font-size:13px; color: grey"><i>'+str(len(temp_df))+' Hospitals'+'</i></span></span></div><div style="position: relative;left: 50%; width:50%; text-align:right; color: black;  padding-right: 4px; ">'+str(temp_df['gen-avail'].sum())+' Beds Available<br><span style = "color: '+color_selector(round(avg_grade))+'; font-size: 13px"><i>Check Availability<b>'+'</b></i></span></div></div>', unsafe_allow_html=True)
	view_gen_hospital = st.checkbox('View Hospitals', key='topic_'+str(0))

	if view_gen_hospital:
		category_wise_hospitals.write(temp_df)

	temp_df_oxy = df[df['oxy-avail'] > 0]
	if len(option)>0:
		temp_df_oxy = temp_df_oxy[temp_df_oxy['district'].isin(option)]
	st.markdown('<div id="topic_'+str(counter)+'" style="position:relative; left:0%; width:100%; border-style: solid; border-color: #fefeff; box-shadow: 0px 1px 3px #aaa; padding: 5px 2px; margin-bottom: 5px; background-color: #fefeff; border-radius: 3px">		<div style="position: absolute; top: 0%; width:50%; height: 100%; color: #5d5d5d; padding-left: 4px; display: flex; align-items: center; font-size: 17px"><span><b>'+'Oxygen Beds'+'</b><br><span style="font-size:13px; color: grey"><i>'+str(len(temp_df_oxy))+' Hospitals'+'</i></span></span></div><div style="position: relative;left: 50%; width:50%; text-align:right; color: black;  padding-right: 4px; ">'+str(temp_df_oxy['oxy-avail'].sum())+' Beds Available<br><span style = "color: '+color_selector(round(avg_grade))+'; font-size: 13px"><i>Check Availability<b>'+'</b></i></span></div></div>', unsafe_allow_html=True)
	view_oxy_hospital = st.checkbox('View Hospitals', key='topic_'+str(1))
	if view_oxy_hospital:
		category_wise_hospitals.write(temp_df_oxy)



	temp_df_icugen = df[df['icu-gen'] > 0]
	if len(option)>0:
		temp_df_icugen = temp_df_icugen[temp_df_icugen['district'].isin(option)]
	st.markdown('<div id="topic_'+str(counter)+'" style="position:relative; left:0%; width:100%; border-style: solid; border-color: #fefeff; box-shadow: 0px 1px 3px #aaa; padding: 5px 2px; margin-bottom: 5px; background-color: #fefeff; border-radius: 3px">		<div style="position: absolute; top: 0%; width:50%; height: 100%; color: #5d5d5d; padding-left: 4px; display: flex; align-items: center; font-size: 17px"><span><b>'+'ICU General Beds'+'</b><br><span style="font-size:13px; color: grey"><i>'+str(len(temp_df_icugen))+' Hospitals'+'</i></span></span></div><div style="position: relative;left: 50%; width:50%; text-align:right; color: black;  padding-right: 4px; ">'+str(temp_df_icugen['icu-gen'].sum())+' Beds Available<br><span style = "color: '+color_selector(round(avg_grade))+'; font-size: 13px"><i>Check Availability<b>'+'</b></i></span></div></div>', unsafe_allow_html=True)	
	view_icugen_hospital = st.checkbox('View Hospitals', key='topic_'+str(2))
	if view_icugen_hospital:
		category_wise_hospitals.write(temp_df_icugen)



	temp_df_icuvent = df[df['icu-ventilator'] > 0]
	if len(option)>0:
		temp_df_icuvent = temp_df_icuvent[temp_df_icuvent['district'].isin(option)]
	st.markdown('<div id="topic_'+str(counter)+'" style="position:relative; left:0%; width:100%; border-style: solid; border-color: #fefeff; box-shadow: 0px 1px 3px #aaa; padding: 5px 2px; margin-bottom: 5px; background-color: #fefeff; border-radius: 3px">		<div style="position: absolute; top: 0%; width:50%; height: 100%; color: #5d5d5d; padding-left: 4px; display: flex; align-items: center; font-size: 17px"><span><b>'+'ICU Ventilator Beds'+'</b><br><span style="font-size:13px; color: grey"><i>'+str(len(temp_df_icuvent))+' Hospitals'+'</i></span></span></div><div style="position: relative;left: 50%; width:50%; text-align:right; color: black;  padding-right: 4px; ">'+str(temp_df_icuvent['icu-ventilator'].sum())+' Beds Available<br><span style = "color: '+color_selector(round(avg_grade))+'; font-size: 13px"><i>Check Availability<b>'+'</b></i></span></div></div>', unsafe_allow_html=True)
	view_icuvent_hospital = st.checkbox('View Hospitals', key='topic_'+str(3))
	if view_icuvent_hospital:
		category_wise_hospitals.write(temp_df_icuvent)


		# if view_article:
		# 	topic_wise_articles.write(counter, trending_topics, related_article_index)




	# if st.button('General Bed'):
	# 	temp_df = df[df['gen-avail'] > 0]
	# 	if len(option)>0:
	# 		temp_df = temp_df[temp_df['district'].isin(option)]
	# 	temp_df.reset_index(inplace=True, drop=True)
	# 	st.table(temp_df[['name', 'gen-avail', 'number', 'district']])

	# if len(option) > 0:
	# 	st.table(df[df['district'].isin(option)])

if __name__ == "__main__":
	main()