import subprocess
import sys
from random import randint

if(len(sys.argv) != 3):
    print('Usage: python metadata2mp3.py metadata_name output_name')

metadata_name = sys.argv[1]
output_name = sys.argv[2]

rng_seed = randint(1, 50)
sample_cmd = 'python sample_rnn.py --rng_seed=' + str(rng_seed) + ' ' +  metadata_name

sample_rnn_output = subprocess.check_output(sample_cmd, shell=True)

out = str(sample_rnn_output).split('Saved to ')

if(len(out) != 2):
    print('Failed to run ' + sample_cmd)
    sys.exit(0)

abc_file_name = out[1]
abc_file_name = abc_file_name[0: len(abc_file_name) - 3]

''' clean the abc file '''
abc_file = open(abc_file_name, 'r+')
abc_content = abc_file.readlines()

second = abc_content[1].replace('[', '').replace(']','')
third = abc_content[2].replace('[', '').replace(']','')
fourth, notes = abc_content[3].split(']')
fourth = fourth.replace('[', '') + '\n'
notes = notes.replace(' ', '')

abc_file.seek(0)
abc_file.truncate()
abc_file.write(abc_content[0])
abc_file.write(second)
abc_file.write(third)
abc_file.write(fourth)
abc_file.write(notes)
abc_file.close()

''' abc2midi '''
abc2midi_cmd = 'abc2midi ' + abc_file_name
abc2midi_output = subprocess.check_output(abc2midi_cmd, shell=True)

out = str(abc2midi_output).split('writing MIDI file')
if(len(out) != 2):
    print('Failed to create mid file')
    print(out)
    sys.exit(0)

mid_file_name = out[1]
mid_file_name = mid_file_name[0: len(mid_file_name) -3]

''' mid to wav '''
wav_file_name = 'tmp.wav'
timidity_cmd = 'timidity ' + mid_file_name + ' -Or1sl -o ' + wav_file_name 
subprocess.run(timidity_cmd, shell=True)

''' lame to mp3 '''
lame_cmd = 'lame ' + wav_file_name + ' ' + output_name  + '.mp3'
subprocess.run(lame_cmd, shell=True)

print('###################|| DONE ||#####################')
print('                                                  ')
print(' Wring to file: ' + output_name + '.mp3')
print('                                                  ')
print('##################################################')

