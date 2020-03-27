today=`date "+%Y/%m/%d %H:%M"`
git pull origin development
python3 /home/sakura/covid19-ishikawa/tool/scraping-cent.py
git add .
git commit -m "データ更新${today}"
git push origin development
