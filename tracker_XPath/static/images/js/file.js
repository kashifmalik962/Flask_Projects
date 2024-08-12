

const options = {
    method: 'POST', // HTTP method
    headers: {
        'Content-Type': 'application/json' // Content type
    },
    body: JSON.stringify(data) // Convert data to JSON string
};

// Sending the data using fetch
fetch('/save_xpath', options)
    .then(response => {
        if (!response.ok) {
            // Handle HTTP errors
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json(); // Parse the JSON response
    })
    .then(data => {
        // Handle the response data
        console.log('Success:', data);
    })
    .catch(error => {
        // Handle errors
        console.error('Error:', error);
    });



function getXPath(element) {{
    var xpath = '';
    for (; element && element.nodeType == 1; element = element.parentNode) {{
        var id = $(element.parentNode).children(element.tagName).index(element) + 1;
        id = id > 1 ? '[' + id + ']' : '';
        xpath = '/' + element.tagName.toLowerCase() + id + xpath;
    }}
    return xpath;
}}

var input_prev = [];
function getText() {{
    const inputs = document.getElementsByTagName('input');
    let input_data = [];

    for (var i = 0; i < inputs.length; i++) {{
        if (inputs[i].value !== '') {{
            let path = getXPath(inputs[i]); // Calculate XPath inside the loop

            if (!input_prev.some(([prevPath, prevValue]) => prevPath === path && prevValue === inputs[i].value)){{
                input_prev.push([path, inputs[i].value]);
                input_data.push([path, inputs[i].value]);
            }}
        }}
    }}
    return input_data.toString();
}}

function clickLink(target){{
    const eleTarget = target;
    if (eleTarget.href){{
        return eleTarget.href;
    }} else {{
        return "";
    }}
}}