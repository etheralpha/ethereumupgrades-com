import os
import glob

data_dir = "_data"
pages_dir = "upgrades"

# Make sure output collection dir exists
os.makedirs(pages_dir, exist_ok=True)

for filepath in glob.glob(os.path.join(data_dir, "*.yml")):
  basename = os.path.splitext(os.path.basename(filepath))[0] # e.g. "pectra-mainnet"
  outpath = os.path.join(pages_dir, f"{basename}.md")

  # generate front matter
  frontmatter = "---\n"
  frontmatter += f"title: {basename.split('-')[0].capitalize()} {basename.split('-')[1].capitalize()} Upgrade\n"
  frontmatter += "layout: default\n"
  frontmatter += f"upgrade_data_file: {basename}\n"
  frontmatter += "---\n"

  with open(outpath, "w") as f:
    f.write(frontmatter)


