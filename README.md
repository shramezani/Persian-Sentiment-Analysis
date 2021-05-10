# Persian-Sentiment-Analysis

<strong>This repository contains a simple sentiment analysis for Persian language</strong>

## Install

To run this source code please create a new tensorflow conda environment first and then install required libraries


```shell
 conda create -n tf_2 tensorflow-gpu cudatoolkit=10.2 python=3.8
 pip install -r requirements.txt 
 conda install -c conda-forge numpy=1.19.5
```


## Dataset

- This folder contains a DeepSentiPers-original.csv that contains all labeled dataset, we then preprocess and spilt this dataset to train.csv, test.csv and valid.csv

- The labels are as follows:
<ol> <li>Furious</li> <li>Angry</li> <li>Neutral</li> <li>Happy</li> <li>Delighted</li> </ol>
<div class="table-wrapper"><table> <thead> <tr> <th style="text-align: center">Label</th> <th style="text-align: center">#</th> </tr> </thead> <tbody> <tr> <td style="text-align: center">Furious</td> <td style="text-align: center">236</td> </tr> <tr> <td style="text-align: center">Angry</td> <td style="text-align: center">1357</td> </tr> <tr> <td style="text-align: center">Neutral</td> <td style="text-align: center">2874</td> </tr> <tr> <td style="text-align: center">Happy</td> <td style="text-align: center">2848</td> </tr> <tr> <td style="text-align: center">Delighted</td> <td style="text-align: center">2516</td> </tr> </tbody> </table></div>

```
@misc{sharami2020deepsentipers,
    title={DeepSentiPers: Novel Deep Learning Models Trained Over Proposed Augmented Persian Sentiment Corpus},
    author={Javad PourMostafa Roshan Sharami and Parsa Abbasi Sarabestani and Seyed Abolghasem Mirroshandel},
    year={2020},
    eprint={2004.05328},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```


- To preprocess and prepare the dataset please follow the Data Preparation.ipynb notebook in the Code directory. We also provided interesting data analysis in this notebook.

## Model

- We are using a fasttext embedding and a two-layer BiGRU model for this project. 
- To pretrain the model please follow the Model.ipynb notebook in the Code directory.
- You can config path addresses and some global variables in the settings.py file
- We save the pretrained models in the Models directory


## REST API

- We are using Flask to deploy the pretrained model. Please open *index.html* which is located in the Code/WebPage directory
and also run ```python flask-restapi.py ```  command in the Code directory. 
