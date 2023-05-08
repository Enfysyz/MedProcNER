from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import csv
import json
import os

def modelUse(text):
    model_name = "lcampillos/roberta-es-clinical-trials-ner"

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name)
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)

    data = nlp(text)
    return data


def dataClean(data):
    # Cleaning Label
    for i in range(len(data)):
        data[i]['word'] = data[i]['word'].replace("Ã³", "ó")
        data[i]['word'] = data[i]['word'].replace("Ã", "á")
        data[i]['word'] = data[i]['word'].replace("á©", "é")
        data[i]['word'] = data[i]['word'].replace("áŃ", "í")
        data[i]['word'] = data[i]['word'].replace("á¡", "á")
        
        if data[i]['word'][0] == 'Ġ':
            data[i]['word'] = data[i]['word'][1:]

    return data


def combine(data):
    #keys = fieldnames = ['entity', 'score', 'index', 'word', 'start', 'end']

    # Combining b- and i-
    combined_data = []
    for i in range(len(data)):
        if data[i]['entity'].startswith('B-'):
            row = {'word': data[i]['word'], 'score': data[i]['score'], 'index': data[i]['index'], 'entity': data[i]['entity'][2:], 'start': data[i]['start'], 'end': data[i]['end']}
            j = i + 1
            while j < len(data) and data[j]['entity'] == 'I-' + row['entity']:
                row['word'] += ' ' + data[j]['word']
                j += 1
            combined_data.append(row)

    return combined_data


def createANN(data, file_name):
    # Creating ANN file
    directory = 'AnnFiles'
    file_name = file_name[:-4]
    n = file_name + '.ann'
    file_path = os.path.join(directory, n)
    
    with open(file_path, mode='w', newline='', encoding='utf-8') as ann_file:
        for i, row in enumerate(data):
            text = row['word']
            label = row['entity']
            
            # Generate the annotation text for this row
            index = i+1
            start_idx = i * len(text) + 1
            end_idx = start_idx + len(text)
            ann_text = f'T{index} {label} {start_idx} {end_idx} {text}\n'
            
            # Write the annotation text to the .ann file
            ann_file.write(ann_text)

            


# Set the path to the folder containing the files
folder_path = 'txt'

# Get a list of all the files in the folder
file_list = os.listdir(folder_path)

# Loop over each file and read its contents
for file_name in file_list:
    # Construct the path to the file
    fileno = 0
    file_path = os.path.join(folder_path, file_name)
    
    
    # Open the file and read its contents
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()
    
    data = modelUse(contents)
    data = dataClean(data)
    combined_data = combine(data)
    createANN(combined_data, file_name)
    print(fileno+1)
    

print("Done")






        
    # Write the plain text to the .ann file
    # plain_text = '\n'.join([row['word'] for row in combined_data])
    # ann_file.write(f'#Text\n{plain_text}')