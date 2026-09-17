import re

def interpret_query(query):
    query = query.lower().strip()

    # Detect groundwater intent
    keywords = ["groundwater", "water level", "status", "recharge", "extraction", "block", "district", "state"]
    
    if any(word in query for word in keywords):
        # Extract location from query
        match = re.search(r"status\s+(\w+)|groundwater\s+(\w+)|in\s+(\w+)", query)
        
        if match:
            location = match.group(1) or match.group(2) or match.group(3)
            return "groundwater_query", location.capitalize()

        # If no location found
        return "groundwater_query", None

    return "unknown", None