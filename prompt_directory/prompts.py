def prompt_func_gemma_for_json(free_text, type_name, schema, description):
    prompt = f"""
    Extract information from the provided text and format it according to the given JSON schema. If a field is not mentioned in the text, set its value to "null" (with quotes). Follow the schema exactly.

    Example 1:
    - Free text: 
    "Please generate a Weather Alert - other for area code 2001. Alert type is Thunderstorm. Intensity: severe. Urgency: high. Ignore the forecast source for now. The duration of this case, I'd say, is around two. severity is empty or unclear"
    - Schema:
    {{
        "alertType": "string",
        "areaCode": "int",
        "intensity": "string",
        "urgency": "string",
        "forecastSource": "string",
        "duration": "int",
        "ruleInstanceName": "string",
        "severity": "int"
    }}
        "ruleInstanceName" field should be: "Weather Alert - ?". ? length should be about 1-3 words.


    - Output:
    {{"alertType": "Thunderstorm","areaCode": 2001,"intensity": "severe","urgency": "high","forecastSource": "null","duration": 2,"ruleInstanceName": "Weather Alert - other","severity": "null"}}

    Example 2: 
    - Free text: 
     "Add a report for 'Shell Delay'. Equipment Malfunction case. Type: shell. Site is not important. Malfunction at level five, urgency four. Desc: Detonation delayed in poland Severity i think 3.",
    - Schema:
    {{
        "type": "string",
        "site": "string",
        "malfunctionLevel": "int",
        "urgency": "int",
        "description": " string",
        "ruleInstanceName": "string",
        "severity": "int"
    }}
    "ruleInstanceName" field should be: "Equipment Malfunction - ?". ? length should be about 1-3 words.

    - Output:
    {{"type": "shell","site": "empty","malfunctionLevel": 5,"urgency": 4,"description": "Detonation delayed in poland","ruleInstanceName": "Equipment Malfunction - Shell Delay","severity": 3}}

    (The severity parameter means the severity level of the alert)


    Now process this input:
    - Free text: {free_text}
    - Schema: {schema}
    "ruleInstanceName" field should be: "{type_name} - ?". ? length should be about 1-3 words.
    - Context for fields (do not fill): {description}
    - Output:
    """
    return prompt


##########################


default_prompt_funcs = {
    "gemma": prompt_func_gemma_for_json
}
