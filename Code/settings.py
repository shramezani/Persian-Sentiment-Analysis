
#Declare global variables

MODEL_DIR = '../Models/' 
MODEL_PATH = MODEL_DIR+'temp_model.h5'
DATA_PATH = '../Dataset/'
TOKENIZER_PATH = MODEL_DIR+'tokenizer.p'
SEED =1234
EMB_SIZE =300
SEQUENCE_LEN = 128


LABEL_DIC={0:'Furious',
           1:'Angry',
           2:'Neutral',
           3:'Happy',
           4:'Delighted'}