# ethereumupgrades-com

This is the source code for <https://ethereumupgrades.com>, an info site for Ethereum upgrades.



## Local Development

1. Clone the repo (or fork the repo to your account)
1. Install dependencies: `bundle install`
1. Create a feature branch off of the `dev` branch
1. Start the local server: `bundle exec jekyll serve`
1. Go to <http://localhost:4400/> to view changes


To build the site use `python3 generate_pages.py && bundle exec jekyll build`.

Resources:

- [Jekyll Docs](https://jekyllrb.com/docs/)
- [Liquid Syntax](https://shopify.github.io/liquid/basics/introduction/)



## Contributing

For updating the site to a new upgrade:

1. Duplicate the most recent upgrade's data file in `site/_data`
1. Rename the file with the upcoming upgrade's name following the `{{upgrade_name}}-{{network}}` convention
1. Update the info within the data file
1. Update the info in `_config.yml`

