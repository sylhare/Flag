sudo mkdir -p /etc/opt/chrome/native-messaging-hosts/
sudo cp ./ctf.neurosoft.neuropass.json /etc/opt/chrome/native-messaging-hosts/
sudo chmod a+r /etc/opt/chrome/native-messaging-hosts/ctf.neurosoft.neuropass.json

sudo mkdir -p /opt/neurosoft/data
sudo chmod a+w /opt/neurosoft/data
sudo chmod +x ./neuropass
sudo cp neuropass /opt/neurosoft

echo 'CREATE TABLE passwords ( id INTEGER PRIMARY KEY, domain text NOT NULL, user text NOT NULL, pass text NOT NULL );' | sqlite3 /opt/neurosoft/data/db
