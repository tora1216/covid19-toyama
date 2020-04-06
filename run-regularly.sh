today=`date "+%Y/%m/%d %H:%M"`
cd /root/covid19-toyama/
git pull origin development
python3 /root/covid19-toyama/tool/test.py
git add .
git commit -m "自動更新テスト${today}"
git push origin development
