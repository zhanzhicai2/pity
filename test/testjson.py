# encoding: utf-8
# @File  : testjson.py
# @Author: zhanzhicai
# @Desc : 
# @Date  :  2024/12/10


import json


class JsonCompare:

    def compare(self, exp, act):
        ans = []
        self._compare(exp, act, ans, '')
        return ans

    def _compare(self, a, b, ans, path):
        a = self._to_json(a)
        b = self._to_json(b)
        if type(a) != type(b):
            ans.append(f"{path} 类型不一致, 分别为{type(a)} {type(b)}")
            return
        if isinstance(a, dict):
            keys = []
            for key in a.keys():
                pt = path + "/" + key
                if key in b.keys():
                    self._compare(a[key], b[key], ans, pt)
                    keys.append(key)
                else:
                    ans.append(f"{pt} 在后者中不存在")
            for key in b.keys():
                if key not in keys:
                    pt = path + "/" + key
                    ans.append(f"{pt} 在后者中多出")
        elif isinstance(a, list):
            i = j = 0
            while i < len(a):
                pt = path + "/" + str(i)
                if j >= len(b):
                    ans.append(f"{pt} 在后者中不存在")
                    i += 1
                    j += 1
                    continue
                self._compare(a[i], b[j], ans, pt)
                i += 1
                j += 1
            while j < len(b):
                pt = path + "/" + str(j)
                ans.append(f"{pt} 在前者中不存在")
                j += 1
        else:
            if a != b:
                ans.append(
                    f"{path} 数据不一致: {a} "
                    f"!= {b}" if path != "" else
                    f"数据不一致: {a} != {b}")

    def _color(self, text, _type=0):
        if _type == 0:
            # 说明是绿色
            return """<span style="color: #13CE66">{}</span>""".format(text)
        return """<span style="color: #FF4949">{}</span>""".format(text)

    def _weight(self, text):
        return """<span style="font-weight: 700">{}</span>""".format(text)

    def _to_json(self, string):
        try:
            float(string)
            return string
        except:
            try:
                if isinstance(string, str):
                    return json.loads(string)
                return string
            except:
                return string


if __name__ == "__main__":
    # 预期结果
    a = """
    {
    	"name": "lixiaoyao",
    	"wife": ["linyueru", "zhaolinger"],
    	"job": {
    		"yuhang": "混混",
    		"suzhou": "林家堡姑爷",
    		"suoyaota": "仙剑派弟子"
    	}
    }
    """

    # 实际结果
    b = """
    {
    	"name": "lixiaoyao",
    	"age": 23,
    	"wife": ["anu", "zhaolinger"],
    	"job": {
    		"yuhang": "混混",
    		"suzhou": "林家堡姑爷",
    		"suoyaota": "仙剑派子弟"
    	}
    }
    """
    obj = JsonCompare()
    ans = obj.compare(a, b)
    print(ans)
