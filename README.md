```
C:\Windows\System32\drivers\etc
```

### 生成图片
```
for i in {1..20}
do
	magick -gravity center -background white -fill black -size 400x400 -font /System/Library/Fonts/Supplemental/AmericanTypewriter.ttc caption:"$i" "image ($i).png"
done
```

### 性别尺码信息 女款 男款 情侣款
```
EU36,EU365,EU37,EU38,EU385,EU39
EU40,EU405,EU41,EU42,EU425,EU43,EU44,EU445,EU45,EUR46
EU36,EU365,EU37,EU38,EU385,EU39,EU40,EU405,EU41,EU42,EU425,EU43,EU44,EU445,EU45,EUR46
```
