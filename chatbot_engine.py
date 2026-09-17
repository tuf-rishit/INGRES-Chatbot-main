from database.db_connect import get_groundwater_data
from backend.translator import translate_text

# Load database once
GW_DATA = get_groundwater_data()


# ---------------------------------------------------------
# 1. FILTER DATAFRAME USING USER INPUT
# ---------------------------------------------------------
def get_groundwater_dataframe(user_input):
    """
    Returns a filtered DataFrame based on district or block name.
    Case-insensitive matching.
    """
    df_filtered = GW_DATA[
        GW_DATA["District"].str.lower().str.contains(user_input.lower()) |
        GW_DATA["Block"].str.lower().str.contains(user_input.lower())
    ]

    return df_filtered


# ---------------------------------------------------------
# 2. CONVERT FILTERED DATA INTO READABLE TEXT
# ---------------------------------------------------------
def generate_text_response(df):
    """
    Converts a filtered DataFrame into a readable chatbot text.
    """
    if df.empty:
        return "No data found for this location."

    response = ""

    for _, row in df.iterrows():
        response += (
            f"Year: {row['Year']} | "
            f"District: {row['District']} | "
            f"Block: {row['Block']} | "
            f"Extractable Groundwater: {row['TOTAL_EXTRACTABLE_GW_MCM']} MCM | "
            f"Extracted: {row['EXTRACTED_GW_MCM']} MCM | "
            f"Stage: {row['STAGE_OF_EXTRACTION_PERCENT']}% | "
            f"Category: {row['CATEGORY']}\n"
        )

    return response


# ---------------------------------------------------------
# 3. MAIN FUNCTION — FILTER + FORMAT + TRANSLATE
# ---------------------------------------------------------
def query_groundwater_text(df, target_lang="en"):
    """
    Handles translation of chatbot response.
    """
    text_response = generate_text_response(df)
    translated = translate_text(text_response, target_lang)
    return translated