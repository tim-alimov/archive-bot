# User Flows: Telegram Archive Bot

## 1. Admin Flow: Archiving a New Item
*How the creator stores and indexes a file.*

1. **Upload:** The Admin uploads or forwards a file, video, or text message to the private Archive Channel.
2. **Trigger Archive:** The Bot automatically detects the new message and attaches an "Archive" inline button to it (or the Admin replies to the message with a command).
3. **Name the Item:** The Admin taps "Archive" and is prompted by the bot to type a clean display name for the item.
4. **Assign Category:** The Admin selects an existing category from an inline keyboard or types a new category name to create one.
5. **Completion:** The item is successfully indexed in the database and is immediately available to end-users.

---

## 2. End-User Flow: Standard Browsing
*How a user organically navigates the bot to find resources.*

1. **Start:** The user opens the bot DM and sends `/start`.
2. **Category Menu:** The bot responds with a Reply Keyboard displaying all available categories.
3. **Select Category:** The user taps a category button (e.g., "Python Scripts").
4. **View Items:** The bot sends a message containing the category description, accompanied by inline buttons for every item inside that category.
5. **Retrieve Asset:** The user taps an item’s inline button. The bot instantly forwards or sends the requested file directly into the DM.

---

## 3. End-User Flow: Deep Link Retrieval
*How a user gets exactly what they need from an external link (e.g., YouTube description).*

1. **Click Link:** The user clicks a deep link provided by the creator (e.g., `t.me/YourArchiveBot?start=file_402`).
2. **Launch Bot:** The Telegram app opens directly to the bot DM with the "Start" button pre-loaded with the deep link payload.
3. **Instant Delivery:** Upon tapping "Start", the bot bypasses the category menu and instantly sends the exact requested file or specific category view to the user.
