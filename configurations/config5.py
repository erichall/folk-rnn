one_hot = True
embedding_size = 256  # is ignored if one_hot=True
num_layers = 3
rnn_size = 512
dropout = 0.5

learning_rate = 0.003
learning_rate_decay_after = 20
learning_rate_decay = 0.97

batch_size = 32
max_epoch = 50
grad_clipping = 5
validation_fraction = 0.05
validate_every = 1000  # iterations

save_every = 5  # epochs

#resume_path="metadata/config5-24_oct_folkwiki_and_sessions_50_length_cap-20181024-210059.pkl"
resume_path="config5-24_oct_folkwiki_and_sessions_50_length_cap-20181024-210059_100_EPOCHS.pkl"

