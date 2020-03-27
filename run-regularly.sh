today=`date "+%Y/%m/%d %H/%M"`
python3 tool/scraping.py
git add .
git commit -m "データ更新${today}"
git push origin development
