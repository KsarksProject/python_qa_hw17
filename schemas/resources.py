resource_schema = {
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "year": {"type": "integer"},
                "color": {"type": "string"},
                "pantone_value": {"type": "string"}
            },
            "required": ["id", "name", "year", "color", "pantone_value"]
        },
        "support": {
            "type": "object",
            "properties": {
                "url": {"type": "string", "format": "uri"},
                "text": {"type": "string"}
            },
            "required": ["url", "text"]
        }
    },
    "required": ["data", "support"]
}
