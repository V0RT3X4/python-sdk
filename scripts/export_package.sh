#!/usr/bin/env bash
set -e

# Tag the current commit
TAG=$(python setup.py --version)

git add setup.py
git commit -m "chore: New tag $TAG"
git push

git tag -a $TAG -m "chore: New tag $TAG"
git push --tags


# Generate changelog
#gem install github_changelog_generator
github_changelog_generator -u V0RT3X4 -p python-sdk -t $GITHUB_CHANGELOG_TOKEN
git add CHANGELOG.md
git commit -m "docs: Update changelog with tag $TAG"
git push


# Push new version to pypi
. venv/bin/activate
rm -rf dist
pip install wheel
python3 setup.py sdist bdist_wheel
python3 -m twine upload -u $TWINE_USERNAME -p $TWINE_PASSWORD dist/*

# Deploy Docs
./docs/deploy_docs.sh
