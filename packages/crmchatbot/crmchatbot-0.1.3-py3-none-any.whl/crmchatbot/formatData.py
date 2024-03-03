def format_data(json_response):
    formatted_data = []
    for data in json_response.get('value', []):
        data_details = []
        for key, value in data.items():
            if not key.startswith('@odata'):
                data_details.append(f"{key.capitalize()}: {value}")
        final_data = "\n".join(data_details)
        formatted_data.append(final_data + "\n\n---\n")

    return "\n".join(formatted_data).rstrip("\n\n---\n")
