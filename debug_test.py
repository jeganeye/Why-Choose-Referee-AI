try:
    from gemini_utils import explain_tradeoffs
    print("Import successful")
    
    result = explain_tradeoffs('iPhone', 'Android', 'battery life')
    print("RESULT:")
    print(result)
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()