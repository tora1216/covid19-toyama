today=`date "+%Y%m%d"`
cd /root/covid19-toyama/
git pull origin development
cd tool
curl -O "http://opendata.pref.toyama.jp/files/covid19/${today}/toyama_patients.csv"
curl -O "http://opendata.pref.toyama.jp/files/covid19/${today}/toyama_counts.csv"
python test.py
git add *
git commit -m "Data Update ${today}"
git push origin development
