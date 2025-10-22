import os
import glob
import time

data_dir = '_data'
pages_dir = 'upgrades'
current_epoch = time.time() + (86400*2) # show last upgrade for 2 days after activation
upcoming_activation = 1000000000000
upcoming_upgrade = ''

# Make sure output collection dir exists
os.makedirs(pages_dir, exist_ok=True)

def generate_frontmatter(basename):
  frontmatter = '---\n'
  frontmatter += f'title: {basename.split('-')[0].capitalize()} {basename.split('-')[1].capitalize()} Upgrade\n'
  frontmatter += 'layout: default\n'
  frontmatter += f'upgrade_data_file: {basename}\n'
  frontmatter += '---\n'
  return frontmatter


for filepath in glob.glob(os.path.join(data_dir, '*.yml')):
  basename = os.path.splitext(os.path.basename(filepath))[0] # e.g. 'pectra-mainnet'
  outpath = os.path.join(pages_dir, f'{basename}.md')

  with open(filepath, 'r') as file:
    content = file.read()
    activation_epoch = content.split('\nactivation_unix_epoch:')[1].split('\n')[0].replace(' ','')
    try:
      activation_epoch = int(activation_epoch)
    except: # accounts for 'tbd' entries
      activation_epoch = 0
    if activation_epoch > current_epoch and activation_epoch < upcoming_activation:
      upcoming_activation = activation_epoch
      upcoming_upgrade = basename

  frontmatter = generate_frontmatter(basename)

  with open(outpath, 'w') as f:
    f.write(frontmatter)

print(upcoming_upgrade)


if upcoming_upgrade != '':
  frontmatter = generate_frontmatter(upcoming_upgrade)
  with open('index.html', 'w') as f:
    f.write(frontmatter)



