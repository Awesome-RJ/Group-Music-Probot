from os import getenv

from dotenv import load_dotenv

load_dotenv()

SESSION_NAME = getenv("BQAyd3DsG4YsTe8yWZYnWJDeZY_E5QfQVEaVAHcDHeFXICJPSwB1iKOfruhEG5ASfymtkBQagr85P1rhkFXlaUVzKAYIeCOt0wklQJY3twDzWV4KcAgORiFp4M9bBVfZI7JaffLGd6-LODNN6PSn_9DTH5qTqKP5f-AusIRXNzQi_IJaVfWBV1pmf9M20lrexnFgucwctq4PUDbRaZ1d8mADAvWMKzliiY6UGWVhgrnpmVTUaCUS0Al9ksWm8psqGy3S6tVZPLErPS3ATpOF43BcJMt98685MutycMf7h9crsUNNNIseV6KMH-8yuWZPjagVDlnR5tZuPUH-yVDiTwMbPtmoUAA", "session")
BOT_TOKEN = getenv("1556849815:AAGyafjOM5BOEsPXRrTWf0YouMUhdcaUo0E")
BOT_NAME = getenv("Group Music Bot")

API_ID = int(getenv("3397400"))
API_HASH = getenv("6b6069887e823aade4dad8fb576f6ad2")

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("1418166549").split()))
