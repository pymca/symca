
import html

user_input = input("Enter your name or message: ")

safe_output = html.escape(user_input)

html_page = f"""
<h2>User Message</h2>
<p>{safe_output}</p>
"""

print("\nGenerated Safe HTML:")
print(html_page)
