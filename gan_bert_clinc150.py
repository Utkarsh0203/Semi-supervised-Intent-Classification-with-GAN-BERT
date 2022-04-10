# -*- coding: utf-8 -*-
"""GAN-BERT_CLINC150.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sx6MlROSFhGuB8gyAggCz9SNqNs1L8Ae
"""

from google.colab import drive
drive.mount('/content/gdrive')

# Commented out IPython magic to ensure Python compatibility.
# %cd "/content/gdrive/MyDrive/AML"
!pwd

!pip uninstall -y tensorflow
!pip install tensorflow-gpu==1.14
!pip install git+https://github.com/guillaumegenthial/tf_metrics.git
!pip install gast==0.2.2

import pandas as pd
import numpy as np
from sklearn.metrics import classification_report

"""### 10_90"""

!python -u ganbert.py \
        --task_name=general \
        --label_rate=0.05 \
        --do_train=true \
        --do_eval=true \
        --do_predict=false \
        --pred_OOS=false \
        --data_dir="data_CLINC150/10_90" \
        --vocab_file= "/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/vocab.txt" \
        --bert_config_file="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_config.json" \
        --init_checkpoint="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_model.ckpt" \
        --max_seq_length=64 \
        --train_batch_size=64 \
        --learning_rate=2e-5 \
        --num_train_epochs=20 \
        --warmup_proportion=0.1 \
        --do_lower_case=false \
        --output_dir=ganbert_output_CLINC150/10_90

"""### 20_80"""

!python -u ganbert.py \
        --task_name=general \
        --label_rate=0.125 \
        --do_train=true \
        --do_eval=true \
        --do_predict=false \
        --pred_OOS=false \
        --data_dir="data_CLINC150/20_80" \
        --vocab_file= "/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/vocab.txt" \
        --bert_config_file="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_config.json" \
        --init_checkpoint="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_model.ckpt" \
        --max_seq_length=64 \
        --train_batch_size=64 \
        --learning_rate=2e-5 \
        --num_train_epochs=18 \
        --warmup_proportion=0.1 \
        --do_lower_case=false \
        --output_dir=ganbert_output_CLINC150/20_80

"""### 40_60"""

!python -u ganbert.py \
        --task_name=general \
        --label_rate=0.33 \
        --do_train=true \
        --do_eval=true \
        --do_predict=false \
        --pred_OOS=false \
        --data_dir="data_CLINC150/40_60" \
        --vocab_file= "/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/vocab.txt" \
        --bert_config_file="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_config.json" \
        --init_checkpoint="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_model.ckpt" \
        --max_seq_length=64 \
        --train_batch_size=64 \
        --learning_rate=2e-5 \
        --num_train_epochs=16 \
        --warmup_proportion=0.1 \
        --do_lower_case=false \
        --output_dir=ganbert_output_CLINC150/40_60

"""### 60_40"""

!python -u ganbert.py \
        --task_name=general \
        --label_rate=0.5 \
        --do_train=true \
        --do_eval=true \
        --do_predict=false \
        --pred_OOS=false \
        --data_dir="data_CLINC150/60_40" \
        --vocab_file= "/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/vocab.txt" \
        --bert_config_file="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_config.json" \
        --init_checkpoint="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_model.ckpt" \
        --max_seq_length=64 \
        --train_batch_size=64 \
        --learning_rate=2e-5 \
        --num_train_epochs=14 \
        --warmup_proportion=0.1 \
        --do_lower_case=false \
        --output_dir=ganbert_output_CLINC150/60_40

"""### 80_20"""

!python -u ganbert.py \
        --task_name=general \
        --label_rate=0.5 \
        --do_train=true \
        --do_eval=true \
        --do_predict=false \
        --pred_OOS=false \
        --data_dir="data_CLINC150/80_20" \
        --vocab_file= "/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/vocab.txt" \
        --bert_config_file="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_config.json" \
        --init_checkpoint="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_model.ckpt" \
        --max_seq_length=64 \
        --train_batch_size=64 \
        --learning_rate=2e-5 \
        --num_train_epochs=12 \
        --warmup_proportion=0.1 \
        --do_lower_case=false \
        --output_dir=ganbert_output_CLINC150/80_20

"""### 90_10"""

!python -u ganbert.py \
        --task_name=general \
        --label_rate=0.5 \
        --do_train=true \
        --do_eval=true \
        --do_predict=false \
        --pred_OOS=false \
        --data_dir="data_CLINC150/90_10" \
        --vocab_file= "/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/vocab.txt" \
        --bert_config_file="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_config.json" \
        --init_checkpoint="/content/gdrive/MyDrive/AML/cased_L-12_H-768_A-12/bert_model.ckpt" \
        --max_seq_length=64 \
        --train_batch_size=64 \
        --learning_rate=2e-5 \
        --num_train_epochs=10 \
        --warmup_proportion=0.1 \
        --do_lower_case=false \
        --output_dir=ganbert_output_CLINC150/90_10