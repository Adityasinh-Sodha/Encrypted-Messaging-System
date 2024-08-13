import tkinter as tk
import base64
import json


encoded_mapping = "eyJBIjogIjQ2ODAyNyIsICJCIjogIjkxMDM2NCIsICJDIjogIjU4MDAzMSIsICJEIjogIjI3MDQ1NiIsICJFIjogIjM5MjA3MCIsICJGIjogIjgwMDUxOSIsICJHIjogIjcyMDUzMSIsICJIIjogIjE0MDY5MCIsICJJIjogIjYzMDcyNCIsICJKIjogIjk1MDAxMiIsICJLIjogIjMwODE3NiIsICJMIjogIjU3MDM4MiIsICJNIjogIjgxMDk0NyIsICJOIjogIjIwMDUzOCIsICJPIjogIjcwMTYyNSIsICJQIjogIjM5MDQ3MCIsICJRIjogIjg1MDA2MSIsICJSIjogIjE2MDI1OSIsICJTIjogIjMwOTU2MiIsICJUIjogIjQ3MDgzNiIsICJVIjogIjkzNjAwMSIsICJWIjogIjcwMDIzNSIsICJXIjogIjQxMDU3OCIsICJYIjogIjYwODAyNSIsICJZIjogIjI4MzEwNSIsICJaIjogIjc1MDk2MCIsICIgIjogIjU0MDI2MyIsICJhIjogIjIwNDg5NiIsICJiIjogIjYxMDQ1MiIsICJjIjogIjkzNTIwMSIsICJkIjogIjQwNzYxMyIsICJlIjogIjkxNTAyNCIsICJmIjogIjIwMzc4NiIsICJnIjogIjU5ODA2MSIsICJoIjogIjE3MDM0OSIsICJpIjogIjY4NTAxOSIsICJqIjogIjQwMjM1NyIsICJrIjogIjc5MDUxMCIsICJsIjogIjMxMDIwNCIsICJtIjogIjU5MDA4MSIsICJuIjogIjIwMDYzOCIsICJvIjogIjcxMDQ5MiIsICJwIjogIjMwNjg1NyIsICJxIjogIjk4MDAxNSIsICJyIjogIjY0MDEyNSIsICJzIjogIjUzMDA5OCIsICJ0IjogIjc4MDUwMyIsICJ1IjogIjYxMDA5MiIsICJ2IjogIjQwODUxMyIsICJ3IjogIjI3OTA2MSIsICJ4IjogIjUwODMwOSIsICJ5IjogIjMwNDYxMiIsICJ6IjogIjgwMjc0NSIsICIxIjogIjYzODA5MSIsICIyIjogIjU5MTA0NyIsICIzIjogIjgyMDQwMCIsICI0IjogIjM1NzkwMiIsICI1IjogIjE5NDYwNyIsICI2IjogIjc1MDAzMSIsICI3IjogIjUwMDM4MiIsICI4IjogIjgxMDYyNSIsICI5IjogIjIzOTA4NCIsICIwIjogIjU3MDEzNiIsICIhIjogIjkyMDcwNCIsICJAIjogIjQ2MjUwMSIsICIjIjogIjcxNTM5MCIsICIkIjogIjg0NjMwMiIsICIlIjogIjM1OTAyNCIsICJeIjogIjE4MDIzNiIsICImIjogIjUwMDEyOCIsICIqIjogIjc5MzAxNSIsICIoIjogIjYyODcwNSIsICIpIjogIjQzNzE5MCIsICJfIjogIjM2MjA0MCIsICIiOiAiNTAyODAxIiwgIi0iOiAiMjA0NjM5IiwgIj0iOiAiOTEwNTgzIiwgIn4iOiAiNzgzMDE1IiwgInsiOiAiNjE5MzUwIiwgIn0iOiAiNDcwODI2IiwgIlsiOiAiMjUwOTYzIiwgIl0iOiAiODYwMzE1IiwgIjoiOiAiNjkwMjQ4IiwgIjsiOiAiMTA2Mjk0IiwgIiciOiAiOTcwMDM1IiwgIj4iOiAiNTQxMDgyIiwgIj8iOiAiMzAyODU3IiwgIjwiOiAiNDc1OTAzIiwgIiwiOiAiNjAzOTIxIiwgIi4iOiAiNTE4MzA3IiwgIi8iOiAiMjA2NDc5IiwgInwiOiAiNTA3MzkxIiwgIisiOiAiNjc0NTM0IiwgIlwiIjogIjkyODYwMyIsICJcXCI6ICIxNTczMDkiLCAiYCI6ICIxMDEwMTAifQ=="

custom_mapping = json.loads(base64.b64decode(encoded_mapping).decode())

def encode_text(text, mapping):
    encoded_chars = []
    for char in text:
        if (encoded_char := mapping.get(char)) is not None:
            encoded_chars.append(encoded_char)
        else:
            encoded_chars.append(char)
    return ''.join(encoded_chars)

def decode_text(encoded_text, mapping):
    reverse_mapping = {value: key for key, value in mapping.items()}
    decoded_text = []
    encoded_sequence = ""
    
    for char in encoded_text:
        encoded_sequence += char
        if (decoded_char := reverse_mapping.get(encoded_sequence)) is not None:
            decoded_text.append(decoded_char)
            encoded_sequence = ""
    
    return ''.join(decoded_text)

def on_encode(event):
    text_to_encode = encode_entry.get("1.0", tk.END).strip()
    encoded_text = encode_text(text_to_encode, custom_mapping)
    encoded_text_var.set(encoded_text)

def on_decode():
    try:
        clipboard_text = root.clipboard_get().strip()
        if clipboard_text:
            decode_entry.delete(0, tk.END)
            decode_entry.insert(tk.END, clipboard_text)
            decoded_text = decode_text(clipboard_text, custom_mapping)
            decoded_entry.delete("1.0", tk.END)
            decoded_entry.insert(tk.END, decoded_text)
        else:
            print("Clipboard is empty!")
    except tk.TclError:
        print("Failed to get clipboard content. Make sure it is not empty.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(encoded_text_var.get())

root = tk.Tk()
root.title("Text Encoder and Decoder")

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
root.columnconfigure(2, weight=1)

tk.Label(root, text="Enter text to encode:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
encode_text_var = tk.StringVar()
encode_entry = tk.Text(root, height=5, width=50)
encode_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
encode_entry.bind("<KeyRelease>", on_encode)

tk.Label(root, text="Encoded Text:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
encoded_text_var = tk.StringVar()
encoded_entry = tk.Entry(root, textvariable=encoded_text_var, state='readonly')
encoded_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
tk.Button(root, text="Copy", command=copy_to_clipboard).grid(row=1, column=3, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Enter encoded text to decode:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
decode_entry = tk.Entry(root)
decode_entry.grid(row=2, column=1, columnspan=2, padx=10, pady=10, sticky="ew")
tk.Button(root, text="Paste & Decode", command=on_decode).grid(row=2, column=3, padx=10, pady=10, sticky="ew")

tk.Label(root, text="Decoded Text:").grid(row=3, column=0, padx=10, pady=10, sticky="w")
decoded_entry = tk.Text(root, height=5, width=50)
decoded_entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

for row in range(4):
    root.rowconfigure(row, weight=1)

root.mainloop()
