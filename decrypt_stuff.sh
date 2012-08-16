rm -rf uploads data.db
cp -r simple_server/uploads uploads
python data_processing/dbdecrypt.py -k changeme uploads/*.db
python data_processing/dbmerge.py uploads/*.db -o data.db
rm -rf uploads
