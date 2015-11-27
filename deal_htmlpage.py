# coding = utf-8

from bs4 import BeautifulSoup

html_doc = """
<html>
<head>
<title>this is the test</title>
</head>
<body>
<p>Alice's dream</p>
<a href="#">1</a>
<a href="#">2</a>
<a href="#">3</a>
</body>
</html>
"""

soup = BeautifulSoup(html_doc)

print(soup.prettify())
#输出文档结构
