from all_libs import *

def load_bert_config(config):
    # Save the slow pretrained tokenizer
    slow_tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    if not os.path.exists(config.bert_config.save_path):
        os.makedirs(config.bert_config.save_path)

    slow_tokenizer.save_pretrained(config.bert_config.save_path)
#
# # Load the fast tokenizer from saved file
# tokenizer = BertWordPieceTokenizer("bert_base_uncased/vocab.txt", lowercase=True)