import pyautogui
import pyperclip
import time
from google import genai
from google.genai import types


def extract_response_text(response):
    if response is None:
        return ""
    if isinstance(response, str):
        return response

    text = getattr(response, "text", None)
    if isinstance(text, str) and text:
        return text

    for attr in ("output_text", "content", "message"):
        value = getattr(response, attr, None)
        if isinstance(value, str) and value:
            return value
        if value is not None:
            nested = extract_response_text(value)
            if nested:
                return nested

    candidates = getattr(response, "candidates", None)
    if candidates:
        for candidate in candidates:
            content = getattr(candidate, "content", None)
            if content is not None:
                parts = getattr(content, "parts", None)
                if parts:
                    for part in parts:
                        part_text = getattr(part, "text", None)
                        if isinstance(part_text, str) and part_text:
                            return part_text
                nested = extract_response_text(content)
                if nested:
                    return nested

    choices = getattr(response, "choices", None)
    if choices:
        for choice in choices:
            message = getattr(choice, "message", None)
            if message is not None:
                content = getattr(message, "content", None)
                if isinstance(content, str) and content:
                    return content
                nested = extract_response_text(message)
                if nested:
                    return nested

    return ""


client = genai.Client(api_key="YOUR_KEY")
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.3


def copy_chat_text():
    pyautogui.click(900, 730)
    time.sleep(0.4)

    pyautogui.hotkey("ctrl", "a")
    time.sleep(0.2)
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.3)

    text = pyperclip.paste()
    if not text or not text.strip():
        pyautogui.press("esc")
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "a")
        time.sleep(0.2)
        pyautogui.hotkey("ctrl", "c")
        time.sleep(0.3)
        text = pyperclip.paste()

    return text


def main():
    time.sleep(3)

    text = copy_chat_text()
    if not text or not text.strip():
        raise RuntimeError("Could not copy chat text. Make sure WhatsApp is focused and the chat window is open.")

    print(repr(text))

    completion = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=text,
        config=types.GenerateContentConfig(
            system_instruction="""
You are Mayuri.
You are chatting on WhatsApp with your friends.
Read the chat history and generate ONLY Mayuri's next reply.

Rules:
- Reply naturally.
- Use Hindi or English mix.
- Keep it short (1-2 lines).
- Don't explain.
- Don't repeat the chat.
- Never mention you are an AI.
"""
        )
    )
    response_text = extract_response_text(completion)
    if not response_text:
        raise RuntimeError(f"Could not parse Gemini response: {completion}")

    pyperclip.copy(response_text)
    # Step 1: Click on message input box
    pyautogui.click(591, 677)
    time.sleep(0.5)

    # Step 2: Paste the text
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.5)

    # Step 3: Press Enter
    pyautogui.press("enter")


if __name__ == "__main__":
    main()