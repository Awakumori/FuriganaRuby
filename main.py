import re
import webbrowser
import os


def create_html_with_ruby(text, output_html_path="japanese_with_furigana.html"):
    """
    将带括号的日文文本转换为带有ruby标签的HTML

    参数:
    text (str): 包含日文和括号内注音的文本，如"色褪(いろあ)せた"
    output_html_path (str): 输出HTML文件的路径

    返回:
    str: 生成的HTML文件路径
    """
    # 正则表达式用于匹配汉字和注音
    pattern = r'([一-龯々]+)\(([ぁ-んァ-ンー]+)\)'

    # 找到上一个匹配结束的位置
    last_end = 0

    # HTML头部
    html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Japanese Text with Furigana</title>
    <style>
        body {
            font-family: "MS Mincho", "ＭＳ 明朝", serif;
            font-size: 14pt;
            line-height: 2;
        }
        ruby {
            ruby-align: center;
        }
        rt {
            font-size: 8pt;
            line-height: 1;
        }
    </style>
</head>
<body>
"""

    # 处理文本中的每一个匹配
    for match in re.finditer(pattern, text):
        # 添加匹配前的普通文本
        if match.start() > last_end:
            text_before = text[last_end:match.start()]
            if text_before:
                # 将换行符转换为HTML的<br>标签
                text_before = text_before.replace('\n', '<br>\n')
                html_content += text_before

        # 添加带注音的汉字
        kanji = match.group(1)
        reading = match.group(2)
        html_content += f'<ruby>{kanji}<rt>{reading}</rt></ruby>'

        # 更新上一个匹配结束的位置
        last_end = match.end()

    # 添加最后一个匹配后的普通文本
    if last_end < len(text):
        text_after = text[last_end:]
        if text_after:
            # 将换行符转换为HTML的<br>标签
            text_after = text_after.replace('\n', '<br>\n')
            html_content += text_after

    # HTML尾部
    html_content += """
</body>
</html>"""

    # 保存HTML文件
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    return output_html_path


# 主函数
if __name__ == "__main__":
    # 示例文本
    sample_text = \
        """
        色褪(いろあ)せた感情(かんじょう)を切(き)り離(はな)すため
刻(きざ)まれた点線(てんせん)を指(ゆび)でなぞるよ
泣(な)けるほど簡単(かんたん)に出来(でき)てしまうから
難(むずか)しく考(かんが)えず千切(ちぎ)ればいいの

それは昨日(きのう)の朝(あさ)まで僕(ぼく)の内側(うちがわ)にあったのに
気(き)がつけば今(いま)は目(め)の前(まえ)で転(ころ)がっているんだ

感情論(かんじょうろん)で切(き)り取(と)った 未完成(みかんせい)で曖昧(あいまい)な恋(こい)の色(いろ)は
山折(やまおり) 谷折(たにおり) 皺(しわ)くちゃになってた
「関係(かんけい)ない」って割(わ)り切(き)って ゴミ箱(ばこ)に捨(す)てられたなら
切(き)り取(と)られてゆく 昨日流(きのうなが)した涙(なみだ)

閉(と)じ込(こ)めた感情(かんじょう)を解(と)き放(はな)すため
こじ開(あ)けた確信犯(かくしんはん) 声(こえ)を潜(ひそ)めて
作(つく)られた偶然(ぐうぜん)も信(しん)じた嘘(うそ)も
諦(あきら)めた瞬間(しゅんかん)に色(いろ)を変(か)えるの

要(い)らない記憶(きおく)を排除(はいじょ)して 重(おも)たい荷物投(にもつな)げ出(だ)して
そこに残(のこ)されたものは弱(よわ)い自分(じぶん)だけ

それは昨日(きのう)の夜(よる)まで綺麗(きれい)な思(おも)い出(で)だったのに
気(き)がつけば今(いま)は名前(なまえ)さえ思(おも)い出(だ)せないの

感情論(かんじょうろん)で切(き)り取(と)った 未完成(みかんせい)で曖昧(あいまい)な恋(こい)の色(いろ)は
山折(やまおり) 谷折(たにおり) 皺(しわ)くちゃになってた
「関係(かんけい)ない」って割(わ)り切(き)って ゴミ箱(ばこ)に捨(す)てられたなら
切(き)り取(と)られてゆく 昨日流(きのうなが)した涙(なみだ)

切(き)り取(と)られてゆく 昨日愛(きのうあい)した人(ひと)




        """

    # 生成HTML
    html_path = create_html_with_ruby(sample_text)
    print(f"HTML文件已生成: {html_path}")

    # 自动在浏览器中打开HTML文件
    absolute_path = os.path.abspath(html_path)
    webbrowser.open('file://' + absolute_path, new=2)