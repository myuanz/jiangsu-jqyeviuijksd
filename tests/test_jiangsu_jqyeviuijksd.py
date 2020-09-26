from jiangsu_jqyeviuijksd import __version__
from jiangsu_jqyeviuijksd.get_question import Question


def test_version():
    assert __version__ == "0.1.0"


def test_question():
    json = """
[
    {
        "id": "510",
        "title": "第529题(判断)",
        "type": "radio",
        "topic": "霍兰德的职业兴趣理论主要从兴趣的角度出发来探索职业指导的问题。",
        "right": "A",
        "know": "",
        "answers": [
            {
                "id": "A",
                "title": "【A】 正确",
                "subId": "510"
            },
            {
                "id": "B",
                "title": "【B】 错误",
                "subId": "510"
            }
        ]
    },
    {
        "id": "512",
        "title": "第530题(判断)",
        "type": "radio",
        "topic": "面对突如其来的疫情，大家瞬间丧失大量资源，失去了对生活的掌控感和安全感，身心都会发生系列变化，这些反应通常表现为一般的身心问题，这也是人在面对灾难时的正常反应，心理学上称之为应激反应。",
        "right": "A",
        "know": "",
        "answers": [
            {
                "id": "A",
                "title": "【A】 正确",
                "subId": "512"
            },
            {
                "id": "B",
                "title": "【B】 错误",
                "subId": "512"
            }
        ]
    }
]
    """
    print(Question.from_json(json))
