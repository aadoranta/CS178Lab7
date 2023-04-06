"""Somerville Projector

This script generates 2D projections of the somerville_happiness_2018
dataset.

It assumes that it is in the same folder as somerville_happiness_survey.csv

This script requires that `pandas`, sklearn, umap, and numpy be installed within 
the Python environment you are running this script in.

and should generate three files:

- pca.json
- mds.json
- tsne.json
- umap.json

Consult the documentation for all four techniques to understand their usage.

https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html
https://scikit-learn.org/stable/modules/generated/sklearn.manifold.MDS.html
https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
https://umap-learn.readthedocs.io/en/latest/
"""

import pandas as pd
import numpy as np
import sklearn
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.manifold import MDS
import json
from umap import UMAP

def project_somerville():
	df = pd.read_csv('somerville_happiness_survey.csv', index_col=0)

	raw_data = df[['city_services', 'housing_cost', 'schools', 'trust_police', 'streets_sidewalks', 'events']]
	raw_data_indices = raw_data.index.values
	num_data_pts = raw_data.shape[0]

	# Just some code loading up junk data, when you finish your solution code, you can comment this out.
	# Currently just makes every point have either a 0 or 1 for its x and y coordinate
	# pca_results = [[np.random.choice([0,1]), np.random.choice([0,1])] for k in range(num_data_pts)]
	# mds_results = [[np.random.choice([0,1]), np.random.choice([0,1])] for k in range(num_data_pts)]
	# tsne_results = [[np.random.choice([0,1]), np.random.choice([0,1])] for k in range(num_data_pts)]
	# umap_results = [[np.random.choice([0,1]), np.random.choice([0,1])] for k in range(num_data_pts)]

	# TODO: calculate the projections on the raw_data to fill the variables 
	# pca_results, mds_results, tsne_results, and umap_result

	# Then, we have some code which gets the projections into an easy-to-deal-with format, as expected
	# by the front end.  It also writes out to the json files. You don't have to change this.

	pca = PCA(n_components=2)
	pca_results = pca.fit_transform(raw_data)

	tsne_2 = TSNE(n_components=2, perplexity=2)
	tsne_results_2 = tsne_2.fit_transform(raw_data)

	tsne_5 = TSNE(n_components=2, perplexity=5)
	tsne_results_5 = tsne_5.fit_transform(raw_data)

	tsne_10 = TSNE(n_components=2, perplexity=10)
	tsne_results_10 = tsne_10.fit_transform(raw_data)

	tsne_20 = TSNE(n_components=2, perplexity=20)
	tsne_results_20 = tsne_20.fit_transform(raw_data)

	mds = MDS(n_components=2)
	mds_results = mds.fit_transform(raw_data)

	umap = UMAP(n_components=2)
	umap_results = umap.fit_transform(raw_data)

	pca_results_json_obj = {}
	mds_results_json_obj = {}
	tsne_results_json_obj_2 = {}
	umap_results_json_obj = {}
	tsne_results_json_obj_5 = {}
	tsne_results_json_obj_10 = {}
	tsne_results_json_obj_20 = {}

# ***********************************************************************************************
	# Added all data features to the projected data dictionary we send to the front end
	for (j, uid) in enumerate(raw_data_indices):
		pca_results_json_obj[str(uid)] = {'x': str(pca_results[j][0]), 'y': str(pca_results[j][1]), 
				    'city_services': str(raw_data['city_services'].iloc[j]), 
				    'housing_cost': str(raw_data['housing_cost'].iloc[j]), 
					'schools': str(raw_data['schools'].iloc[j]), 
					'trust_police': str(raw_data['trust_police'].iloc[j]), 
					'streets_sidewalks': str(raw_data['streets_sidewalks'].iloc[j]), 
					'events': str(raw_data['events'].iloc[j])}
		mds_results_json_obj[str(uid)] = {'x': str(mds_results[j][0]), 'y': str(mds_results[j][1]),
					'city_services': str(raw_data['city_services'].iloc[j]), 
				    'housing_cost': str(raw_data['housing_cost'].iloc[j]), 
					'schools': str(raw_data['schools'].iloc[j]), 
					'trust_police': str(raw_data['trust_police'].iloc[j]), 
					'streets_sidewalks': str(raw_data['streets_sidewalks'].iloc[j]), 
					'events': str(raw_data['events'].iloc[j])}
		tsne_results_json_obj_2[str(uid)] = {'x': str(tsne_results_2[j][0]), 'y': str(tsne_results_2[j][1]),
					'city_services': str(raw_data['city_services'].iloc[j]), 
				    'housing_cost': str(raw_data['housing_cost'].iloc[j]), 
					'schools': str(raw_data['schools'].iloc[j]), 
					'trust_police': str(raw_data['trust_police'].iloc[j]), 
					'streets_sidewalks': str(raw_data['streets_sidewalks'].iloc[j]), 
					'events': str(raw_data['events'].iloc[j])}
		umap_results_json_obj[str(uid)] = {'x': str(umap_results[j][0]), 'y': str(umap_results[j][1]),
					'city_services': str(raw_data['city_services'].iloc[j]), 
				    'housing_cost': str(raw_data['housing_cost'].iloc[j]), 
					'schools': str(raw_data['schools'].iloc[j]), 
					'trust_police': str(raw_data['trust_police'].iloc[j]), 
					'streets_sidewalks': str(raw_data['streets_sidewalks'].iloc[j]), 
					'events': str(raw_data['events'].iloc[j])}
		tsne_results_json_obj_5[str(uid)] = {'x': str(tsne_results_5[j][0]), 'y': str(tsne_results_5[j][1]),
					'city_services': str(raw_data['city_services'].iloc[j]), 
				    'housing_cost': str(raw_data['housing_cost'].iloc[j]), 
					'schools': str(raw_data['schools'].iloc[j]), 
					'trust_police': str(raw_data['trust_police'].iloc[j]), 
					'streets_sidewalks': str(raw_data['streets_sidewalks'].iloc[j]), 
					'events': str(raw_data['events'].iloc[j])}
		tsne_results_json_obj_10[str(uid)] = {'x': str(tsne_results_10[j][0]), 'y': str(tsne_results_10[j][1]),
					'city_services': str(raw_data['city_services'].iloc[j]), 
				    'housing_cost': str(raw_data['housing_cost'].iloc[j]), 
					'schools': str(raw_data['schools'].iloc[j]), 
					'trust_police': str(raw_data['trust_police'].iloc[j]), 
					'streets_sidewalks': str(raw_data['streets_sidewalks'].iloc[j]), 
					'events': str(raw_data['events'].iloc[j])}
		tsne_results_json_obj_20[str(uid)] = {'x': str(tsne_results_20[j][0]), 'y': str(tsne_results_20[j][1]),
					'city_services': str(raw_data['city_services'].iloc[j]), 
				    'housing_cost': str(raw_data['housing_cost'].iloc[j]), 
					'schools': str(raw_data['schools'].iloc[j]), 
					'trust_police': str(raw_data['trust_police'].iloc[j]), 
					'streets_sidewalks': str(raw_data['streets_sidewalks'].iloc[j]), 
					'events': str(raw_data['events'].iloc[j])}
# ****************************************************************************************************
		

	# Finally, we write them out to json.
	with open('pca.json', 'w') as outfile:
		json.dump(pca_results_json_obj, outfile)

	with open('mds.json', 'w') as outfile:
		json.dump(mds_results_json_obj, outfile)

	with open('tsne2.json', 'w') as outfile:
		json.dump(tsne_results_json_obj_2, outfile)

	with open('tsne5.json', 'w') as outfile:
		json.dump(tsne_results_json_obj_5, outfile)

	with open('tsne10.json', 'w') as outfile:
		json.dump(tsne_results_json_obj_10, outfile)

	with open('tsne20.json', 'w') as outfile:
		json.dump(tsne_results_json_obj_20, outfile)

	with open('umap.json', 'w') as outfile:
		json.dump(umap_results_json_obj, outfile)

	return pca_results_json_obj, mds_results_json_obj, tsne_results_json_obj_2, umap_results_json_obj, tsne_results_json_obj_5, tsne_results_json_obj_10, tsne_results_json_obj_20
