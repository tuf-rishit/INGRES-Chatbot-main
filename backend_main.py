from backend.nlu_model import interpret_query
from database.db_connect import run_query

def process_user_query(text):
    intent, filters = interpret_query(text)

    if intent == "groundwater_status":
        query = f"SELECT * FROM groundwater WHERE block='{filters['block']}';"
        result = run_query(query)

        if len(result) > 0:
            formatted = format_response(result)
            return formatted, convert_to_chart(result)
        else:
            return "❌ No data found for this block. Try again.", None

    return "⚠ I could not understand your question. Try asking: `status of Indore block`", None

def format_response(result):
    r = result[0]
    return (f"📍 **Block:** {r['block']} ({r['district']}, {r['state']})\n"
            f"🔹 **Recharge:** {r['recharge']} MCM\n"
            f"🔹 **Extraction:** {r['extraction']} MCM\n"
            f"🔹 **Stage:** **{r['stage']}**\n"
            f"📅 **Year:** {r['year']}")

def convert_to_chart(records):
    return {
        "year": [r["year"] for r in records],
        "extraction": [r["extraction"] for r in records],
        "recharge": [r["recharge"] for r in records]
    }