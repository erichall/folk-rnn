import matplotlib as mpl
import numpy as np
mpl.use('Agg')
import matplotlib.pyplot as plt

import seaborn as sns
sns.set()

file_name = 'nohup.out'

with open(file_name) as f:
    content = f.readlines()
    f.close()

data = []
for row in content:
    if(row.split('/')[0].isdigit()):
        data.append(row)

    if('loss:' in row):
        data.append(row)


epochs = []
train_loss = []
validation_loss = []
train_loss_val = []
curr_t_loss = 0
for d in data:
    row = d.split(' ')
    
    if('loss:' in d):
        val_loss = d.split(':')[1].strip()
        validation_loss.append(float(val_loss))
        train_loss_val.append(curr_t_loss)
        continue


    if(len(row) < 5):
        continue
    
    epoch = int(row[0].split('/')[0])
    tloss = float(row[3].split('=')[1])
    curr_t_loss = tloss
    epochs.append(int(epoch))
    train_loss.append(float(tloss))

fig, (ax1, ax2)  = plt.subplots(1,2)
fig.suptitle('Training loss')

ax1.plot(epochs, train_loss)
ax1.set_title('Training loss')
ax1.set_ylabel('Loss')
ax1.set_xlabel('Epochs')

ax2.plot(np.arange(len(validation_loss)), validation_loss, label='validation')
ax2.plot(np.arange(len(validation_loss)), train_loss_val, label='train')
ax2.set_title('Validation vs  Training loss')
ax2.set_ylabel('Loss')
ax2.set_xlabel('# validation, every 1000 epoch')
ax2.legend()

#plt.xlabel('Epochs')
#plt.ylabel('Loss')

fig.savefig('loss_plotv2')
