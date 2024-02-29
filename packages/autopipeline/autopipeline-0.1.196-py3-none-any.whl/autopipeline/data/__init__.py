import pkg_resources
import csv
import pandas as pd

def get_persuasion_effect_data():
    data_file_path = pkg_resources.resource_filename('autopipeline', 'data/persuasive-17.csv')
    df = pd.read_csv(data_file_path, on_bad_lines='skip', delimiter='\t')
    return df

def get_toxic_data():
    data_file_path = pkg_resources.resource_filename('autopipeline', 'data/toxic.csv')
    df = pd.read_csv(data_file_path, on_bad_lines='skip', delimiter='\t')
    return df

def get_dog_whistle_data():
    data_file_path = pkg_resources.resource_filename('autopipeline', 'data/dogwhistle.tsv')
    df = pd.read_csv(data_file_path, on_bad_lines='skip', delimiter='\t')
    return df

