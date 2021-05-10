
#Declare global variables
SEED =1234
EMB_SIZE =100
SEQUENCE_LEN = 128
CLASS_NUM = 5

MODEL_DIR = '../Models/' 
DATA_DIR  = '../Dataset/'
EMB_DIR   = '../Embedding/'

MODEL_PATH = MODEL_DIR+'temp_model.h5'
TOKENIZER_PATH = MODEL_DIR+'tokenizer.p'
ORIG_DATA_PATH = DATA_DIR+'DeepSentiPers-original.csv'
EMBEDDING_PATH = EMB_DIR+'fasttext-{emb_size}.bin'.format(emb_size = str(EMB_SIZE))



LABEL_DIC={0:'Furious',
           1:'Angry',
           2:'Neutral',
           3:'Happy',
           4:'Delighted'}