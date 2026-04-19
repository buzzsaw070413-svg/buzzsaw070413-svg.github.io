import webbrowser
import os

html_content = """
<!DOCTYPE html>
<html>
<head>
<title>My Docs</title>
<style>
    body {
        margin: 0;
        background: #f1f3f4;
        font-family: Arial, sans-serif;
    }

    .toolbar {
        background: white;
        padding: 10px;
        border-bottom: 1px solid #ddd;
        font-size: 18px;
        font-weight: bold;
    }

    .editor {
        max-width: 800px;
        margin: 40px auto;
        background: white;
        padding: 40px;
        min-height: 80vh;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        outline: none;
        font-size: 16px;
        line-height: 1.6;
    }
</style>
</head>
<body>

<div class="toolbar">Untitled Document</div>

<div class="editor" contenteditable="true">
test
</div>

</body>
</html>
"""

# Save file
file_path = os.path.abspath("doc_editor.html")
with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

# Open in browser
webbrowser.open("file://" + file_path)
