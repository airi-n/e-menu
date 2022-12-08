from django import template
register = template.Library()
import pykakasi



@register.filter
def hebon(string):
    kakasi = pykakasi.kakasi()  # インスタンスの作成
    kakasi.setMode('H', 'a')  # ひらがなをローマ字に変換するように設定
    kakasi.setMode('K', 'a')  # カタカナをローマ字に変換するように設定
    kakasi.setMode('J', 'a')  # 漢字をローマ字に変換するように設定
    conversion = kakasi.getConverter()
    return conversion.do(string)
