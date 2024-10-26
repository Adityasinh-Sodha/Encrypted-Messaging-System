const encodedMapping = "eyJBIjogIjQ2ODAyNyIsICJCIjogIjkxMDM2NCIsICJDIjogIjU4MDAzMSIsICJEIjogIjI3MDQ1NiIsICJFIjogIjM5MjA3MCIsICJGIjogIjgwMDUxOSIsICJHIjogIjcyMDUzMSIsICJIIjogIjE0MDY5MCIsICJJIjogIjYzMDcyNCIsICJKIjogIjk1MDAxMiIsICJLIjogIjMwODE3NiIsICJMIjogIjU3MDM4MiIsICJNIjogIjgxMDk0NyIsICJOIjogIjIwMDUzOCIsICJPIjogIjcwMTYyNSIsICJQIjogIjM5MDQ3MCIsICJRIjogIjg1MDA2MSIsICJSIjogIjE2MDI1OSIsICJTIjogIjMwOTU2MiIsICJUIjogIjQ3MDgzNiIsICJVIjogIjkzNjAwMSIsICJWIjogIjcwMDIzNSIsICJXIjogIjQxMDU3OCIsICJYIjogIjYwODAyNSIsICJZIjogIjI4MzEwNSIsICJaIjogIjc1MDk2MCIsICIgIjogIjU0MDI2MyIsICJhIjogIjIwNDg5NiIsICJiIjogIjYxMDQ1MiIsICJjIjogIjkzNTIwMSIsICJkIjogIjQwNzYxMyIsICJlIjogIjkxNTAyNCIsICJmIjogIjIwMzc4NiIsICJnIjogIjU5ODA2MSIsICJoIjogIjE3MDM0OSIsICJpIjogIjY4NTAxOSIsICJqIjogIjQwMjM1NyIsICJrIjogIjc5MDUxMCIsICJsIjogIjMxMDIwNCIsICJtIjogIjU5MDA4MSIsICJuIjogIjIwMDYzOCIsICJvIjogIjcxMDQ5MiIsICJwIjogIjMwNjg1NyIsICJxIjogIjk4MDAxNSIsICJyIjogIjY0MDEyNSIsICJzIjogIjUzMDA5OCIsICJ0IjogIjc4MDUwMyIsICJ1IjogIjYxMDA5MiIsICJ2IjogIjQwODUxMyIsICJ3IjogIjI3OTA2MSIsICJ4IjogIjUwODMwOSIsICJ5IjogIjMwNDYxMiIsICJ6IjogIjgwMjc0NSIsICIxIjogIjYzODA5MSIsICIyIjogIjU5MTA0NyIsICIzIjogIjgyMDQwMCIsICI0IjogIjM1NzkwMiIsICI1IjogIjE5NDYwNyIsICI2IjogIjc1MDAzMSIsICI3IjogIjUwMDM4MiIsICI4IjogIjgxMDYyNSIsICI5IjogIjIzOTA4NCIsICIwIjogIjU3MDEzNiIsICIhIjogIjkyMDcwNCIsICJAIjogIjQ2MjUwMSIsICIjIjogIjcxNTM5MCIsICIkIjogIjg0NjMwMiIsICIlIjogIjM1OTAyNCIsICJeIjogIjE4MDIzNiIsICImIjogIjUwMDEyOCIsICIqIjogIjc5MzAxNSIsICIoIjogIjYyODcwNSIsICIpIjogIjQzNzE5MCIsICJfIjogIjM2MjA0MCIsICIiOiAiNTAyODAxIiwgIi0iOiAiMjA0NjM5IiwgIj0iOiAiOTEwNTgzIiwgIn4iOiAiNzgzMDE1IiwgInsiOiAiNjE5MzUwIiwgIn0iOiAiNDcwODI2IiwgIlsiOiAiMjUwOTYzIiwgIl0iOiAiODYwMzE1IiwgIjoiOiAiNjkwMjQ4IiwgIjsiOiAiMTA2Mjk0IiwgIiciOiAiOTcwMDM1IiwgIj4iOiAiNTQxMDgyIiwgIj8iOiAiMzAyODU3IiwgIjwiOiAiNDc1OTAzIiwgIiwiOiAiNjAzOTIxIiwgIi4iOiAiNTE4MzA3IiwgIi8iOiAiMjA2NDc5IiwgInwiOiAiNTA3MzkxIiwgIisiOiAiNjc0NTM0IiwgIlwiIjogIjkyODYwMyIsICJcXCI6ICIxNTczMDkiLCAiYCI6ICIxMDEwMTAifQ=="; 




const customMapping = JSON.parse(atob(encodedMapping));

function encodeText(text, mapping) {
    let encodedChars = [];
    for (let char of text) {
        let encodedChar = mapping[char];
        encodedChars.push(encodedChar !== undefined ? encodedChar : char);
    }
    return encodedChars.join('');
}

function decodeText(encodedText, mapping) {
    let reverseMapping = Object.fromEntries(Object.entries(mapping).map(([key, value]) => [value, key]));
    let decodedText = [];
    let encodedSequence = "";

    for (let char of encodedText) {
        encodedSequence += char;
        let decodedChar = reverseMapping[encodedSequence];
        if (decodedChar !== undefined) {
            decodedText.push(decodedChar);
            encodedSequence = "";
        }
    }
    return decodedText.join('');
}

document.getElementById("encode-text").addEventListener("input", function() {
    let textToEncode = this.value.trim();
    let encodedText = encodeText(textToEncode, customMapping);
    let encodedTextBox = document.getElementById("encoded-text");
    encodedTextBox.value = encodedText;
    

    encodedTextBox.scrollLeft = encodedTextBox.scrollWidth;
});

function decodeTextInput() {
    let encodedText = document.getElementById("decode-text").value.trim();
    if (encodedText) {
        let decodedText = decodeText(encodedText, customMapping);
        document.getElementById("decoded-text").value = decodedText;
        document.getElementById("decode-text").value = "";  
    } else {
        console.log("No encoded text provided!");
    }
}

function copyToClipboard() {
    let encodedText = document.getElementById("encoded-text").value;
    navigator.clipboard.writeText(encodedText).then(() => {
        console.log("Text copied to clipboard");
    }).catch(err => {
        console.error("Failed to copy text: ", err);
    });
}
