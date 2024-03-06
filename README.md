# Beijing Air Quality Analysis

## Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run steamlit app
```
streamlit run dashboard.py
```


This repository is for Dicoding Course submission which try to answer this question

Problem Statement:
Partikel matter, umumnya disingkat sebagai PM dan digunakan sebagai ukuran polusi udara, secara signifikan memengaruhi masyarakat. Meskipun partikel dengan diameter 10 mikron atau kurang (≤PM10) dapat menembus dan terbenam dalam paru-paru, yang lebih berbahaya bagi kesehatan adalah yang memiliki diameter 2,5 mikron atau kurang (≤PM2.5). Maka dari itu muncul 3 pertanyaan

1. Bagaimana perubahan tingkatan PM2.5 dalam tahun, bulan, dan hari?
2. Apa hubungan variabel SO2, NO2, dan CO terhadap perubahan tingkatan PM?
3. Stasiun manakah yang memiliki tingkat polutan terendah dan tertinggi?

The dasboard can be viewed trough the website below
The link : https://beijingair.streamlit.app/

Created by Gery Jonathan 