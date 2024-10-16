import streamlit as st 

st.title("내가 만든 앱")

markdown_text = """ 
# This is a Header

## This is a Subheader

You can write normal text here.

* This is a bullet point 
* Another bullet point

1. Numbered list item 1 
2. Numbered list item 2

**Bold text** and *italic text*

[This is a link](https://www.streamlit.io)

Here's a code block: 
```python
def hello_world():
print("Hello, World!") 
```

And here's a table:

|Column1|Column2| 
|----------|----------| 
|Row1 |Value1 | 
|Row2 |Value2 |

> This is a blockquote

---

![Cute Cat](https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_November_2010-1a.jpg) 

---

"""

st.markdown(markdown_text)

