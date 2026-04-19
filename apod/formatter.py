import textwrap

# Format multiple astronomical pictures of the day.
def format_apod(data):
    if isinstance(data, list):
        results = []
        for item in data:
            results.append(format_single_apod(item))
        return "\n\n    ---\n".join(results)
    else:
        return format_single_apod(data)

# Format one APOD.
def format_single_apod(data):
    title = data.get("title", "N/A")
    date = data.get("date", "N/A")
    url = data.get("url", "N/A")
    get_explanation = data.get("explanation", "N/A")
    wrapped_explanation = textwrap.wrap(get_explanation, width=80)
    explanation = "\n".join(wrapped_explanation)

    return (f"""

    Title: {title}
    Date: {date}
    URL: {url}

    Explanation:
{textwrap.indent(explanation, '    ')}
""")
