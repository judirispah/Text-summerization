import os
from textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self,example_batch):
        input_encodings=self.tokenizer(example_batch['dialogue'],max_length=1024 ,truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    
    def convert(self):
        #dataset=load_from_disk(self.config.data_path)
        # Assuming the files are in JSON format
        dataset = load_dataset('json', data_files={
    'train': f'{self.config.data_path}/train.json',
    'test': f'{self.config.data_path}/test.json',
    'validation': f'{self.config.data_path}/val.json'
})
        tokenized_dataset=dataset.map(self.convert_examples_to_features,batched=True)
        print(tokenized_dataset['train'][0])
        tokenized_dataset.save_to_disk(os.path.join(self.config.root_dir,"tokenized_samsum_dataset"))


        
