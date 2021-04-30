import streamlit as st
import pandas as pd
import numpy as np
import datetime
import time

def color_selector(score):
	return 'green'
	# if score >= 66.67 and score <= 100:
	# 	return 'green'
	# elif score < 66.67 and score >= 33.33:
	# 	return '#ff9900'
	# elif score < 33.33 and score >= 0:
	# 	return '#cc0000'

def write(df):
# def write(counter, trending_topics, related_article_index):

	# df = pd.read_csv('Trending_Stage_1.csv')
	# df = pd.read_csv('trend.csv',lineterminator='\n')
	# CSV for Source Image Selection
	# source_img = pd.read_csv('source_img_selector.csv')

	# Hide Articles Button Top
	# if st.button('Hide Articles', key='hide_'+str(counter)):
	# 		trending_topics.write('')
	# counter = 0
	# st.markdown('<center style="font-size: 15px">'+df['district'][counter]+'</center>',unsafe_allow_html = True)

	article_printer = []
	related_article_index = df.index.values

	for num in related_article_index:
		# ot_src_img = '#'
		# st.write(df['name'][num])
		# st.write(df['number'][num])
		# st.write(df['lat'][num]*100)
		# st.write(round(df['lng'][num]*100))
		# st.write(df['district'][num])
		# st.write(df['number'][num])

		# for label, row in source_img.iterrows():
		# 	if row['source'] == df['Source'][num]:
		# 		ot_src_img = row['source_url']

		# m = '<div style="position:relative; left:0%; width:100%; border-style: solid; border-color: white; box-shadow: 0px 2px 5px #aaa; padding-bottom:3px;padding-left: 2px; padding-right: 2px;  margin-bottom: 5px">		<img src="'+str(ot_src_img)+'" style="width:75px">		<div style="font-size:12px"><b>'+str(df['name'][num])+'</b></div>		<div style="font-size:11px; padding-bottom:5px">'+str(df['number'][num])+'</div>		<p style="position:relative; left:0%; width:100%; border-style: solid; border-width: .5px; border-color: #efefef; font-size:10px;"><span style="position: absolute; width:33.33%; color: '+color_selector(2)+'">Grade: <b>'+str(33)+'</b></span><a href="'+str(df['district'][num])+'" target="_blank" style="color: #ccc; font-size: 10px; vertical-align: middle;"><span style="position:absolute; display: block; left: 33.33%; width:33.33%; padding-bottom: 2px; padding-top: 2px; text-align:center;">Source</span></a><span style="position: absolute;left: 66.67%; width:33.33%; text-align:right; color: grey"><b>'+str(df['number'][num])+'</b></span></p></div>'
		m = '<div style="position:relative; left:0%; width:100%; border-style: solid; border-color: white; box-shadow: 0px 2px 5px #aaa; padding-bottom:3px;padding-left: 2px; padding-right: 2px;  margin-bottom: 5px"><div style="font-size:12px"><b>'+str(df['name'][num])+'</b></div>		<div style="font-size:11px; padding-bottom:5px">'+str(df['number'][num])+'</div></div>'
		article_printer.append(m)

	
	st.markdown('<div style = "position:relative; width:100%; height: 65vh; overflow-y: auto; margin-bottom:4px">'+" ".join(article_printer)+'</div>', unsafe_allow_html=True)

	# if st.button('Hide Articles', key='hide_end_'+str(counter)):
	# 	trending_topics.write('', trending_topics, related_article_index)