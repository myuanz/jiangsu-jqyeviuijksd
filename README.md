# jiangsu-jqyeviuijksd
http://www.91job.org.cn/default/contest 的自动做题工具

仅供 Python 和 HTTP 相关知识的学习交流只用, 勿用于其他途径, 作者不承担任何连带责任

## 直接使用本项目
1. 正常安装 Python3.7, 由于用到了`tensorflow`只能固定在此版本. 
2. `python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple jiangsu-jqyeviuijksd`
3. `js-job answer-question -u <your-id> -p <your-password> -s <your-school>`

## 如果用于研究
1. `git clone https://github.com/myuanz/jiangsu-jqyeviuijksd`
2. `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple poetry`
3. `poetry install`
4. `从 console.py 开始读`

--- 
## 其他使用

## 如何获取所有学校前缀?
在 http://www.91job.org.cn/default/contest 控制台运行以下代码获取
```javascript
JSON.stringify($x('//ul/li/a').map(elem => ({
    [elem.href.split('.')[0].slice('http://'.length)]: elem.text
})).reduce((acc, item) => Object.assign(acc, item)))
```
<details>
<summary>所有学校前缀</summary>

```JSON
{
    "nju": "南京大学",
    "seu": "东南大学",
    "nuaa": "南京航空航天大学",
    "njust": "南京理工大学",
    "njtech": "南京工业大学",
    "njupt": "南京邮电大学",
    "hhu": "河海大学",
    "njfu": "南京林业大学",
    "nuist": "南京信息工程大学",
    "njau": "南京农业大学",
    "njmu": "南京医科大学",
    "njucm": "南京中医药大学",
    "cpu": "中国药科大学",
    "njnu": "南京师范大学",
    "njue": "南京财经大学",
    "jspi": "江苏警官学院",
    "nipes": "南京体育学院",
    "nua": "南京艺术学院",
    "niit": "南京工业职业技术大学",
    "sju": "三江学院",
    "njit": "南京工程学院",
    "nau": "南京审计大学",
    "njxzc": "南京晓庄学院",
    "jvic": "江苏经贸职业技术学院",
    "njty": "南京特殊教育师范学院",
    "forestpolice": "南京森林警察学院",
    "juti": "江苏联合职业技术学院",
    "jmi": "江苏海事职业技术学院",
    "ytc": "应天职业技术学院",
    "cxxy": "东南大学成贤学院",
    "njci": "南京交通职业技术学院",
    "njpi": "南京科技职业学院",
    "zdxy": "正德职业技术学院",
    "zscollege": "钟山职业技术学院",
    "jku": "金肯职业技术学院",
    "nty": "南京铁道职业技术学院",
    "njcit": "南京信息职业技术学院",
    "jit": "金陵科技学院",
    "jlxy": "南京大学金陵学院",
    "zijin": "南京理工大学紫金学院",
    "nuaajc": "南京航空航天大学金城学院",
    "cucn": "中国传媒大学南广学院",
    "njpji": "南京工业大学浦江学院",
    "njnuzb": "南京师范大学中北学院",
    "niva": "南京视觉艺术职业学院",
    "bjxy": "南京信息工程大学滨江学院",
    "naujsxy": "南京审计大学金审学院",
    "jscvc": "江苏城市职业学院",
    "ncc": "南京城市职业学院",
    "nimt": "南京机电职业技术学院",
    "nith": "南京旅游职业学院",
    "jssmu": "江苏卫生健康职业学院",
    "jsie": "江苏第二师范学院",
    "jiangnan": "江南大学",
    "wxit": "无锡职业技术学院",
    "wxstc": "无锡科技职业学院",
    "wxic": "无锡商业职业技术学院",
    "wsoc": "无锡南洋职业技术学院",
    "jnys": "江南影视艺术职业学院",
    "jsit": "江苏信息职业技术学院",
    "jypc": "江阴职业技术学院",
    "thxy": "无锡太湖学院",
    "wxcu": "无锡城市职业技术学院",
    "wxgy": "无锡工艺职业技术学院",
    "cumt": "中国矿业大学",
    "xzhmu": "徐州医科大学",
    "jsnu": "江苏师范大学",
    "jsjzi": "江苏建筑职业技术学院",
    "xzit": "徐州工程学院",
    "jzp": "九州职业技术学院",
    "xzcit": "徐州工业职业技术学院",
    "cumtxhc": "中国矿业大学徐海学院",
    "xznukwxy": "江苏师范大学科文学院",
    "xzyz": "徐州幼儿师范高等专科学校",
    "xzsw": "徐州生物工程职业技术学院",
    "jsvist": "江苏安全技术职业学院",
    "cczu": "常州大学",
    "czu": "常州工学院",
    "jsut": "江苏理工学院",
    "ccit": "常州信息职业技术学院",
    "czwyxx": "常州艺术高等职业学校",
    "cztgi": "常州纺织服装职业技术学院",
    "czgyxy": "常州工业职业技术学院",
    "czie": "常州工程职业技术学院",
    "czjdu": "建东职业技术学院",
    "czimt": "常州机电职业技术学院",
    "js-cj": "江苏城乡建设职业学院",
    "suda": "苏州大学",
    "usts": "苏州科技大学",
    "sgmart": "苏州工艺美术职业技术学院",
    "jssvc": "苏州市职业大学",
    "szit": "沙洲职业工学院",
    "usl": "硅湖职业技术学院",
    "szjm": "苏州经贸职业技术学院",
    "siit": "苏州工业职业技术学院",
    "szetop": "苏州托普信息职业技术学院",
    "szmtc": "苏州卫生职业技术学院",
    "szai": "苏州农业职业技术学院",
    "ivt": "苏州工业园区职业技术学院",
    "wjxvtc": "苏州健雄职业技术学院",
    "hkuspace": "苏州百年职业学院",
    "ksdy": "昆山登云科技职业学院",
    "sdwz": "苏州大学文正学院",
    "sudatec": "苏州大学应用技术学院",
    "uststpxy": "苏州科技大学天平学院",
    "szlg": "江苏科技大学苏州理工学院",
    "gist": "苏州高博软件技术职业学院",
    "szitu": "苏州信息职业技术学院",
    "siso": "苏州工业园区服务外包职业学院",
    "szys": "苏州幼儿师范高等专科学校",
    "cslg": "常熟理工学院",
    "ntu": "南通大学",
    "jcet": "江苏工程职业技术学院",
    "ntvu": "南通职业大学",
    "ntpc": "南通理工学院",
    "ntst": "南通科技职业学院",
    "ntsc": "江苏航运职业技术学院",
    "xlxy": "南通大学杏林学院",
    "jsbc": "江苏商贸职业学院",
    "ntnc": "南通师范高等专科学校",
    "lygtc": "连云港职业技术学院",
    "lygsf": "连云港师范高等专科学校",
    "jou": "江苏海洋大学",
    "njmukdc": "南京医科大学康达学院",
    "jscfa": "江苏财会职业学院",
    "hytc": "淮阴师范学院",
    "hyit": "淮阴工学院",
    "jsei": "江苏电子信息职业学院",
    "jsfsc": "江苏食品药品职业技术学院",
    "jscjxy": "江苏财经职业技术学院",
    "jshl": "江苏护理职业学院",
    "ycit": "盐城工学院",
    "yctu": "盐城师范学院",
    "jyzx": "明达职业技术学院",
    "ycmc": "江苏医药职业学院",
    "yctei": "盐城工业职业技术学院",
    "yyz": "盐城幼儿师范高等专科学校",
    "yzu": "扬州大学",
    "yzpc": "扬州市职业大学",
    "yzerc": "扬州环境资源职业技术学院",
    "jhu": "江海职业技术学院",
    "ypi": "扬州工业职业技术学院",
    "yzuglxy": "扬州大学广陵学院",
    "tdxynjupt": "南京邮电大学通达学院",
    "jstc": "江苏旅游职业学院",
    "just": "江苏科技大学",
    "ujs": "江苏大学",
    "zjc": "镇江市高等专科学校",
    "jssfjx": "江苏省司法警官高等职业学校",
    "jsafc": "江苏农林职业技术学院",
    "jinshan": "金山职业技术学院",
    "ujsjjxy": "江苏大学京江学院",
    "nufehs": "南京财经大学红山学院",
    "jatc": "江苏航空职业技术学院",
    "tzpc": "泰州职业技术学院",
    "jsahvc": "江苏农牧科技职业学院",
    "tzu": "泰州学院",
    "nustti": "南京理工大学泰州科技学院",
    "nnutc": "南京师范大学泰州学院",
    "hlxy": "南京中医药大学翰林学院",
    "cczuhdc": "常州大学怀德学院",
    "cjsiu": "宿迁职业技术学院",
    "sqc": "宿迁学院"
}
```
</details>


## 如何获取题目?
```shell script
> js-job get-question-and-save --help
仅供 Python 和 HTTP 相关知识的学习交流只用, 勿用于其他途径, 作者不承担任何连带责任

Usage: js-job get-question-and-save [OPTIONS]

  获取答案并保存, 需特殊条件, 除研究外勿用

Options:
  -u TEXT  学号  [required]
  -p TEXT  密码  [required]
  -s TEXT  学校名  [required]
  --help   Show this message and exit.
```
## 如何自动登录?
```shell script
> js-job get-sess --help
仅供 Python 和 HTTP 相关知识的学习交流只用, 勿用于其他途径, 作者不承担任何连带责任

Usage: js-job get-sess [OPTIONS]

  使用用户名和密码获取会话, 自动计算验证码

Options:
  -u TEXT  学号  [required]
  -p TEXT  密码  [required]
  -s TEXT  学校名  [required]
  --help   Show this message and exit.
```